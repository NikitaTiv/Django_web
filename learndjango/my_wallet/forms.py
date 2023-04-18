from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Wallet


class AddWalletForm(forms.Form):
    name = forms.CharField(max_length=50, label='Название', required=False)
    wallets = forms.ModelMultipleChoiceField(queryset=Wallet.objects.all(), required=False)


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'password2')
