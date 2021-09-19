import requests
import time
from bs4 import BeautifulSoup

headers = {
    'accept-encoding':
    'gzip, deflate, br',
    'accept-language':
    'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control':
    'no-cache',
    'pragma':
    'no-cache',
    'sec-ch-ua':
    '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-platform':
    '"Windows"',
    'user-agent':
    'Mozzilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
config = {'EMAIL': '', 'PASSWORD': ''}


def login(headers, config):
    global session
    session = requests.session()
    session.headers.update(headers)
    response = session.post(
        'https://web.spaggiari.eu/auth-p7/app/default/AuthApi4.php?a=aLoginPwd',
        headers={
            'accept': '*/*',
            'content-length': '56',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://web.spaggiari.eu',
            'referer': 'https://web.spaggiari.eu/home/app/default/login.php',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest'
        },
        data={
            'cid': '',
            'uid': config['EMAIL'],
            'pwd': config['PASSWORD'],
            'pin': '',
            'target': ''
        })
    soup = BeautifulSoup(response.text, 'lxml')
    text = soup.getText()
    index = text.find('"account_string":"')
    time.sleep(0.5)
    session.post(
        'https://web.spaggiari.eu/auth-p7/app/default/AuthApi4.php?a=aLoginSam',
        headers={
            'accept': '*/*',
            'content-length': '13',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://web.spaggiari.eu',
            'referer': 'https://web.spaggiari.eu/home/app/default/login.php',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest'
        },
        data={'uid': text[index + 18:index + 27]})
    time.sleep(0.5)
    result = session.post(
        'https://web.spaggiari.eu/home/app/default/login_ok_redirect.php',
        headers={
            'accept':
            'text/html,appplication/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'content-length': '60',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://web.spaggiari.eu',
            'referer': 'https://web.spaggiari.eu/home/app/default/login.php',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'x-requested-with': 'XMLHttpRequest'
        },
        data={
            'custcode': '',
            'login': config['EMAIL'],
            'password': config['PASSWORD'],
            'pin': ''
        },
        cookies={'weblogin': config['EMAIL']})
    return result


def getVotes(order, quantity):
    session.get()


################
##VOTES MODULE##
################
"""
session.get(
    'https://web.spaggiari.eu/cvv/app/default/genitori_note.php?ordine=materia&filtro=tutto',
    headers={
        'accept':
        'text/html,appplication/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'referer':
        'https://web.spaggiari.eu/cvv/app/default/genitori_note.php',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1'
    })
"""

response = login(headers, config)

log = [
    'RESPONSE:\n\n',
    str(response), '\n\nHEADERS:\n\n',
    str(response.headers), '\n\nURL:\n\n',
    str(response.url), '\n\nRAW:\n\n',
    str(response.raw), '\n\nTEXT:\n\n',
    str(response.text)
]

f = open('/Users//Documents/SpaggiariReaper/output.txt', 'a')
f.writelines(log)
