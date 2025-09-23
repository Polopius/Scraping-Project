import pprint
import requests
from bs4 import BeautifulSoup

printer = pprint.PrettyPrinter()

# Base site url
baseURL = 'https://quotes.toscrape.com'

# Get user agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070213 BonEcho/2.0.0.2pre'
}

page_url = 'https://quotes.toscrape.com/page/1'
author_links = []

while page_url:

    r = requests.get(page_url) # Current page we want to scrape
    soup = BeautifulSoup(r.content, 'lxml')

    quotes = soup.find_all('div', class_='quote')
    # print(quotes)

    author_set = {link for item in quotes for span in item.find_all('span') for link in span.find_all('a', href=True)}

    for author in author_set:
        author_links.append(baseURL + author['href'])
    
    next_page = soup.find('li', class_='next')
    
    if next_page:
        page_url = (baseURL + next_page.find('a', href=True)['href'])
    else:
        print('Last page reached')
        page_url = None

author_links = list(set(author_links))
printer.pprint(author_links)