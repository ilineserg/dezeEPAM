from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth

articles_of_stories = []

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "cache-control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "cookie": "pkbRem=%7B%22uid%22%3A3011766%2C%22username%22%3A%22ilineserg%22%2C%22rem%22%3A%226aebdf22bb6e139da1a0dc5b033ae8de%22%2C%22tries%22%3A0%7D"
}

username = 'ilineserg'
password = 'TestPassword1'

url = 'https://pikabu.ru/subs'
sess = requests.Session()

resp = sess.post(url, headers=headers, data={'username': username, 'password': password})

soup = BeautifulSoup(resp.text, 'html.parser')
articles_of_stories.extend(soup.find_all('article'))

"""while len(articles_of_stories) < 100:
    page = 2
    resp = sess.post(url + f'?page={page}', headers=headers, data={'username': username, 'password': password})
    soup = BeautifulSoup(resp.text, 'html.parser')
    articles_of_stories.extend(soup.find_all('article'))
    page += 1"""

"""if len(articles_of_stories) > 100:
    while len(articles_of_stories) != 100:
        articles_of_stories.pop()

print(len(articles_of_stories))"""


with open("file.html", "w") as articles:
    #articles.write(str(articles_of_stories[0]))
    articles.write(resp.text)