#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
from itertools import cycle

from classes.Tasks.BaseTask import BaseTask

class FollowAndUnfollow(BaseTask):
    def __init__(self, insta):
        super().__init__(insta)
        self.userGenerator = None

    def runTask(self):
        currentUser = self.getNextUser()
        """:type currentUser: User"""
        if currentUser.isFollowing:
            self._insta.unfollow(currentUser.id)
            time.sleep(5)
            self._insta.follow(currentUser.id)
        else:
            self._insta.follow(currentUser.id)

        self.setNextExec()

    def getNextUser(self):
        self.userGenerator = cycle(self._usersList) if not self.userGenerator else self.userGenerator
        return next(self.userGenerator)