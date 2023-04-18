from django import template
from my_wallet.models import Wallet

register = template.Library()


@register.simple_tag()
def get_wallets():
    return Wallet.objects.all()
