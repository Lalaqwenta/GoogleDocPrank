#"entry.206608746"  : "Я уже Смешарик (несколько лет)"      Выбор одного ответа
#"entry.541429037"  : "ИМЯ_ОТВЕТ"                           Текст
#"entry.1949553758" : "КЛУБ_ОТВЕТ"                          Текст
#"entry.1861355305" : "СКОЛЬКО_ИГР_ОТВЕТ"                   Текст
#"entry.1772746954" : "ЧТО_ТРЕВОЖИТ_ОТВЕТ"                  Текст
#"entry.56781382"   : "КАК_ЛУЧШЕ_ОТВЕТ"                     Текст
#"entry.1418118175" : "ЧТО_ПОЛЕЗНО_ЗНАТЬ_ОТВЕТ"             Текст
#"entry.824422351"  : "ЧТО_НРАВИТСЯ_ОТВЕТ"                  Текст
#"entry.1226550788" : "ты состоишь в каком клубе"           Выбор одного ответа
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
import time

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
    what_do_you_like_to_play = multi_select_option_from_file(maps + "whatDoYouLikeToPlay", "add_other")
    what_do_you_like_to_play_other = mono_select_option_from_file(maps + "whatDoYouLikeToPlay_other", None)
#Какие проблемы вам встретились
    what_problems_found = multi_select_option_from_file(maps + "whatProblemsYouFound", "add_other")
    what_problems_found_other = mono_select_option_from_file(maps + "whatProblemsYouFound_other", None)
#Какие проблемы вы решили
    what_problems_solved = multi_select_option_from_file(maps + "whatProblemsYouSolved", "add_other")
    what_problems_solved_other = mono_select_option_from_file(maps + "whatProblemsYouSolve_other", None)
#На что ты любишь кататься (читаем из файлов)
    what_type_of_rp = multi_select_option_from_file(maps + "whatTypeOfRPAreYou", "add_other")
    what_type_of_rp_other = mono_select_option_from_file(maps + "whatTypeOfRPAreYou_other", None)
#Откуда об этом узнал
    where_did_you_learn = mono_select_option_from_file(maps + "whereDidYouLearnAboutLARP", "add_other")
    where_did_you_learn_other = mono_select_option_from_file(maps + "whereDidYouLearnAboutLARP_other", None)
#Как узнаешь про игры
    with_whom_do_you_attend = multi_select_option_from_file(maps + "withWhomDoYouAttend", "add_other")
    with_whom_do_you_attend_other = mono_select_option_from_file(maps + "withWhomDoYouAttend_other", None)
#Ты состоишь в каком-нибудь клубе или команде?
    are_you_in_club = mono_select_option_from_file(maps + "areYouInClub", "add_other")
    are_you_in_club_other = mono_select_option_from_file(maps + "areYouInClub_other", None)
#Название клуба в котором состоишь
    club_name = mono_select_option_from_file(maps + "clubNames", None)
#Как решил эти проблемы
    how_did_you_solve = multi_select_option_from_file(maps + "howDidYouSolve", "add_other")
    how_did_you_solve_other = mono_select_option_from_file(maps + "howDidYouSolve_other", None)
#Как обрастаешь снарягой
    how_do_you_get_stuff = mono_select_option_from_file(maps + "howDoYouGetStuff", "add_other")
    how_do_you_get_stuff_other = mono_select_option_from_file(maps + "howDoYouGetStuff_other", None)
#Как давно в РД
    how_long_in_larp = mono_select_option_from_file(maps + "howLongInLARP", "add_other")
    how_long_in_larp_other = mono_select_option_from_file(maps + "howLongInLARP_other", None)
#Сколько игр посетил
    how_many_games_attended = mono_select_option_from_file(maps + "howManyGamesAttended", None)
#Погоняло
    nickname = mono_select_option_from_file(maps + "nicknames", None)
    nickname = random.choice([nickname, name])
#
    what_troubles = mono_select_option_from_file(maps + "whatTroubles", None)
    what_can_improve = mono_select_option_from_file(maps + "whatCanImprove", None)
    what_newbie = mono_select_option_from_file(maps + "whatNewbie", None)
    what_i_like = mono_select_option_from_file(maps + "whatILike", None)
#формируем json
    form_data = {
        'entry.1226550788' : are_you_in_club,
        'entry.1226550788.other_option_response' : are_you_in_club_other,
        'entry.1949553758' : club_name,
        'entry.337047416'  : how_did_you_solve,
        'entry.337047416.other_option_response' : how_did_you_solve_other,
        'entry.522066257'  : how_do_you_get_stuff,
        'entry.522066257.other_option_response' : how_do_you_get_stuff_other,
        'entry.206608746'  : how_long_in_larp,
        'entry.206608746.other_option_response' : how_long_in_larp_other,
        'entry.1861355305' : how_many_games_attended,
        'entry.541429037'  : nickname,
        "entry.1315330665" : where_did_you_learn,
        "entry.1315330665.other_option_response" : where_did_you_learn_other,
        "entry.1741486870" : what_type_of_rp,
        "entry.1741486870.other_option_response" : what_type_of_rp_other,
        "entry.511178249"  : with_whom_do_you_attend,
        "entry.511178249.other_option_response"  : with_whom_do_you_attend_other,
        "entry.265185965"  : what_do_you_like_to_play,
        "entry.265185965.other_option_response" : what_do_you_like_to_play_other,
        "entry.650149429"  : what_problems_found,
        "entry.650149429.other_option_response"  : what_problems_found_other,
        "entry.1793078507" : what_problems_solved,
        "entry.1793078507.other_option_response" : what_problems_solved_other,
        "entry.1772746954" : what_troubles,
        "entry.56781382"   : what_can_improve,
        "entry.1418118175" : what_newbie,
        "entry.824422351"  : what_i_like
        }
#сохраняем сгенерированные имена в файл
    save_to_file_by_lines(str(form_data), config.log_path + "logs")
#отправляем запрос
    response = requests.post(urlResponse, data=form_data, headers=user_agent)
    if response.status_code != 200:
        with codecs.open(config.log_path + "error" + time.strftime("%Y%m%d-%H%M%S") + ".html", "a", encoding='utf-8') as file:
            file.write(response.text + '\n')
        return False
    else : return True

# Общие настройки
pers = Person(locale=Locale.RU)
url = config.url
maps = config.maps
urlResponse = url+'/formResponse'
urlReferer = url+'/viewform'
user_agent = {'Referer':urlReferer,'User-Agent': config.user_agent}

# в цикле
def main():
    i = 0
    while True:
        if post_record() :
            time.sleep(random.randint(0, 1))
            i+=1
            print(str(i) + "\n")
        else :
            return False

if main() :
    print ("All failed but I don't see where.")
else :
    print ("All failed as expected.")
