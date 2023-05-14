from learndjango.my_wallet.utils.get_filters import get_filters


def test__get_filters__success_case(filters):
    assert get_filters() == filters
