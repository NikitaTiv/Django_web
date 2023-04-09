from django.shortcuts import render, HttpResponse


def news(request):
    return render(request, 'my_wallet/news.html')


def get_news(request, news_id):
    return HttpResponse(f"Новость c id={news_id}")


def get_my_wallets(request):
    return render(request, 'my_wallet/my_wallet.html')


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
