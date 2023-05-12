from datetime import datetime
from dotenv import load_dotenv
import os
import requests

from db_models import News, session
from utils_parser import replace_slug_symblols, get_parse_date_tuple, get_photo_directory, download_photo

load_dotenv()


def get_newsdata_news(url: str) -> list[dict[str, str | list[str] | None]]:
    params = {
        'q': 'business',
        'apiKey': os.getenv('NEWSDATA_API'),
        'language': 'en',
        'country': 'us',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:65.0) Gecko/20100101 Firefox/65.0',
    }
    result = requests.get(url, params=params, headers=headers)
    return result.json()['results']


def save_news(title: str | list[str], content: str | list[str], image_url: str | list[str], slug: str) -> None:
    year, month, day = get_parse_date_tuple()
    directory = get_photo_directory(year, month, day)
    download_photo(directory, image_url, slug)
    news = News(
        title=title, content=content, photo=os.path.join(directory[15:], f'{slug}.jpg'),
        slug=slug, time_create=datetime.now(), is_published=True
    )
    session.add(news)
    session.commit()


def get_news() -> None:
    news = get_newsdata_news('https://newsdata.io/api/1/news')
    for item in news:
        if item['content'] and item['image_url'] and item['title']:
            slug = replace_slug_symblols(item['title']).lower()
            news_exist = session.query(News).filter(News.slug==slug).count()
            if not news_exist:
                save_news(item['title'], item['content'], item['image_url'], slug)
                print('News added.')
            else:
                print('Already exists.')


if __name__ == '__main__':
    get_news()
