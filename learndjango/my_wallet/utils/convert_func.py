from datetime import datetime


def convert_date(request_date_from: str, request_date_to: str) -> tuple[datetime | None, datetime | None]:
    date_from = datetime.strptime(request_date_from, '%d/%m/%Y') if request_date_from else None
    date_to = datetime.strptime(request_date_to, '%d/%m/%Y') if request_date_to else None
    return date_from, date_to
