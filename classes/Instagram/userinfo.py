#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from classes.Sourse.unwanted import unwanted_username_list

class User:
    POPULAR_FOLLOWS_COUNT = 500
    FAKE_COEFICIENT = 3
    NORMAL_COEFICIENT = 2
    FAKE_FOLLOWED_LIMIT = 150
    BEGINNER_FOLLOWS_COUNT = 50

    def __init__(self, userInfo):
        self.id = userInfo['id']
        self.username = userInfo['username']
        self.followsCount = userInfo['follows']['count']
        self.followed_by = userInfo['followed_by']['count']
        self.fullName = userInfo['full_name']
        self.media = userInfo['media']['nodes']
        self.biography = userInfo['biography']
        self.isFollower = userInfo['follows_viewer'] or userInfo['has_requested_viewer']
        self.isFollowing = userInfo['followed_by_viewer'] or userInfo['requested_by_viewer']

    def isPopular(self):
        return self.followsCount > self.POPULAR_FOLLOWS_COUNT

    def isFake(self):
        return self.followed_by >= self.FAKE_FOLLOWED_LIMIT and \
               self.followsCount > 0 and \
               self.followsCount / self.followed_by > self.FAKE_COEFICIENT

    def isNormal(self):
        return not self.inBlackList() and \
               not self.isFake() and \
               self.followed_by > 0 and \
               self.followed_by / self.followsCount <= self.NORMAL_COEFICIENT

    def isBeginner(self):
        return self.followsCount < self.BEGINNER_FOLLOWS_COUNT

    def inBlackList(self):
        for x in unwanted_username_list:
            if re.search(x, self.username):
                return True



