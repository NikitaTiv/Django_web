from django.shortcuts import redirect, render, HttpResponse


def index(request):
    return render(request, 'my_wallet/index.html')


def get_my_wallets(request):
    context = {'title': 'My wallets', }
    return render(request, 'my_wallet/my_wallet.html', context=context)


def register(request):
    return HttpResponse('Registration')


def authorization(request):
    return HttpResponse('Authorization')


def edit_profile(request):
    return HttpResponse('Редактирование профиля')


def get_wallet_info(request, wallet_id):
    return HttpResponse(f'Информация о wallet {wallet_id}')


def statistics(request):
    return HttpResponse('Statistics')
