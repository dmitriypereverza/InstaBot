#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
from classes.Instagram.instaUser import User
from classes.Tasks.BaseTask import BaseTask

class FollowAndUnfollow(BaseTask):
    def runTask(self, user: User):
        if user.isFollowing:
            self._insta.unfollow(user.id)
            time.sleep(5)
            self._insta.follow(user.id)
        else:
            self._insta.follow(user.id)
        self.setNextExec()