from datetime import datetime, timedelta
from django.db.models.query import QuerySet
import pytz

from my_wallet.models import Transaction

utc=pytz.UTC


def get_transaction_object(ordering: str, user: str) -> QuerySet:
    return Transaction.objects.order_by(ordering).filter(wallet__user=user)


def get_objects_list(date_from: datetime, date_to: datetime, ordering: str, user: str) -> list[Transaction]:
    date_from_local = utc.localize(date_from) if date_from else None
    date_to_local = utc.localize(date_to + timedelta(hours=24)) if date_to else None
    item_list = Transaction.objects.order_by(ordering).filter(wallet__user=user)
    if date_from_local and date_to_local:
        return [item for item in item_list if date_from_local <= item.time_create <= date_to_local]
    if date_from_local:
        return [item for item in item_list if date_from_local <= item.time_create]
    if date_to_local:
        return [item for item in item_list if item.time_create <= date_to_local]
    return item_list
