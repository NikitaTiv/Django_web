from django.urls import path

from my_wallet.views import (NewsHome, ShowNews, MyWallet, add_wallet, delete_wallet, register, authorization,
                             edit_profile, WalletInfo, statistics)

urlpatterns = [
    path('news/', NewsHome.as_view(), name='home'),
    path('news/<slug:news_slug>', ShowNews.as_view(), name='news'),
    path('wallets/', MyWallet.as_view(), name='wallets'),
    path('wallets/add_wallet', add_wallet, name='add_wallet'),
    path('wallets/delete_wallet', delete_wallet, name='delete_wallet'),
    path('wallets/<slug:wallet_slug>/', WalletInfo.as_view(), name='wallet_info'),
    path('register/', register, name='register'),
    path('authorization/', authorization, name='authorization'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('statistics/', statistics, name='statistics'),
]
