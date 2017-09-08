#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.Connection.request import RequestFacade
from classes.Instagram import Endpoints
from classes.Log.LogClass import Logger

def getMediaInfoByCode(mediaCode):
    urlFollow = Endpoints.url_media_detail % mediaCode
    try:
        return RequestFacade().getJson(urlFollow)['graphql']
    except:
        Logger.log("Error in getMediaInfoByCode()!")

def getUserInfoByLogin(userName):
    return RequestFacade().getJson(Endpoints.url_user_info % userName)['user']