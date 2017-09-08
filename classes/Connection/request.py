#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json

import requests

class RequestFacade:
    user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
    accept_language = 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'

    def __init__(self):
        self.session = requests.Session()
        self.session.cookies.update({
            'sessionid':  '',
             'mid': '',
            'ig_pr': '1',
            'ig_vw': '1920',
            'csrftoken': '',
            's_network': '',
             'ds_user_id': ''
        })
        self.session.headers.update({
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': self.accept_language,
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'www.instagram.com',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'User-Agent': self.user_agent,
            'X-Instagram-AJAX': '1',
            'X-Requested-With': 'XMLHttpRequest'
        })

    def get(self, url):
        return self.session.get(url)

    def headersUpdate(self, param):
        self.session.headers.update(param)

    def post(self, url_login, data = None, allow_redirects = None):
        return self.session.post(url_login, data, allow_redirects)

    def getJson(self, url):
        return json.loads(self.get(url).text)


