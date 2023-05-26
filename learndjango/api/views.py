from rest_framework import generics

from my_wallet.models import News, Wallet
from api.permissions import IsOwner
from api.serializers import NewsSerializer, WalletSerializer


class NewsAPIList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class WalletAPIList(generics.ListAPIView):
    serializer_class = WalletSerializer

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)


class WalletAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = 'name'
    permission_classes = (IsOwner,)


class WalletAPICreate(generics.CreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
