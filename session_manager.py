import requests

base_url = 'https://quotes.toscrape.com/page/1'
login_url = 'https://quotes.toscrape.com/login'

'''# Context manager: allows us to stay connected and logged in
with requests.session() as s:
    s.post(login_url, data=payload)
    r = s.get(base_url)
    soup = BeautifulSoup(r.content, 'lxml')
    # print(soup.prettify())'''

def get_logged_in_session(username, password):
    
    payload = {
        'username' : username,
        'password' : password
    }
    
    session = requests.Session()
    
    r = session.post(login_url, data=payload)
    
    # Check for login error (optional)
    '''
    if 'Invalid username or password' in response.text:
        print('Login Failed..')
        return None
    '''
    
    print("Login Successful")
    return session