import sys
import requests
from bs4 import BeautifulSoup


payload={
    'session_key' : 'gokadi7@yandex.ru',
    'session_password' : 'sea1235813'
}

URL = 'https://www.linkedin.com/uas/login-submit'
s = requests.session()
s.post(URL, data=payload)

r = s.get('http://www.linkedin.com/nhome')
soup = BeautifulSoup(r.text)
print(soup.find('title'))
