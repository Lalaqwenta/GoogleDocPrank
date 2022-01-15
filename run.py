
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


# Общие настройки
pers = Person(locale=Locale.RU)
GoogleURL = 'https://docs.google.com/forms/d/e/1FAIpQLSdGRAnwy6oHuIua_EWVlwSqFlOfUze0bZRk2WyuuUyLiZad9Q'
urlResponse = GoogleURL+'/formResponse'
urlReferer = GoogleURL+'/viewform'
user_agent = {'Referer':urlReferer,'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}


#Генерация рандомных значений и отправка запросов к гугл-форме в цикле
for i in range(1, 3):
#имя
    name = pers.full_name()
#почта
    email = pers.email(domains=['mail.ru', 'yandex.ru', 'list.ru', 'gmail.com', 'bk.ru'])
#возраст милф
    milf_age = random.randint(30, 55)
#что ты выигрывал (читаем из файлов)
    what_did_you_win = multi_select_option_from_file("What did you win", "add_other")
    what_did_you_win_other = mono_select_option_from_file("Other - What did you win", 0)
#кто твои друзья (читаем из файлов)
    who_are_your_freinds = mono_select_option_from_file("Who are your freinds", "add_other")
    who_are_your_freinds_other = mono_select_option_from_file("Other - Who are your freinds", 0)
#формируем json
    form_data = {
        'entry.2014055157': name,
        'entry.496536405': what_did_you_win,
        'entry.496536405.other_option_response': what_did_you_win_other,
        'entry.457997219': who_are_your_freinds,
        'entry.457997219.other_option_response': who_are_your_freinds_other,
        'entry.825455790': milf_age,
        'emailAddress': email}
    print(form_data)
#сохраняем сгенерированные имена в файл
    save_to_file_by_lines(name, "Saved Names.txt")
#отправляем запрос
    response = requests.post(urlResponse, data=form_data, headers=user_agent)
    print(response)
