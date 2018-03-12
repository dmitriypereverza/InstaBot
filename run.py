#!/usr/bin/python3
# -*- coding: utf-8 -*-
import config
from classes.Bot.Scheduler import Scheduler
from classes.Instagram.InstaBot import InstaBot
from classes.Source.commentTemplateList import templateListEn
from classes.Tasks.FollowAndUnfollow import FollowAndUnfollow
from classes.Tasks.TraditionalFollowing import TraditionalFollowing
from classes.TextGenerator.MsgGenerator import MsgGenerator
from classes.UserSource.UserSourceBuilder import UserSourceBuilder
from classes.UserSource import UserSources
from classes.UserSource import UserSourceContainer

if __name__ == "__main__":
    instaBot = InstaBot(login=config.login, password=config.password)
    instaBot.login()
    scheduler = Scheduler()

    scheduler.addTask(
        FollowAndUnfollow(instaBot)
            .setDelay(80, 100)
            .setUserSource(
                UserSourceBuilder() \
                    .setType(UserSourceContainer.USER_LIST) \
                    .setSource(['urgantcom'], UserSources.LIST_TYPE) \
                    .setIsCycle(True)
                    .get()
        ).setLikeSettings({
                'needLike': True,
                'count': 2,
                'range': 6,
                'firstLike': True,
            })
            .needFollow(True)
            .needComment(True)
            .setCommentGenerator(MsgGenerator(templateListEn, type=MsgGenerator.TYPE_LIST))
    ).enableTaskLoop().start()