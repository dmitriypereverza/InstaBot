#!/usr/bin/python3
# -*- coding: utf-8 -*-

import vk_api

def bestWall(vk, popul, query):
    count = 1000
    q = popul + " " + query
    values = {'q': q, 'count': count}
    response = vk.method('newsfeed.search', values)

    a = "репосты" + "\n" + q + "\n"
    b = "комменты" + "\n" + q + "\n"
    nayd = 0
    for i in range(len(response['items'])):
        likes = response['items'][i]['likes']['count'] + 1
        reposts = response['items'][i]['reposts']['count']
        comments = response['items'][i]['comments']['count']
        owner_id = response['items'][i]['owner_id']
        id = response['items'][i]['id']

        percent = 100 * reposts / likes
        if percent > 45:
            link = "http://VK.com/wall" + str(owner_id) + "_" + str(id)
            a = a + link + ", " + str(percent) + "%\n"
            nayd = 1 + nayd

        percentComment = 100 * comments / likes
        if (percent > 20) & (comments > 100):
            link = "http://VK.com/wall" + str(owner_id) + "_" + str(id)
            b = b + link + ", " + str(percent) + "%\n"
            nayd = 1 + nayd
    return a + "\n" + b


def bestWallAll(query, vk):
    popul = "likes:10"
    a = bestWall(vk, popul, query)
    popul = "likes:100"
    b = bestWall(vk, popul, query)
    popul = "likes:1000"
    c = bestWall(vk, popul, query)
    all = a + "\n" + b + "\n" + c + "\n"
    return all


login = '89094346969'  # Логин от ВК
password = '741dmitriy963'  # Пароль от ВК
token = '7e9aa79788282d414bbbf24d96af3bba43a31f8b4101f0e266e4a3d90b69a16322ca17566b0a4745a8026'

try:
    vk = vk_api.VkApi(login, password, token = token)  # Авторизируемся
except vk_api.authorization_error as error_msg:
    print(error_msg)  # В случае ошибки выведем сообщение

query = "Кулон"

messaga = bestWallAll(query, vk)
values = {'user_id': 41244707, 'message': messaga}
# response = VK.method('messages.send', values)

print(messaga)