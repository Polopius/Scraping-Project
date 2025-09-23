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
quotes_data_list = []

while page_url:
    r = requests.get(page_url) # Current page we want to scrape
    soup = BeautifulSoup(r.content, 'lxml')

    quotes = soup.find_all('div', class_='quote')
    
    for item in quotes:
        # Get quotes, author name, and tags
        quote_text = item.find('span', class_='text').text.strip()
        
        author_name = item.find('small', class_='author').text.strip()
        
        tags = [tag.text.strip() for container in item.find_all('div', class_='tags') for tag in container.find_all('a', class_='tag')]
        
        # Append to quote data list
        quotes_data_list.append({
            'quotes' : quote_text,
            'author' : author_name,
            'tags' : tags
        })
    
    next_page = soup.find('li', class_='next')
    if next_page:
        page_url = (baseURL + next_page.find('a', href=True)['href'])
    else:
        print('Last page reached')
        page_url = None

printer.pprint(quotes_data_list)