from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.shortcuts import HttpResponse, redirect, HttpResponseRedirect, render
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy, reverse
from transliterate import translit

from my_wallet.forms import AddWalletForm, RegisterUserForm, AddTransactionForm, StatReportForm
from my_wallet.models import News, Wallet, Transaction
from my_wallet.utils.convert_func import convert_date
from my_wallet.utils.db_functions import get_objects_list


class NewsHome(ListView):
    paginate_by = 6
    model = News
    template_name = 'my_wallet/news.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.order_by('-id').filter(is_published=True)


class ShowNews(DetailView):
    model = News
    template_name = 'my_wallet/show_news.html'
    slug_url_kwarg = 'news_slug'
    context_object_name = 'post'


class MyWallet(LoginRequiredMixin, FormView):
    form_class = AddWalletForm
    template_name = 'my_wallet/my_wallet.html'

    def get_form_kwargs(self):
        kwargs = super(MyWallet, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


@login_required
def add_wallet(request):
    wallet_name = request.POST.get('name', False)
    if wallet_name:
        if Wallet.objects.filter(user=request.user, name=wallet_name).exists():
            messages.success(request, 'Такой Wallet уже существует.')
        else:
            slug = translit(wallet_name, language_code='ru', reversed=True)
            slug_without_spaces = slug.replace(' ', '_')
            Wallet.objects.create(name=wallet_name, slug=slug_without_spaces.lower(), user_id=request.user.id)
    return redirect('wallets')


@login_required
def delete_wallet(request):
    wallet_id = request.POST.get('wallets', False)
    if wallet_id:
        wallet = Wallet.objects.get(pk=wallet_id)
        wallet.delete()
    return redirect('wallets')


@login_required
def open_wallet(request):
    wallet_id = request.POST.get('wallets', False)
    if wallet_id:
        wallet = Wallet.objects.values('slug').get(pk=wallet_id)
        return HttpResponseRedirect(reverse('wallet_info', args=[wallet['slug']]))
    return redirect('wallets')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'my_wallet/registration.html'

    def form_valid(self, form):
        try:
            user = form.save()
            login(self.request, user)
            return redirect('home')
        except IntegrityError:
            messages.success(self.request, "Такой email уже существует.")
            return redirect('register')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'my_wallet/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def edit_profile(request):
    return HttpResponse('Редактирование профиля')


class WalletInfo(LoginRequiredMixin, ListView, FormView):
    form_class = AddTransactionForm
    model = Transaction
    template_name = 'my_wallet/transaction.html'
    context_object_name = 'transactions'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wallet_name'] = self.kwargs['wallet_slug']
        return context

    def get_queryset(self):
        if Wallet.objects.filter(user__username=self.request.user, slug=self.kwargs['wallet_slug']).exists():
            current_wallet_id = Wallet.objects.values('id').get(
                user__username=self.request.user, slug=self.kwargs['wallet_slug']
            )
            if Wallet.objects.get(pk=current_wallet_id['id']).transaction_set.count() > 0:
                return Transaction.objects.order_by('-time_create').filter(
                    wallet=current_wallet_id['id']
                ).select_related('wallet')
            else:
                return [
                    Transaction(
                        description='В этом кошельке еще нет транзакций', amount='', time_create='', wallet=None
                    ),
                ]


@login_required
def add_transaction(request, wallet_name):
    wallet_description = request.POST.get('description', False)
    wallet_amount = request.POST.get('amount', False)
    wallet = Wallet.objects.values('id').get(slug=wallet_name, user__username=request.user)
    if wallet_description and wallet_amount and wallet:
        try:
            Transaction.objects.create(
                description=wallet_description, amount=wallet_amount, wallet_id=wallet['id'],
            )
        except ValidationError:
            messages.success(request, "Поле 'Цена' должна содержать число.")

    return HttpResponseRedirect(reverse('wallet_info', args=[wallet_name]))


def delete_transaction(request, transaction_id):
    deleted_transaction = Transaction.objects.get(pk=transaction_id)
    deleted_transaction.delete()
    return HttpResponseRedirect(reverse('wallet_info', args=[deleted_transaction.wallet.slug]))


@login_required
def statistics(request):
    form = StatReportForm(request.POST) if request.method == "POST" else StatReportForm()
    try:
        date_from, date_to = convert_date(request.POST.get('date_from', None), request.POST.get('date_to', None))
    except ValueError:
        messages.success(request, "Дата указана не корректно.")
        return redirect('statistics')
    ordering = request.POST['filters'] if request.method == "POST" else '-time_create'
    transactions = get_objects_list(date_from, date_to, ordering, request.user)
    summary = sum([transaction.amount for transaction in transactions])
    return render(request, "my_wallet/statistics.html", {'form': form, 'statistics': transactions, 'summary': summary})
