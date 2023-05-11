from datetime import datetime

from learndjango.my_wallet.utils.parsers.utils_parser import get_parse_date_tuple

def test__get_parse_date_tuple__success_case():
    today = datetime.now()
    assert get_parse_date_tuple() == (today.strftime("%Y"), today.strftime("%m"), today.strftime("%d"))
