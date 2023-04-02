from django.urls import path

from my_wallet.views import index, my_wallet

urlpatterns = [
    path('', index, name='home'),
    path('my_wallet/', my_wallet, name='news'),
]
