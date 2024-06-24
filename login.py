import requests
from bs4 import BeautifulSoup
import re
import json
import pprint

def main():

    base_url = ('https://www.fhlbtradedesk.com')
    login_url = ('https://www.fhlbtradedesk.com/my.policy')

    payload = {
        'username': 'JChing1',
        'password': 'MatthewCovington1',
        'vhost': 'standard'
    }

    with requests.session() as session:

        # Initial connect and sends login payload
        r = session.get(base_url)
        print("Cookies before login:", session.cookies.get_dict(), '\n')

        logon = session.post(login_url, data=payload)
        print("Cookies after login:", logon.cookies.get_dict(),  '\n')

        soup = BeautifulSoup(logon.content, 'html.parser')
        print(soup.prettify())

        print('\n', logon.status_code)

        # TODO Need to navigate to the order page for the specific bonds
        
        # TODO Wait until the time comes then spam the orders like crazy



# Login??  
#https://www.fhlbtradedesk.com/my.policy

# The right one:
# Idk 

#cookies = parseCookieFile('PATH_TO_YOUR_COOKIE_FILE.TXT')
#cookie_json = json.dumps(cookies)

# Probably important stuff regarding the proxy
#proxy_url = "http://{0}:{1}@proxy.blah.blah.com:[portnumber]".format('proxy_uid', 'proxy_password')
#session.proxies = {'http': proxy_url, 'https': proxy_url}

if __name__ == '__main__':
    main()