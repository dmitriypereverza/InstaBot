#!/usr/bin/python3
# -*- coding: utf-8 -*-
from itertools import cycle
from  classes.Instagram.InstaBot import InstaBot
from classes.Exeptions.exeptions import NotOverrideMethodExeption
from classes.Instagram.instaUser import User

FILE_TYPE = 'file'
LIST_TYPE = 'list'

class BaseUserSource:
    def __init__(self, source=None, type=FILE_TYPE):
        self._listFromFile = []
        self._insta = None
        self._isCycle = False
        if type == FILE_TYPE:
            self._listFromFile = self._getListFromFile(source)
        elif type == LIST_TYPE:
            self._listFromFile = source

    def getCount(self):
        raise NotOverrideMethodExeption('Do not overided method: getCount()')

    def getNext(self):
        raise NotOverrideMethodExeption('Do not overided method: getNext()')

    def setInstaConnect(self, instaConnect: InstaBot):
        self._insta = instaConnect

    def isCycle(self, *args):
        if not len(args) != 0:
            return self._isCycle
        self._isCycle = args[0]

    def _getListFromFile(self, filePath):
        with open(filePath, 'r') as f:
            output = f.readlines()
        return [x.strip() for x in output]

class UserList(BaseUserSource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.userListGenerator = None

    def getNext(self):
        userName = self._getNextUserName()
        if userName:
            return User(self._insta.getUserInfoByLogin(userName))

    def _getNextUserName(self):
        if not self.userListGenerator:
            if self.isCycle():
                self.userListGenerator = cycle(self._listFromFile)
            else:
                self.userListGenerator = (x for x in self._listFromFile)

        return next(self.userListGenerator)

class HashTagUserSource(BaseUserSource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tagsGenerator = None
        self._userList = []

    def getNext(self):
        user = self.getNextUser()
        if not user:
            self._userList = (x for x in self.getUsersByTag(self.getNextTag()))
            user = self.getNextUser()

        return user

    def getNextUser(self):
        try:
            return next(self._userList)
        except:
            return None

    def getNextTag(self):
        if not self.tagsGenerator:
            if self.isCycle():
                self.tagsGenerator = cycle(self._listFromFile)
            else:
                self.tagsGenerator = (x for x in self._listFromFile)

        return next(self.tagsGenerator)

    def getUsersByTag(self, tag):
        return list(map(
            lambda x: User(self._insta.getUserInfoByLogin(x)),
            self._insta.getUserNamesByTag(tag)
        ))

class GeoUserSource(BaseUserSource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geoGenerator = None
        self._userList = []

    def getNext(self):
        location = next(self._userList)
        if not location:
            self._userList = [x for x in self.getUsersByLocation(self.getNextLocation())]

        return location

    def getNextLocation(self):
        if not self.geoGenerator:
            if self.isCycle():
                self.geoGenerator = cycle(self._listFromFile)
            else:
                self.geoGenerator = (x for x in self._listFromFile)

        return next(self.geoGenerator)

    def getUsersByLocation(self, locationId):
        return list(map(
            lambda x: User(self._insta.getUserInfoByLogin(x)),
            self._insta.getUsersByLocation(locationId)
        ))

class FollowersUserSource(BaseUserSource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.userFollowersGenerator = None
        self._userList = []

    def getNext(self):
        follower = next(self._userList)
        if not follower:
            self._userList = [x for x in self.getUsersFollowers(self.getNextUserWithFollowers())]

        return follower

    def getNextUserWithFollowers(self):
        if not self.userFollowersGenerator:
            if self.isCycle():
                self.userFollowersGenerator = cycle(self._listFromFile)
            else:
                self.userFollowersGenerator = (x for x in self._listFromFile)

        return next(self.userFollowersGenerator)

    def getUsersFollowers(self, username):
        return list(map(
            lambda x: User(self._insta.getUserInfoByLogin(x)),
            self._insta.getUserFollowers(username, 50)
        ))

class FollowedByUserSource(BaseUserSource):
    pass