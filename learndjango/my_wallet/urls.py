from django.urls import path

from my_wallet.views import (news, show_news, get_my_wallets, add_wallet, delete_wallet, register, authorization,
                             edit_profile, get_wallet_info, statistics)

urlpatterns = [
    path('news/', news, name='home'),
    path('news/<slug:news_slug>', show_news, name='news'),
    path('wallets/', get_my_wallets, name='wallets'),
    path('wallets/add_wallet', add_wallet, name='add_wallet'),
    path('wallets/delete_wallet', delete_wallet, name='delete_wallet'),
    path('wallets/<int:wallet_id>/', get_wallet_info, name='wallet_info'),
    path('register/', register, name='register'),
    path('authorization/', authorization, name='authorization'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('statistics/', statistics, name='statistics'),
]
