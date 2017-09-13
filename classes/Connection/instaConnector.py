#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.Connection.requestHandlerMixin import RequestHandlerMixin
from classes.Exeptions.exeptions import TypeErrorExeption
from classes.Instagram import Endpoints
from classes.Log.LogClass import Logger

class InstaConnect:
    csrfToken = None
    loginSuccess = False

    def __init__(self, requestManager):
        if not isinstance(requestManager, RequestHandlerMixin):
            raise TypeErrorExeption('{} not is instance RequestHandlerMixin'.format(requestManager.__class__.__name__))
        self.requestManager = requestManager

    def login(self, login, password):
        context = self.requestManager.get(Endpoints.url)
        self.requestManager.headersUpdate({'X-CSRFToken': context.cookies['csrftoken']})

        loginConnect = self.requestManager.post(
            Endpoints.urlLogin,
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
                Logger.sucess("Login like {} success!".format(login))

        else:
            Logger.error("Incorrect login or password!")

    def logout(self):
        try:
            logoutPost = {'csrfmiddlewaretoken': self.csrfToken}
            self.requestManager.post(Endpoints.urlLogout, data = logoutPost)
            self.loginSuccess = False
        except Exception as e:
            Logger.error("Logout error! " + e)

    def isConnected(self):
        return self.loginSuccess