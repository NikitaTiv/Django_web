from datetime import datetime

from learndjango.my_wallet.utils.parsers.utils_parser import get_parse_date_tuple, get_photo_directory

def test__get_parse_date_tuple__success_case():
    assert get_parse_date_tuple() == (
        datetime.now().strftime("%Y"), datetime.now().strftime("%m"), datetime.now().strftime("%d")
    )


def test__get_photo_directory__success_case():
    assert get_photo_directory('2023', '05', '11') == '../../../media/photos/2023/05/11'
