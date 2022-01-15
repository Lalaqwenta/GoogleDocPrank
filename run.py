#"entry.206608746"  : "Я уже Смешарик (несколько лет)"      Выбор одного ответа
#"entry.541429037"  : "ИМЯ_ОТВЕТ"                           Текст
#"entry.1949553758" : "КЛУБ_ОТВЕТ"                          Текст
#"entry.1861355305" : "СКОЛЬКО_ИГР_ОТВЕТ"                   Текст
#"entry.1772746954" : "ЧТО_ТРЕВОЖИТ_ОТВЕТ"                  Текст
#"entry.56781382"   : "КАК_ЛУЧШЕ_ОТВЕТ"                     Текст
#"entry.1418118175" : "ЧТО_ПОЛЕЗНО_ЗНАТЬ_ОТВЕТ"             Текст
#"entry.824422351"  : "ЧТО_НРАВИТСЯ_ОТВЕТ"                  Текст
#"entry.1226550788" : "Да"                                  Выбор одного ответа
#"entry.1315330665" : "Пригласил знакомый"                  Выбор одного ответа
#"entry.522066257"  : "Делаю всё своими руками!"            Выбор одного ответа
#"entry.1741486870" : "Тысячники"                           Выбор нескольких ответов
#"entry.511178249"  : "Езжу только со"                      Выбор нескольких ответов
#"entry.265185965"  : "Социалка"                            Выбор нескольких ответов
#"entry.650149429"  : "Непонятно где закупать снаряжение"   Выбор нескольких ответов
#"entry.1793078507" : "Проверенные крафтеры"                Выбор нескольких ответов
#"entry.337047416"  : "Горьким опытом"                      Выбор нескольких ответов

import config
import requests
from mimesis import Person
from mimesis.locales import Locale
import random
import codecs

#вытаскивает случайное кол-во вариантов из ткст файла
#и добавим __other_option__ в конец списка, если other_flag = add_other
def multi_select_option_from_file (txt_file_name, other_flag):
    with codecs.open(txt_file_name, encoding='utf-8') as txt_file:  # Читаем файл
        lines = txt_file.read().splitlines()
    ran_lines = random.sample(lines, random.randint(1, len(lines)))
    if other_flag == "add_other" :  list.append(ran_lines, '__other_option__')
    return ran_lines

#вытаcкивает один случайный вариант из ткст файла
#в том числе  __other_option__ , если other_flag = add_other
def mono_select_option_from_file (txt_file_name, other_flag):
    with codecs.open(txt_file_name, encoding='utf-8') as txt_file:  # Читаем файл
        lines = txt_file.read().splitlines()
    if other_flag == "add_other" : list.append(lines, '__other_option__')
    ran_choice = random.choice(lines)
    return ran_choice

#сохраняет строки построчно в ткст файл
def save_to_file_by_lines(name, txt_file_name):
    with codecs.open(txt_file_name, "a", encoding='utf-8') as file:
        file.write(name + '\n')

#Генерация рандомных значений и отправка запросов к гугл-форме
def post_record():
#имя
    name = pers.full_name()
#почта
    email = pers.email(domains=['mail.ru', 'yandex.ru', 'list.ru', 'gmail.com', 'bk.ru'])
#возраст милф
    milf_age = random.randint(30, 55)
#что ты выигрывал (читаем из файлов)
    what_did_you_win = multi_select_option_from_file(maps + "whatDidYouWin", "add_other")
    what_did_you_win_other = mono_select_option_from_file(maps + "whatDidYouWin_other", 0)
#кто твои друзья (читаем из файлов)
    who_are_your_friends = mono_select_option_from_file(maps + "whoAreYourFriends", "add_other")
    who_are_your_friends_other = mono_select_option_from_file(maps + "whoAreYourFriends_other", 0)
#формируем json
    form_data = {
        'entry.2014055157': name,
        'entry.496536405': what_did_you_win,
        'entry.496536405.other_option_response': what_did_you_win_other,
        'entry.457997219': who_are_your_friends,
        'entry.457997219.other_option_response': who_are_your_friends_other,
        'entry.825455790': milf_age,
        'emailAddress': email}
    print(form_data)
#сохраняем сгенерированные имена в файл
    save_to_file_by_lines(name, "savedNames")
#отправляем запрос
    response = requests.post(urlResponse, data=form_data, headers=user_agent)
    if response.status_code != 200:
        print(response)

# Общие настройки
pers = Person(locale=Locale.RU)
url = config.url
maps = config.maps
urlResponse = url+'/formResponse'
urlReferer = url+'/viewform'
user_agent = {'Referer':urlReferer,'User-Agent': config.user_agent}

# в цикле
def main():
    for i in range(1, 11):
        post_record()

main()
