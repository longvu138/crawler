import requests
from bs4 import BeautifulSoup

respon = requests.get('https://2dep.vn/').text

soup = BeautifulSoup(respon, 'html.parser')

for link in soup.find_all('a'):
    url = link.get('href')
    title = link.getText().strip()
    if link.getText().strip() == '':
        print('title: rỗng - link: ', url)
    else:
        print('title: {} - link: {} '. format(title, url))
