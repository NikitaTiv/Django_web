from django.urls import path

from my_wallet.views import (NewsHome, ShowNews, MyWallet, add_wallet, delete_wallet, RegisterUser, LoginUser,
                             open_wallet, logout_user, edit_profile, WalletInfo, statistics, delete_transaction)

urlpatterns = [
    path('news/', NewsHome.as_view(), name='home'),
    path('news/<slug:news_slug>', ShowNews.as_view(), name='news'),
    path('wallets/', MyWallet.as_view(), name='wallets'),
    path('wallets/add_wallet', add_wallet, name='add_wallet'),
    path('wallets/delete_wallet', delete_wallet, name='delete_wallet'),
    path('wallets/open_wallet', open_wallet, name='open_wallet'),
    path('wallets/<slug:wallet_slug>/', WalletInfo.as_view(), name='wallet_info'),
    path('delete_transaction/<int:transaction_id>/', delete_transaction, name='delete_transaction'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('statistics/', statistics, name='statistics'),
]
