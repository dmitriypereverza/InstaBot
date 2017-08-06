#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint
import re

class MsgGenerator:
    def __init__(self):
        self.list = []

    def generate(self):
        strResult = "{Привет|Здравствуй|Салют|Добрый день|Хай}, {tenderbuddyname}), не {посчитай|сочти} за спам, и можно тебя попросить?) Мы с {друзьями|знакомыми|коллегами} {постим|выкладываем|находим} {топовую|крутую|хайповую} одежду с ALiexpress и если у тебя есть {минутка|свободное время|время}, можешь {посмотреть|оценить|заглянуть в} группу. У меня на странице первая запись. Надеюсь тебе {придется по душе|понравиться}) заранее спасибо) и извини если что то не так("

        strResult = re.sub('\|', '~~', strResult)
        matches = re.findall(r"{.*?}", strResult)
        for i in range(len(matches)):
            groupedMatches = re.findall(r"([^\~\~\{\}]+)", matches[i])
            strResult = re.sub(R'{}'.format(matches[i]), groupedMatches[randint(0, len(groupedMatches) - 1)], strResult)

        return strResult