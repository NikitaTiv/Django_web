from django import forms
from .models import Wallet


class AddWalletForm(forms.Form):
    name = forms.CharField(max_length=50, label='Название', required=False)
    wallets = forms.ModelMultipleChoiceField(queryset=Wallet.objects.all(), required=False)
