# coding: utf-8

import requests
import json
from settings import account_list, common_data

login_url = 'http://118.121.16.74:8080/api/lls/newRegisteredLogin/'
get_coin_url = 'http://118.121.16.74:8080/api/lls/shake/'


def login(login_data):
    r = requests.post(
        url=login_url,
        data=login_data
    )
    rep = json.loads(r.content)
    return rep


def get_coin(token):
    get_url = '%s/%s' % (get_coin_url, token)
    r = requests.get(
        url=get_url
    )
    rep = r.content
    return rep

for account in account_list:
    login_data = common_data
    login_data.update(account)
    token = login(login_data).get('token')
    print get_coin(token)
