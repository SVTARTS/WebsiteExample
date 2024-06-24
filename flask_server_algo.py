import requests
from bs4 import BeautifulSoup
import re
import json
import pprint

def main():

    base_url = ('http://127.0.0.1:5000/')
    login_url = ('http://127.0.0.1:5000/login')
    submit_order_url = ('http://127.0.0.1:5000/order')

    payload = {
        'username': 'jching1',
        'password': 'password1',
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

        """
        order_payload = {'product': '1', 
        'quantity': 'my_quantity',
        'structure_type': 'my_struct_type',
        'structure_description' : 'my_desc',
        'call_freq': 'my_call',
        'spread': 'duh_spread',
        'settlement_date' : 'my_settlement_date',
        'maturity_date': '1',
        'order_amount': '1',
        'investor':'1',      
        }

        """

        order_payload = {'product': 'product',
        'quantity':'quantity',
        'Structure Type':'structure',
        'Structure Description' : 'my_desc',
        'Call Freq': 'my_call',
        'Spread (Bps)': 'duh_spread',
        'Settlement Date: ' : 'my_settlement_date',
        'Maturity Date: ': '1',
        'Order Amount (MM): ': '1',
        'Investor: ':'1',      
        
        }

        submit_order = session.post(submit_order_url, data=order_payload)
        #soup2 = BeautifulSoup(submit_order.content, 'html.parser')
        #print(soup2.prettify())

        # TODO Wait until the time comes then spam the orders like crazy



if __name__ == '__main__':
    main()


