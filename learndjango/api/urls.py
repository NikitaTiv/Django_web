from django.urls import path

from api.views import WalletAPICreate, NewsAPIList, WalletAPIDetail, WalletAPIList

urlpatterns = [
    path('api/v1/newslist/', NewsAPIList.as_view()),
    path('api/v1/walletlist/', WalletAPIList.as_view()),
    path('api/v1/wallet/', WalletAPICreate.as_view()),
    path('api/v1/wallet/<str:name>/', WalletAPIDetail.as_view()),
]
