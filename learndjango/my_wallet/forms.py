from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Wallet


class AddWalletForm(forms.Form):
    name = forms.CharField(max_length=50, label='Название', required=False)
    wallets = forms.ModelMultipleChoiceField(queryset=None, required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['wallets'].queryset = Wallet.objects.filter(user__username=self.user)


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class AddTransactionForm(forms.Form):
    description = forms.CharField(max_length=50, label='Название')
    amount = forms.CharField(max_length=50, label='Цена')
    wallet = forms.CharField(max_length=50, label='Wallet')
