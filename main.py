# emailAddress - почта
# entry.2014055157 - кто ты такой
# entry.496536405 - что ты выигрывал
# name="entry.496536405.other_option_response" - что ты выигрывал (другое)
# entry.457997219 - кто твои друзья
# entry.825455790 - милфы начинаются с
# shagapov@phystech.edu


import requests
import mimesis
import locale
from mimesis import Person
from mimesis.locales import Locale
from mimesis import locales
import random

pers = Person(locale=Locale.RU)

GoogleURL = 'https://docs.google.com/forms/d/e/1FAIpQLSdGRAnwy6oHuIua_EWVlwSqFlOfUze0bZRk2WyuuUyLiZad9Q'
urlResponse = GoogleURL+'/formResponse'
urlReferer = GoogleURL+'/viewform'

form_data = {
            'entry.2014055157' : 'Артем слился',
            'entry.496536405' : {'Анус собаки','Ролевую игру'},
            'entry.457997219' : 'Геи пидоры из далекого долгопрудного',
            'entry.825455790' : '18',
            'emailAddress':'shagapov@phystech.edu'}

user_agent = {'Referer':urlReferer,'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}

for i in range(1, 11):
    name = pers.full_name()
    email = pers.email(domains=['mail.ru', 'yandex.ru', 'list.ru', 'gmail.com', 'bk.ru'])
    print(f'{name}, {email}')
    form_data = {
        'entry.2014055157': name,
        'entry.496536405': {'Анус собаки', 'Ролевую игру'},
        'entry.457997219': 'Геи пидоры из далекого долгопрудного',
        'entry.825455790': '18',
        'emailAddress': email}
    response = requests.post(urlResponse, data=form_data, headers=user_agent)
    print(response)
