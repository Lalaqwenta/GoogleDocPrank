# emailAddress - почта
# entry.2014055157 - кто ты такой
# entry.496536405 - что ты выигрывал
# name="entry.496536405.other_option_response" - что ты выигрывал (другое)
# entry.457997219 - кто твои друзья
# entry.825455790 - милфы начинаются с
# shagapov@phystech.edu

import config
import requests
import mimesis
import locale
from mimesis import Person
from mimesis.locales import Locale
from mimesis import locales
import random

def post_record():
    name = pers.full_name()
    email = pers.email(domains=['mail.ru', 'yandex.ru', 'list.ru', 'gmail.com', 'bk.ru'])
    print(f'{name}, {email}')
    form_data = {
        'entry.2014055157': name,
        'entry.496536405': {'Анус собаки', 'Ролевую игру'},
        'entry.457997219': 'Геи пидоры из далекого долгопрудного',
        'entry.825455790': '18',
        'emailAddress': email
    }
    response = requests.post(urlResponse, data=form_data, headers=user_agent)
    if response.status_code != 200:
        print(response)

pers = Person(locale=Locale.RU)

url = config.url
urlResponse = url+'/formResponse'
urlReferer = url+'/viewform'

user_agent = {'Referer':urlReferer,'User-Agent': config.user_agent}

def main():
    for i in range(1, 11):
        post_record()

main()
