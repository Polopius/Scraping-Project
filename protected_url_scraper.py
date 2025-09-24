import pprint
import creds
import pandas as pd
from bs4 import BeautifulSoup
from session_manager import get_logged_in_session
from good_data import get_gud
MY_USERNAME = creds.username
MY_PASSWORD = creds.password

printer = pprint.PrettyPrinter()

base_url = 'https://quotes.toscrape.com' # Base site url
page_url = 'https://quotes.toscrape.com/page/1'

'''
# Get user agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070213 BonEcho/2.0.0.2pre'
}
'''
session = get_logged_in_session(MY_USERNAME, MY_PASSWORD)
quotes_data_list = []
author_data_list = []
link = []

if session:
    try:
        while page_url:
            r = session.get(page_url)
            soup = BeautifulSoup(r.content, 'lxml')
            quotes = soup.find_all('div', class_='quote')
            for item in quotes:
                good = [ref['href'].replace('http://', 'https://', 1) for ref in item.find_all('a', href=True)]
                link.append(good[1])

            next_page = soup.find('li', class_='next')
            # print(next_page)
            if next_page:
                page_url = (base_url + next_page.find('a', href=True)['href'])
            else:
                print('Last page reached')
                page_url = None
        link = list(dict.fromkeys(link))
        

    finally:
        print("Closing session")
        session.close()
