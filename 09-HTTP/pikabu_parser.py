import os

from bs4 import BeautifulSoup
from collections import Counter
import requests


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SUBS_URL = "https://pikabu.ru/new/subs"

COOKIE = "INPUT YOUR COOKIE HERE"
MAX_ARTICLES = 100


def article_parser(text):
    soup = BeautifulSoup(text, 'lxml')
    container = soup.find('div',  class_="stories-feed__container")
    articles = container.find_all('div', class_="story__main")
    result = []
    for article in articles:
        title = article.find('a', class_="story__title-link")
        if title:
            title = title.text.strip()
        else:
            continue

        tags_container = article.find('div', class_="story__tags")
        tags = tags_container.find_all('a', class_="tags__tag")
        tags = list(map(lambda a: a.text.strip(), tags))
        tags = list(filter(lambda a: a != '[моё]', tags))

        if not all([title, tags]):
            continue
        result.append((title, tags))

    return result


def main():
    articles_of_stories = []
    tags_counter = Counter()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "cookie": COOKIE,
    }

    session = requests.Session()
    session.headers.update(headers)

    count = 0
    page = 1

    while count < MAX_ARTICLES:
        params = {}
        if page != 1:
            params.update({"page": page})

        r = session.get(url=SUBS_URL, params=params, allow_redirects=True)

        print(r.url)
        print("page", page)

        for title, tags in article_parser(text=r.text):
            if count >= MAX_ARTICLES:
                break
            articles_of_stories.append((title, tags))
            for tag in tags:
                tags_counter[tag] += 1
            count += 1

        print("count", count)
        page += 1

    with open(os.path.join(BASE_PATH, "most_popular_tag.txt"), "w") as tags_file:
        most_popular_tags = tags_counter.most_common(10)
        tags_file.write(f"Most popular tags:\n")

        for idx, tag in enumerate(most_popular_tags):
            tag_name, tag_mentions = tag
            tags_file.write(f"{idx + 1}. \"{tag_name}\": {tag_mentions}\n")


if __name__ == "__main__":
    main()