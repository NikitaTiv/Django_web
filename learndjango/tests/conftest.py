import pytest
import shutil


@pytest.fixture
def file_remove(file):
    yield
    shutil.rmtree(file['directory'][:29])


@pytest.fixture
def file():
    return {
        'directory': 'learndjango/media/photos/2000/05/11', 
        'image_url': 'https://static01.nyt.com/images/2023/05/13/multimedia/13sportsbet6-ghqc/13sportsbet6-ghqc-moth.jpg',
        'slug': 'test_slug',
    }


@pytest.fixture
def filters():
    return [
        ('-time_create', 'время добавления (по убыванию)'),
        ('time_create', 'время добавления (по возрастанию)'),
        ('description', 'имя (по возрастанию)'),
        ('-description', ' имя (по убыванию)'),
    ]
