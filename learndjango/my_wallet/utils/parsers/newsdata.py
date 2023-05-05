from db import News, session
from dotenv import load_dotenv
import os
import requests

from utils import replace_slug_symblols, save_news

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
