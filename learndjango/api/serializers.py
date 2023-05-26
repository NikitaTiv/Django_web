from rest_framework import serializers

from my_wallet.models import News, Wallet


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'content', 'time_create')


class WalletSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Wallet
        fields = ('name', 'user')
