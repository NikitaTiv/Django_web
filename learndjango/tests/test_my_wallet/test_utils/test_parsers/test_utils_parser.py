from datetime import datetime
import os

from learndjango.my_wallet.utils.parsers.utils_parser import (get_parse_date_tuple, get_photo_directory,
                                                              download_photo, cut_slug, replace_slug_symblols)

def test__get_parse_date_tuple__success_case():
    assert get_parse_date_tuple() == (
        datetime.now().strftime("%Y"), datetime.now().strftime("%m"), datetime.now().strftime("%d")
    )


def test__get_photo_directory__success_case():
    assert get_photo_directory('2023', '05', '11') == '../../../media/photos/2023/05/11'


def test__download_photo__success_case(file, file_remove):
    download_photo(file['directory'], file['image_url'], file['slug'])
    assert os.path.exists(file['directory'])


def test__cut_slug__success_case():
    assert cut_slug('test_slug_for_tests_very_long') == 'test_slug_for_tests'


def test__replace_slug_symblols__success_case():
    assert replace_slug_symblols(',t.e x:t/') == 'te_xt' 


