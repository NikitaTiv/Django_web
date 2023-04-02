from django.shortcuts import render


def index(request):
    return render(request, 'my_wallet/index.html')


def my_wallet(request):
    return render(request, 'my_wallet/my_wallet.html', {'title': 'Главная страница'})
