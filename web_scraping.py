import pprint
import requests
from bs4 import BeautifulSoup
import sys
import io

printer = pprint.PrettyPrinter()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

baseURL = 'https://quotes.toscrape.com'
baseurl = 'https://quotes.toscrape.com/' # get the base url

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070213 BonEcho/2.0.0.2pre'
}

page_url = 'https://quotes.toscrape.com/page/1'
author_links = []

# while page_url:

#     r = requests.get(page_url) # Current page we want to scrape
#     soup = BeautifulSoup(r.content, 'lxml')

#     quotes = soup.find_all('div', class_='quote')
#     # print(quotes)

#     author_set = {link for item in quotes for span in item.find_all('span') for link in span.find_all('a', href=True)}

#     for author in author_set:
#         author_links.append(baseURL + author['href'])
    
#     next_page = soup.find('li', class_='next')
    
#     if next_page:
#         page_url = (baseURL + next_page.find('a', href=True)['href'])
#     else:
#         print('Last page reached')
#         page_url = None

# author_links = list(set(author_links))
# # printer.pprint(author_links)
# print(len(author_links))

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