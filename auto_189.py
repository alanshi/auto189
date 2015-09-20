# coding: utf-8

import requests
import json

login_url = 'http://118.121.16.74:8080/api/lls/newRegisteredLogin/'
get_coin_url = 'http://118.121.16.74:8080/api/lls/shake/'
login_data = {'accNbr': '18086808650',
   'password': '1357525',
   'osVersion': '7.1.1',
   'deviceModel': 'IPHONE_MOBILE',
   'appVersion': '2.1.3',
   'mobileVersion': '7.1.1',
   'channelCode': '200256'}


def login():
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

token = login().get('token')

print get_coin(token)
