from django.urls import path

from my_wallet.views import (news, get_news, get_my_wallets, register, authorization,
                             edit_profile, get_wallet_info, statistics)

urlpatterns = [
    path('', news, name='home'),
    path('news/<int:news_id>', get_news, name='news'),
    path('wallets/', get_my_wallets, name='wallets'),
    path('wallets/<int:wallet_id>/', get_wallet_info, name='wallet_info'),
    path('register/', register, name='register'),
    path('authorization/', authorization, name='authorization'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('statistics/', statistics, name='statistics'),
]
