#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime

from classes.Connection.request import RequestFacade
from classes.Instagram import Endpoints


class InstaConnect:
    csrfToken = None
    loginSuccess = False

    def __init__(self):
        self.requestManager = RequestFacade()

    def login(self, login, password):
        # TODO log event
        context = self.requestManager.get(Endpoints.url)
        self.requestManager.headersUpdate({'X-CSRFToken': context.cookies['csrftoken']})

        loginConnect = self.requestManager.post(
            Endpoints.url_login,
            data = {
                'username': login,
                'password': password
            },
            allow_redirects = True
        )
        self.requestManager.headersUpdate({'X-CSRFToken': loginConnect.cookies['csrftoken']})
        self.csrfToken = loginConnect.cookies['csrftoken']
        if loginConnect.status_code == 200:
            r = self.requestManager.get(Endpoints.url)
            finder = r.text.find(login)
            if finder != -1:
                self.loginSuccess = True
        else:
            print('Login error! Connection error!')

    def logout(self):
        try:
            logoutPost = {'csrfmiddlewaretoken': self.csrfToken}
            self.requestManager.post(Endpoints.url_logout, data = logoutPost)
            self.loginSuccess = False
        except:
            print("Logout error!")

    def isConnected(self):
        return self.loginSuccess