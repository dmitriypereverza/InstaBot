#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
from itertools import cycle

from classes.Tasks.BaseTask import BaseTask

class FollowAndUnfollow(BaseTask):
    def __init__(self, insta):
        super().__init__(insta)
        self.delay = [35, 55]
        self.userGenerator = None

    def runTask(self):
        currentUser = self.getNextUser()
        """:type currentUser: User"""
        if currentUser.isFollowing:
            self.insta.unfollow(currentUser.id)
            time.sleep(5)
            self.insta.follow(currentUser.id)
        else:
            self.insta.follow(currentUser.id)

        self.setNextExec()

    def getNextUser(self):
        self.userGenerator = cycle(self.usersList) if not self.userGenerator else self.userGenerator
        return next(self.userGenerator)