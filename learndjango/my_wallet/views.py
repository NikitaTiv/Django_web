from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.utils import IntegrityError
from django.shortcuts import HttpResponse, redirect, HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy, reverse
from transliterate import translit

from my_wallet.forms import AddWalletForm, RegisterUserForm, AddTransactionForm
from my_wallet.models import News, Wallet, Transaction


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
    slug = translit(wallet_name, language_code='ru', reversed=True)
    if wallet_name:
        Wallet.objects.create(name=wallet_name, slug=slug.lower(), user_id=request.user.id)
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
    wallet = Wallet.objects.values('slug').get(pk=wallet_id)
    return HttpResponseRedirect(reverse('wallet_info', args=[wallet['slug']]))


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'my_wallet/registration.html'
    success_url = reverse_lazy('login')

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

    def get_queryset(self):
        if Wallet.objects.filter(user__username=self.request.user, slug=self.kwargs['wallet_slug']).exists():
            if Wallet.objects.get(slug=self.kwargs['wallet_slug']).transaction_set.count() > 0:
                return Transaction.objects.filter(wallet__slug=self.kwargs['wallet_slug']).select_related('wallet')
            else:
                return [
                    Transaction(
                        description='В этом кошельке еще нет транзакций', amount='', time_create='', wallet=None
                    ),
                ]


def delete_transaction(request, transaction_id):
    deleted_transaction = Transaction.objects.get(pk=transaction_id)
    deleted_transaction.delete()
    return HttpResponseRedirect(reverse('wallet_info', args=[deleted_transaction.wallet.slug]))


def statistics(request):
    return HttpResponse('Statistics')
