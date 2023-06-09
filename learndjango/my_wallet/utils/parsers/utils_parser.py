from datetime import datetime
import os
import requests


def get_parse_date_tuple() -> tuple[str, str, str]:
    today = datetime.now()
    return today.strftime("%Y"), today.strftime("%m"), today.strftime("%d")


def get_photo_directory(year: str, month: str, day: str) -> str:
    return os.path.join('..', '..', '..', 'media', 'photos', year, month, day)


def download_photo(directory: str, image_url: str, slug: str) -> None:
    os.makedirs(directory, exist_ok=True)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:65.0) Gecko/20100101 Firefox/65.0',
    }
    photo = requests.get(image_url, headers=headers)
    out = open(f'{directory}/{slug}.jpg', "wb")
    out.write(photo.content)
    out.close()


def cut_slug(text: str) -> str:
    list_words = text.split("_")
    slug = "_".join(list_words[:4])
    return slug


def replace_slug_symblols(text: str) -> str:
    replace_values = {
        '’': '', ',': '', '.': '', ' ': '_', ':': '', '‘': '', '/': '', "'": '', 'é': '', '#': '', '"': '', '+': '',
    }
    for old_symbol, new_symbol in replace_values.items():
        text = text.replace(old_symbol, new_symbol)
    slug = cut_slug(text)
    return slug
