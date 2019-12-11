from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth


user_agent = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

username = 'ilineserg'
password = 'TestPassword1'

url = 'https://pikabu.ru'
sess = requests.Session()
sess.verify = True

resp = sess.post(url, headers=user_agent, data={'username': username, 'password': password})
resp.raise_for_status()

print(sess.cookies)
resp = sess.get(url + '/subs')
resp.raise_for_status()

print(resp.text.count('ilineserg'))