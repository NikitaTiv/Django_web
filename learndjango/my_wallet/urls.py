from django.urls import path

from my_wallet.views import (index, get_my_wallets, register, authorization,
                             edit_profile, get_wallet_info, statistics)

urlpatterns = [
    path('', index, name='home'),
    path('wallets/', get_my_wallets, name='wallets'),
    path('wallets/<str:wallet_id>/', get_wallet_info, name='wallets'),
    path('register/', register, name='register'),
    path('authorization/', authorization, name='authorization'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('statistics/', statistics, name='statistics'),
]
