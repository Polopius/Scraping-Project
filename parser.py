import requests
import time
from bs4 import BeautifulSoup

def remove_list_duplicates(list_):
    unique_list = []
    seen = set()
    for item in list_:
        t = tuple(sorted(item.items()))
        if t not in seen:
            seen.add(t)
            unique_list.append(item)
    return unique_list

def quotes_data_scraper(session, page_url, base_url, headers=None):
    quotes_data_list = []
    author_data_list = []
    count = 1
    while page_url:
        r = session.get(page_url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')    
        
        quotes = soup.find_all('div', class_='quote')
        for item in quotes:
            quote_text = item.find('span', class_='text').text.strip()
            author = item.find('small', class_='author').text.strip()
            tags = [tag.text.strip() for tag in item.find('div', class_='tags').find_all('a', class_='tag')]
            author_goodreads_link = item.find('a', href=True, string='(Goodreads page)')['href'].replace("http://", "https://", 1) # port 80 timeout
            quotes_data_list.append({
                'quotes': quote_text,
                'author': author,
                'tags': tags
            })
            author_data_list.append({
                'name': author,
                'link': author_goodreads_link
            })
            print(f'Saved quotes: {count}')
            count+=1
        
        next_page = soup.find('li', class_='next')
        if next_page:
            page_url = (base_url + next_page.find('a', href=True)['href'])
        else:
            print('Last page reached')
            page_url = None
    author_data_list = remove_list_duplicates(author_data_list)
    return quotes_data_list, author_data_list

def author_data_scraper(unique_author_data_list, headers=None):
    author_info_list = []
    for authors in unique_author_data_list:
        print(f'Currently saving {authors["name"]}\'s data')
        # print(f'Currently saving {authors['name']}\' data...')
        r = requests.get(authors['link'], headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        
        born_title = soup.find('div', class_='dataTitle', string='Born')
        born_data = ""
        if born_title:
            if born_title.next_sibling:
                text = getattr(born_title.next_sibling, "strip", lambda: "")()
                if text:
                    born_data = text
            
            born_date = born_title.find_next_sibling()

            if born_data and born_date.name == 'div' and 'dataItem' in born_date.get('class', []):
                born_data += ", " + born_date.text.strip()
            elif born_date.name == 'div' and 'dataItem' in born_date.get('class', []):
                born_data = born_date.text.strip()
            else:
                born_data = "No information"
                
        died_title = soup.find('div', class_='dataTitle', string='Died')    
        died_data = ""
        if died_title:
            died_data = died_title.find_next_sibling('div', class_='dataItem', itemprop='deathDate').text.strip()
        else:
            died_data = "Still alive"
        
        genre_title = soup.find('div', class_='dataTitle', text='Genre')
        genre_data = []
        if genre_title: 
            genre_data = [genre.text.strip() for genre in genre_title.find_next_sibling('div', class_='dataItem').find_all('a') ]
        else:
            genre_data = None
        
        influences_title = soup.find('div', class_='dataTitle', string='Influences')
        influences_data = []
        if influences_title:
            influences_data = [influence.text.strip() for influence in influences_title.find_next_sibling('div', class_='dataItem').select_one('span[style*="display:none"]').find_all('a')]
        else:
            influences_data = None
        
        author_info_list.append({
            'name': authors['name'],
            'Born': born_data,
            'Died': died_data,
            'Genres': genre_data,
            'Influences': influences_data
        })
        time.sleep(2)

    return author_info_list