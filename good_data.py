from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070213 BonEcho/2.0.0.2pre'
}

def get_gud(link):
    for x in link:
        # print(x)
        r = requests.get(x, headers=headers) 
        # print(r)
        soup = BeautifulSoup(r.content, 'lxml')
        
    return soup





