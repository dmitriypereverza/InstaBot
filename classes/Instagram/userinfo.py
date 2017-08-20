#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests


class User:
    user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
    url_user_info = "https://www.instagram.com/%s/?__a=1"

    def __init__(self, userLogin):
        self.s = requests.Session()
        self.s.headers.update({'User-Agent': self.user_agent})

        userInfo = self.get_user_info_by_login(userLogin)
        self.id = userInfo['id']
        self.username = userInfo['username']
        self.followsCount = userInfo['follows']['count']
        self.followed_by = userInfo['followed_by']['count']
        self.fullName = userInfo['full_name']
        self.mediaCount = len(userInfo['media'])
        self.biography = userInfo['biography']

    def get_user_info_by_login(self, user_name):
        url_info = self.url_user_info % user_name
        info = self.s.get(url_info)
        return json.loads(info.text)['user']