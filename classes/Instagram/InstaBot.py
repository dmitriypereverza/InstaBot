#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import itertools
import json
import logging
import random
import sys

from classes.Connection.instaConnector import InstaConnect
from classes.Connection.request import RequestFacade
from classes.Instagram import Endpoints
from classes.Instagram.userinfo import User

if 'threading' in sys.modules:
    del sys.modules['threading']
from classes.Log.LogClass import Logger

class InstaBot:
    ownerAccount = None

    def __init__(self, login, password):
        self.botStart = datetime.datetime.now()
        self.userLogin = login.lower()
        self.userPassword = password
        self.instaConnector = InstaConnect()
        self.requestManager = RequestFacade()


    def login(self):
        self.instaConnector.login(self.userLogin, self.userPassword)
        if self.instaConnector.isConnected():
            self.ownerAccount = User.getUserByName(self.userLogin)

    def logout(self):
        self.instaConnector.logout()

    def getMediaByTag(self, tag):
        """ Get media ID set, by your hashtag """

        if self.instaConnector.isConnected():
            Logger.log("Get media id by tag: %s" % tag)
            try:
                all_data = self.requestManager.getJson(Endpoints.url_tag % tag)
                return list(all_data['tag']['media']['nodes'])
            except:
                Logger.error("Except on get_media!")
                return None
        else:
            self.write_log("Not connect!")

    def getUserFollowersByUserId(self, userId, limit):
        if self.login_status:
            url_followers = Endpoints.url_followers % (userId, limit)
            try:
                followers = self.s.post(url_followers)
                if followers.status_code == 200:
                    Logger.log("Get followers from : %s." % userId)
                    response = json.loads(followers.text)
                    return response['data']['user']['edge_followed_by']['edges']
            except:
                self.write_log("Except on get followers!")
        return False

    def getPostsByLocationId(self, locationId):
        if self.login_status:
            urlLocationSearch = Endpoints.url_location_search % locationId
            try:
                followers = self.s.post(urlLocationSearch)
                if followers.status_code == 200:
                    response = json.loads(followers.text)
                    Logger.log("Get posts from location: %s." % response['location']['name'])
                    return response['location']['media']['nodes']
            except:
                self.write_log("Except on get data from location!")
        return False

    def like(self, media_id):
        """ Send http request to like media by ID """
        if self.login_status:
            url_likes = Endpoints.url_likes % media_id
            try:
                like = self.s.post(url_likes)
            except:
                self.write_log("Except on like!")
                like = 0
            return like

    def unlike(self, media_id):
        """ Send http request to unlike media by ID """
        if self.login_status:
            url_unlike = Endpoints.url_unlike % (media_id)
            try:
                unlike = self.s.post(url_unlike)
            except:
                self.write_log("Except on unlike!")
                unlike = 0
            return unlike

    def comment(self, media_id, comment_text):
        """ Send http request to comment """
        if self.login_status:
            comment_post = {'comment_text': comment_text}
            url_comment = Endpoints.url_comment % (media_id)
            try:
                comment = self.s.post(url_comment, data=comment_post)
                if comment.status_code == 200:
                    self.comments_counter += 1
                    log_string = 'Write: "%s". #%i.' % (comment_text,
                                                        self.comments_counter)
                    self.write_log(log_string)
                return comment
            except:
                self.write_log("Except on comment!")
        return False

    def follow(self, user_id):
        """ Send http request to follow """
        if self.login_status:
            url_follow = Endpoints.url_follow % (user_id)
            try:
                follow = self.s.post(url_follow)
                if follow.status_code == 200:
                    Logger.log("Followed: %s." % user_id)
                return follow
            except:
                self.write_log("Except on follow!")
        return False

    def unfollow(self, user_id):
        """ Send http request to unfollow """
        if self.login_status:
            url_unfollow = Endpoints.url_unfollow % (user_id)
            try:
                unfollow = self.s.post(url_unfollow)
                if unfollow.status_code == 200:
                    self.unfollow_counter += 1
                    log_string = "Unfollow: %s #%i." % (user_id,
                                                        self.unfollow_counter)
                    self.write_log(log_string)
                return unfollow
            except:
                self.write_log("Exept on unfollow!")
        return False

    def write_log(self, log_text):
        """ Write log by print() or logger """
        Logger.log(log_text)
