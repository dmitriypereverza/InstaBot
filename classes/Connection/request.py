#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import inject
import requests
import DIConfig
from classes.Connection.requestHandlerMixin import RequestHandlerMixin

class RequestFacade(RequestHandlerMixin):
    user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
    accept_language = 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
    logger = inject.attr(DIConfig.Logger)

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

    def get(self, *args, **kwargs):
        response = self.session.get(*args, **kwargs)
        if response.status_code != 200:
            self.logger.error('Can\'t do get request. Status code: {}\nError text: {}'.format(response.status_code, json.loads(response.text)['message']))
        return response

    def headersUpdate(self, *args, **kwargs):
        self.session.headers.update(*args, **kwargs)

    def post(self, *args, **kwargs):
        response = self.session.post(*args, **kwargs)
        if response.status_code != 200:
            self.logger.error('Can\'t do post request. Status code: {}\nError text: {}'.format(response.status_code, json.loads(response.text)['message']))
        return response

    def getJson(self, url):
        response = self.get(url)
        if response.status_code != 200:
            self.logger.error('Can\'t get json. Status code: ' + response.status_code)
        return json.loads(response.text)



