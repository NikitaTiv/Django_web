from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy

from my_wallet.forms import AddWalletForm, RegisterUserForm
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
    login_url = reverse_lazy('home')


@login_required
def add_wallet(request):
    wallet_name = request.POST.get('name', False)
    if wallet_name:
        Wallet.objects.create(name=wallet_name)
    return redirect('wallets')


@login_required
def delete_wallet(request):
    wallet_id = request.POST.get('wallets', False)
    if wallet_id:
        wallet = Wallet.objects.get(pk=wallet_id)
        wallet.delete()
    return redirect('wallets')


def register(request):
    form = RegisterUserForm()
    return render(request, 'my_wallet/registration.html', {'form': form})


def authorization(request):
    return HttpResponse('Authorization')


def edit_profile(request):
    return HttpResponse('Редактирование профиля')


class WalletInfo(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'my_wallet/transaction.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(wallet__slug=self.kwargs['wallet_slug'])


def statistics(request):
    return HttpResponse('Statistics')
