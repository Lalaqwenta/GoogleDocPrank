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
#Во что ты любишь играть
    what_do_you_like_to_play = multi_select_option_from_file(maps + "whatDoYouLikeToPlay")
#Какие проблемы вам встретились
    what_problems_found = mono_select_option_from_file(maps + "whatProblemsYouFound", None
#Какие проблемы вы решили
    what_problems_solved = mono_select_option_from_file(maps + "whatProblemsYouSolved", None
#На что ты любишь кататься (читаем из файлов)
    what_type_of_rp = multi_select_option_from_file(maps + "whatTypeOfRPAreYou", "add_other")
    what_type_of_rp_other = mono_select_option_from_file(maps + "whatTypeOfRPAreYou_other", None)
#Откуда об этом узнал
    where_did_you_learn = mono_select_option_from_file(maps + "whereDidYouLearnAboutLARP", "add_other")
    where_did_you_learn_other = mono_select_option_from_file(maps + "whereDidYouLearnAboutLARP_other", None)
#Как узнаешь про игры
    with_whom_do_you_attend = multi_select_option_from_file(maps + "withWhomDoYouAttend", "add_other")
    with_whom_do_you_attend_other = mono_select_option_from_file(maps + "withWhomDoYouAttend_other", None)
#формируем json
    form_data = {
        "entry.206608746"  : 
        "entry.541429037"  : 
        "entry.1949553758" : 
        "entry.1861355305" : 
        "entry.1772746954" : 
        "entry.56781382"   : 
        "entry.1418118175" : 
        "entry.824422351"  : 
        "entry.1226550788" : 
        "entry.1315330665" : where_did_you_learn, 
        "entry.1315330665.other_option_response" : where_did_you_learn_other,
        "entry.522066257"  : 
        "entry.1741486870" : what_type_of_rp,
        "entry.1741486870.other_option_response" : what_type_of_rp_other,
        "entry.511178249"  : with_whom_do_you_attend,
        "entry.511178249.other_option_response"  : with_whom_do_you_attend_other,
        "entry.265185965"  : what_do_you_like_to_play,
        "entry.650149429"  : what_problems_found,
        "entry.1793078507" : what_problems_solved,
        "entry.337047416"  : 
    }
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
    for i in range(1, 2):
        post_record()

main()
