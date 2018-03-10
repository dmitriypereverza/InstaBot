#!/usr/bin/python3
# -*- coding: utf-8 -*-
import inject

import DIConfig
from classes.Connection.requestHandlerMixin import RequestHandlerMixin
from classes.Exeptions.exeptions import TypeErrorExeption
from classes.Instagram import Endpoints

class InstaConnect:
    csrfToken = None
    loginSuccess = False
    """:type logger LoggerMixin """
    logger = inject.attr(DIConfig.Logger)

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
                self.logger.success("Login like {} success!".format(login))

        else:
            self.logger.error("Incorrect login or password!")

    def logout(self):
        try:
            logoutPost = {'csrfmiddlewaretoken': self.csrfToken}
            self.requestManager.post(Endpoints.urlLogout, data = logoutPost)
            self.loginSuccess = False
        except Exception as e:
            self.logger.error("Logout error! " + e)

    def isConnected(self):
        return self.loginSuccess