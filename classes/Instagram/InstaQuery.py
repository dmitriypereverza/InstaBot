#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.Connection.request import RequestFacade
from classes.Instagram import Endpoints
from classes.Log.LogClass import Logger

def getMediaInfoByCode(mediaCode):
    urlFollow = Endpoints.urlMediaDetail % mediaCode
    try:
        return RequestFacade().getJson(urlFollow)['graphql']
    except:
        Logger.log("Error in getMediaInfoByCode()!")