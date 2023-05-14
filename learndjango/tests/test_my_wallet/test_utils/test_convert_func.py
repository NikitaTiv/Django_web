from datetime import datetime
import pytest

from learndjango.my_wallet.utils.convert_func import convert_date

@pytest.mark.parametrize(
    'date_1, date_2, expected_result_1, expected_result_2',
    [
        ('31/12/2023', '31/12/2023', datetime(2023, 12, 31, 0, 0), datetime(2023, 12, 31, 0, 0)),
        ('', '', None, None),
    ],
    ids=[
        'success_case',
        'fail_case',
    ],
)
def test__convert_func(date_1, date_2, expected_result_1, expected_result_2):
    assert convert_date(date_1, date_2) == (expected_result_1, expected_result_2)
