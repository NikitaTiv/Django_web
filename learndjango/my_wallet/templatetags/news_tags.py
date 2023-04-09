from django import template
from my_wallet.models import News

register = template.Library()


@register.simple_tag()
def get_news():
    return News.objects.order_by('-id').filter(is_published=True).all()[:6]
