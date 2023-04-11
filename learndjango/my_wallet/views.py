from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

from my_wallet.forms import AddWalletForm
from my_wallet.models import News, Wallet


def news(request):
    return render(request, 'my_wallet/news.html')


def show_news(request, news_slug):
    post = get_object_or_404(News, slug=news_slug)
    context = {
        'post': post,
    }
    return render(request, 'my_wallet/show_news.html', context=context)


def get_my_wallets(request):
    form = AddWalletForm()
    context = {
        'form': form,
    }
    return render(request, 'my_wallet/my_wallet.html', context=context)


def add_wallet(request):
    wallet_name = request.POST['name']
    if wallet_name:
        Wallet.objects.create(name=wallet_name)
    return redirect('wallets')


def delete_wallet(request):
    wallet_id = request.POST.get('wallets', False)
    if wallet_id:
        wallet = Wallet.objects.get(pk=wallet_id)
        wallet.delete()
    return redirect('wallets')


def register(request):
    return HttpResponse('Registration')


def authorization(request):
    return HttpResponse('Authorization')


def edit_profile(request):
    return HttpResponse('Редактирование профиля')


def get_wallet_info(request, wallet_id):
    context = {
        'wallet_id': wallet_id,
    }
    return render(request, 'my_wallet/transaction.html', context=context)


def statistics(request):
    return HttpResponse('Statistics')
