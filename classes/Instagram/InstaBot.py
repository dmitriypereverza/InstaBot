#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import functools
from classes.Connection.instaConnector import InstaConnect
from classes.Connection.request import RequestFacade
from classes.Instagram import Endpoints, InstaQuery
from classes.Instagram.instaUser import User
from classes.Log.LogClass import Logger

def checkConnectAndLogged(func):
    @functools.wraps(func)
    def inner(self, *args, **kwargs):
        if self.instaConnector.isConnected():
            Logger.log("Exect {}() with params: {} {}.".format(func.__name__, args, kwargs))
            try:
                result = func(self, *args, **kwargs)
                return result
            except:
                Logger.error("Except on get data from {}!".format(func.__name__))
        else:
            Logger.error("Not connect!")
    return inner

class InstaBot:
    ownerAccount = None

    def __init__(self, login, password):
        self.botStart = datetime.datetime.now()
        self.userLogin = login.lower()
        self.userPassword = password
        self.requestManager = RequestFacade()
        self.instaConnector = InstaConnect(self.requestManager)

    def login(self):
        self.instaConnector.login(self.userLogin, self.userPassword)
        if self.instaConnector.isConnected():
            self.ownerAccount = User(self.getUserInfoByLogin(self.userLogin))

    def logout(self):
        self.instaConnector.logout()

    @checkConnectAndLogged
    def getPostsByLocationId(self, locationId):
        urlLocationSearch = Endpoints.urlLocationSearch % locationId
        response = self.requestManager.getJson(urlLocationSearch)
        return response['location']['media']['nodes']

    @checkConnectAndLogged
    def like(self, media_id):
        urlLikes = Endpoints.urlLikes % media_id
        return self.requestManager.post(urlLikes)

    @checkConnectAndLogged
    def unlike(self, media_id):
        urlUnlike = Endpoints.urlUnlike % media_id
        return self.requestManager.post(urlUnlike)

    @checkConnectAndLogged
    def comment(self, media_id, comment_text):
        urlComment = Endpoints.urlComment % media_id
        return self.requestManager.post(
            urlComment,
            data = {'comment_text': comment_text}
        )

    @checkConnectAndLogged
    def follow(self, user_id):
        urlFollow = Endpoints.urlFollow % user_id
        return self.requestManager.post(urlFollow)

    @checkConnectAndLogged
    def unfollow(self, userId):
        urlUnfollow = Endpoints.urlUnfollow % userId
        return self.requestManager.post(urlUnfollow)

    @checkConnectAndLogged
    def getMediaByTag(self, tag):
        all_data = self.requestManager.getJson(Endpoints.urlTag % tag)
        return all_data['tag']['media']['nodes']

    @checkConnectAndLogged
    def getUserFollowersByUserId(self, userId, limit):
        urlFollowers = Endpoints.urlFollowers % (userId, limit)
        response = self.requestManager.getJson(urlFollowers)
        return response['data']['user']['edge_followed_by']['edges']

    def getUserInfoByLogin(self, userName):
        return self.requestManager.getJson(Endpoints.urlUserInfo % userName)['user']

    def getUsersByTags(self, tags):
        userList = []
        for tag in tags:
            userList += self.getUserNamesByTag(tag)
        return userList

    def getUserNamesByTag(self, tag):
        userNames = []
        for media in self.getMediaByTag(tag):
            mediaInfo = InstaQuery.getMediaInfoByCode(media['code'])
            userName = mediaInfo['shortcode_media']['owner']['username']
            if userName not in userNames:
                userNames.append(userName)
        return userNames

    def getUserFollowers(self, username, limit):
        user = User(self.getUserInfoByLogin(username)),
        userNames = []
        for follower in self.getUserFollowersByUserId(user.id, limit):
            userName = follower['node']['username']
            if userName not in userNames:
                userNames.append(userName)
        return userNames

    def getUsersByLocation(self, locationId):
        posts = self.getPostsByLocationId(locationId)
        userNames = []
        for post in posts:
            mediaInfo = InstaQuery.getMediaInfoByCode(post['code'])
            userName = mediaInfo['shortcode_media']['owner']['username']
            if userName not in userNames:
                userNames.append(userName)
        return userNames