import pprint
import creds
import pandas as pd
from session_manager import get_logged_in_session
from parser import author_data_scraper, quotes_data_scraper

MY_USERNAME = creds.username
MY_PASSWORD = creds.password

printer = pprint.PrettyPrinter()

base_url = 'https://quotes.toscrape.com' # Base site url
page_url = 'https://quotes.toscrape.com/page/1'

# Get user agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070213 BonEcho/2.0.0.2pre'
}

session = get_logged_in_session(MY_USERNAME, MY_PASSWORD)
quotes_data_list = []
author_data_list = []

if session:
    try:
        print('# Saving quotes...')
        quotes_data_list, author_data_list = quotes_data_scraper(session, page_url, base_url, headers) 
        print('# Saving quotes completed...')
        
        print('# Saving author data...')
        author_info_list = author_data_scraper(author_data_list, headers)
        print('# Saving author data completed...')
        
        print('Converting data to csv...')
        quotes_df = pd.DataFrame(quotes_data_list, index=False)
        authors_df = pd.DataFrame(author_info_list, index=False)
        print('Csv conversion completed...')
        
        authors_df.to_csv('Authors.csv')
        quotes_df.to_csv('Quotes.csv')
    finally:
        print("\nClosing session")
        session.close()