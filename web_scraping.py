import requests
from bs4 import BeautifulSoup
import sys
import io

# Set stdout to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

baseurl = 'https://quotes.toscrape.com/' # get the base url

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0'
}
x=0
product_link = []

while True:
    x+=1
    # print('works')
    r = requests.get(f'https://quotes.toscrape.com/page/{x}/') # get the current url(all of it)
    soup = BeautifulSoup(r.content, 'lxml')
    if soup.find_all('div', class_='row')[1].find('div', class_='col-md-8').get_text(strip=True) == 'No quotes found!←Previous':
        break

    product_list = soup.find_all('div', class_='quote')

    for quotes in product_list:
        # print('working')
        link = quotes.find_all('span')
        a = link[1].find('a',href=True)['href']
        product_link.append(baseurl+a) 

print(len(product_link))