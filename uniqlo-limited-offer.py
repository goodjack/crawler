import requests
from bs4 import BeautifulSoup


def get_web_page(url):
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_items(dom):
    soup = BeautifulSoup(dom, 'html.parser')

    # items = [] # 特價商品
    units = soup.find_all('div', 'unit')
    for unit in units:
        name = unit.find('dt', 'name').find('a').getText().strip()
        price = unit.find('dd', 'price').getText().strip()
        print(name, price)


limited_offer_men = get_web_page(
    'http://www.uniqlo.com/tw/store/list/limited-offer/men/')
if limited_offer_men:
    get_items(limited_offer_men)

limited_offer_women = get_web_page(
    'http://www.uniqlo.com/tw/store/list/limited-offer/women/')
if limited_offer_women:
    get_items(limited_offer_women)