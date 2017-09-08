#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from classes.Connection.instaConnector import InstaConnect
from classes.Connection.request import RequestFacade
from classes.Instagram import Endpoints, InstaQuery
from classes.Instagram.userinfo import User
from classes.Log.LogClass import Logger

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
            self.ownerAccount = User.getUserByName(self.userLogin)

    def logout(self):
        self.instaConnector.logout()

    def getPostsByLocationId(self, locationId):
        if self.instaConnector.isConnected():
            urlLocationSearch = Endpoints.url_location_search % locationId
            Logger.log("Get posts from locationId: %s." % locationId)
            try:
                response = self.requestManager.getJson(urlLocationSearch)
                return response['location']['media']['nodes']
            except:
                Logger.error("Except on get data from location!")
        Logger.error("Not connect!")

    def like(self, media_id):
        if self.instaConnector.isConnected():
            urlLikes = Endpoints.url_likes % media_id
            try:
                return self.requestManager.post(urlLikes)
            except:
                Logger.error("Except on like!")
        Logger.error("Not connect!")

    def unlike(self, media_id):
        if self.instaConnector.isConnected():
            urlUnlike = Endpoints.url_unlike % media_id
            try:
                response = self.requestManager.post(urlUnlike)
            except:
                Logger.error("Except on unlike!")
        Logger.error("Not connect!")

    def comment(self, media_id, comment_text):
        if self.instaConnector.isConnected():
            urlComment = Endpoints.url_comment % media_id
            try:
                return self.requestManager.post(
                    urlComment,
                    data = {'comment_text': comment_text}
                )
            except:
                Logger.error("Except on comment!")
        Logger.error("Not connect!")

    def follow(self, user_id):
        if self.instaConnector.isConnected():
            urlFollow = Endpoints.url_follow % user_id
            try:
                return self.requestManager.post(urlFollow)
            except:
                Logger.error("Except on follow!")
        Logger.error("Not connect!")

    def unfollow(self, userId):
        if self.instaConnector.isConnected():
            urlUnfollow = Endpoints.url_unfollow % userId
            try:
                return self.requestManager.post(urlUnfollow)
            except:
                Logger.error("Exept on unfollow!")
        Logger.error("Not connect!")

    def getMediaByTag(self, tag):
        if self.instaConnector.isConnected():
            Logger.log("Get media by tag: %s" % tag)
            try:
                all_data = self.requestManager.getJson(Endpoints.url_tag % tag)
                return all_data['tag']['media']['nodes']
            except:
                Logger.error("Except on get_media!")
                return None
        else:
            Logger.error("Not connect!")

    def getUserFollowersByUserId(self, userId, limit):
        if self.instaConnector.isConnected():
            urlFollowers = Endpoints.url_followers % (userId, limit)
            Logger.log("Get followers from : %s." % userId)
            try:
                response = self.requestManager.getJson(urlFollowers)
                return response['data']['user']['edge_followed_by']['edges']
            except:
                Logger.error("Except on get followers!")
        Logger.error("Not connect!")

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
        user = User.getUserByName(username)
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

