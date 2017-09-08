#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.Instagram.InstaBot import InstaBot

class UserSearcher:
    """:type instaConnect: InstaBot"""
    instaConnect = None

    def __init__(self, instaConnect):
        if (instaConnect.login_status):
            self.instaConnect = instaConnect

    def getUsersByTags(self, tags):
        userList = []
        for tag in tags:
            userList += self.getUserNamesByTag(tag)
        return userList

    def getUserNamesByTag(self, tag):
        userNames = []
        for media in self.instaConnect.getMediaByTag(tag):
            mediaInfo = self.instaConnect.getMediaInfoByCode(media['code'])
            userName = mediaInfo['shortcode_media']['owner']['username']
            if userName not in userNames:
                userNames.append(userName)
        return userNames

    def getUserFollowers(self, username, limit):
        user = self.instaConnect.getUserByName(username)
        userNames = []
        for follower in self.instaConnect.getUserFollowersByUserId(user.id, limit):
            userName = follower['node']['username']
            if userName not in userNames:
                userNames.append(userName)
        return userNames

    def getUsersByLocation(self, locationId):
        posts = self.instaConnect.getPostsByLocationId(locationId)
        userNames = []
        for post in posts:
            mediaInfo = self.instaConnect.getMediaInfoByCode(post['code'])
            userName = mediaInfo['shortcode_media']['owner']['username']
            if userName not in userNames:
                userNames.append(userName)
        return userNames

