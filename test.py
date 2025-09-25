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

link = 'https://quotes.toscrape.com/author/Alexandre-Dumas-fils'
