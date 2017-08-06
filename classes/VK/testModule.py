#!/usr/bin/python3
# -*- coding: utf-8 -*-

import vk_api
import time
import re


def vko():
    login = '89094346969'  # Логин от ВК
    password = '741dmitriy963'  # Пароль от ВК
    token = '7e9aa79788282d414bbbf24d96af3bba43a31f8b4101f0e266e4a3d90b69a16322ca17566b0a4745a8026'
    try:
        vk = vk_api.VkApi(login, password, token=token)  # Авторизируемся
    except vk_api.authorization_error as error_msg:
        print(error_msg)  # В случае ошибки выведем сообщение
        return  # и выйдем

    relig='Православие' #кстати можно вводить, например, "Христианство", "Протестантизм" и др.
    goroda=(7159, 81) # через запятую можно перечислить все города и поселки по соседству
    for gorod in goroda:
        values1 = {'city': gorod,'religion':relig} #Получение списка участников группы
        response1 = vk.method('users.search', values1)
        kolvo=response1['count']
        print('количество православных жителей в городе:№'+str(gorod)+' равно='+str(kolvo)+' чел')
        if kolvo<1:
            print('этот город пропустим')
        elif kolvo<1000:
            telsea=0
            indx=0
            file = open(str(gorod)+relig+'.txt', 'w')
            time.sleep(5)
            values = {'fields': 'contacts','city': gorod,'religion':relig,'count':1000,'sort': 1}
            response = vk.method('users.search', values) #инфа об участниках. Разом
            print('_'*10+relig+'_'*10+'чел:'+str(kolvo)+'_'*10+'Город:'+str(gorod)+'_'*10)
            gran=response['count']
            if gran>1000:
                gran=1000
            for usdx in range(0,gran):
                indx=indx+1
                try:
                    mobile_phone = response['items'][usdx]['mobile_phone']
                    match1 = re.search("[\.\?\*]", mobile_phone) #Если эти символы есть
                    match2 = re.search("[0-9]", mobile_phone) #Если цифр нет
                    if (mobile_phone=='')or match1 or not(match2):
                        continue
                except:
                    mobile_phone = u'не указан'
                    continue
                try:
                    first_name = response['items'][usdx]['first_name']
                except:
                    first_name = u'имя нет'
                try:
                    last_name = response['items'][usdx]['last_name']
                except:
                    last_name = u'ФАМИЛИИ нет'
                vivod ='http://VK.com/id'+str(response['items'][usdx]['id'])+'\t'+str(gorod)+u'\t'+last_name+'\t'+first_name+u'\t'+mobile_phone+u'\t'+'\n'
                try:
                    vivod = vivod.encode("KOI8-R")
                except:
                    vivod = 'Ошибка пользователя id='+str(response['items'][usdx]['id'])
                percent = (100.0/kolvo)*indx
                print('Выполнено:'+str(percent)+'%\t')#+vivod
                file.write(vivod)
                telsea=telsea+1
            file.close
            print('_'*35+relig+'_'*3+'найдено:'+str(telsea)+' это в процентах:'+str(100.0/kolvo*telsea)+'_'*35)

        elif kolvo<9000:
            telsea=0
            indx=0
            file = open(str(gorod)+relig+'.txt', 'w')
            for birth_month in range(1,13):
                time.sleep(5)
                values = {'fields': 'contacts','birth_month':birth_month,'city': gorod,'religion':relig,'count':1000,'sort': 1}
                response = vk.method('users.search', values) #инфа об участниках. Разом
                print('_'*10+relig+'_'*10+'чел:'+str(kolvo)+'_'*10+'Месяц:'+str(birth_month)+'_'*10+str(gorod)+'_'*10)
                gran=response['count']
                if gran>1000:
                    gran=1000
                for usdx in range(0,gran):
                    indx=indx+1
                    try:
                        mobile_phone = response['items'][usdx]['mobile_phone']
                        match1 = re.search("[\.\?\*]", mobile_phone) #Если эти символы есть
                        match2 = re.search("[0-9]", mobile_phone) #Если цифр нет
                        if (mobile_phone=='')or match1 or not(match2):
                            continue
                    except:
                        mobile_phone = u'не указан'
                        continue
                    try:
                        first_name = response['items'][usdx]['first_name']
                    except:
                        first_name = u'имя нет'
                    try:
                        last_name = response['items'][usdx]['last_name']
                    except:
                        last_name = u'ФАМИЛИИ нет'
                    vivod ='http://VK.com/id'+str(response['items'][usdx]['id'])+'\t'+str(gorod)+u'\t'+last_name+'\t'+first_name+u'\t'+mobile_phone+u'\t'+'\n'
                    try:
                        vivod = vivod.encode("KOI8-R")
                    except:
                        vivod = 'Ошибка пользователя id='+str(response['items'][usdx]['id'])
                    percent = (100.0/kolvo)*indx
                    print('Выполнено:'+str(percent)+'%\t')#+vivod
                    file.write(vivod)
                    telsea=telsea+1
                file.close
                print('_'*35+relig+'_'*3+'найдено:'+str(telsea)+' это в процентах:'+str(100.0/kolvo*telsea)+'_'*35)
        else:
            telsea=0
            indx=0
            file = open(str(gorod)+relig+'.txt', 'w')
            values1 = {'city': gorod,'religion':relig} #Получение списка участников группы
            response1 = vk.method('users.search', values1)
            kolvo=response1['count']
            for birth_month in range(1,13):
                for birth_day in range(1,32):
                    time.sleep(15)
                    values = {'fields': 'contacts','birth_day':birth_day,'birth_month':birth_month,'city': gorod,'religion':relig,'count':1000,'sort': 1}
                    response = vk.method('users.search', values) #инфа об участниках. Разом
                    print('_'*10+relig+'_'*10+'чел:'+str(kolvo)+'_'*10+'Месяц:'+str(birth_month)+'    День:'+str(birth_day)+'_'*10+str(gorod)+'_'*10)
                    gran=response['count']
                    if gran>1000:
                        gran=1000
                    for usdx in range(0,gran):
                        indx=indx+1
                        try:
                            mobile_phone = response['items'][usdx]['mobile_phone']
                            match1 = re.search("[\.\?\*]", mobile_phone) #Если эти символы есть
                            match2 = re.search("[0-9]", mobile_phone) #Если цифр нет
                            if (mobile_phone=='')or match1 or not(match2):
                                continue
                        except:
                            mobile_phone = u'не указан'
                            continue
                        try:
                            first_name = response['items'][usdx]['first_name']
                        except:
                            first_name = u'имя нет'
                        try:
                            last_name = response['items'][usdx]['last_name']
                        except:
                            last_name = u'ФАМИЛИИ нет'
                        birthday=str(birth_day)+'.'+str(birth_month)
                        vivod ='http://VK.com/id'+str(response['items'][usdx]['id'])+'\t'+str(gorod)+u'\t'+last_name+'\t'+first_name+u'\t'+mobile_phone+u'\t'+birthday+'\n'
                        try:
                            vivod = vivod.encode("KOI8-R")
                        except:
                            vivod = 'Ошибка пользователя id='+str(response['items'][usdx]['id'])
                        percent = (100.0/kolvo)*indx
                        print('Выполнено:'+str(percent)+'%\t')#+vivod
                        file.write(str(vivod))
                        telsea=telsea+1
            file.close
            print('_'*35+relig+'_'*3+'найдено:'+str(telsea)+' это в процентах:'+str(100.0/kolvo*telsea)+'_'*35)

vko()
