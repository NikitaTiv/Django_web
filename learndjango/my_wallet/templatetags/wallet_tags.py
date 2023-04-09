from django import template
from my_wallet.models import Wallet, Transaction

register = template.Library()


@register.simple_tag()
def get_wallets():
    return Wallet.objects.all()


@register.inclusion_tag('my_wallet/list_transactions.html')
def get_transactions(wallet_id=None):
    transactions = Transaction.objects.filter(wallet_id=wallet_id)
    return {'transactions': transactions}
