# from get_date import get_date_now, get_day_number, get_time_now, get_week_number, parse_time
from get_date import *
import json

lessons = ''
with open('lessons.json',encoding='utf-8') as f:
    lessons = json.load(f)



# Полчение текущей пары, если таковой не оказывается, то отправляется одна из причин
def get_lessons():
    day_now = get_day_number()
    if day_now == 6:
        return "no lesson"
    week = get_week('')['day'][day_now]['lessons']
    time_now = get_time_now()
    if time_now > parse_time(week[len(week) - 1]['time_end']):
        return "lessons are over"
    if time_now < parse_time(week[0]['time_start']):
       return "lessons will start"
    for lessons_today in week:
        if (time_now >= parse_time(lessons_today['time_start']) and time_now <= parse_time(lessons_today['time_end'])):
            return lessons_today
    for i in range(0, len(week) - 1):
        if (time_now >= parse_time(week[i]['time_end']) and time_now <= parse_time(week[i+1]['time_start'])):
            return "pause"




# Получение расписания пар на сегодня
def get_all_lessons_today():
    day_now = get_day_number()
    if day_now == 6:
        return "На сегодня пар нет"
    week = get_week('')['day'][day_now]['lessons']
    text = ''
    les = get_lessons()
    for i in range(0, len(week)):
        less_today = week[i]
        #Если в данный момент идет какая-то из пар, то она выделяется жирным шрифтом, иначе обычным
        if check_lesson_now():
            if less_today == les:
                text += f"\n<b>{i+1}) Пара: {les['name']}\nНачало в: {les['time_start']}\nКонец в: {les['time_end']}\nАудитория: {les['auditorium']}</b>\n"
            else:
                text += f"\n{i+1}) Пара: {less_today['name']}\nНачало в: {less_today['time_start']}\nКонец в: {less_today['time_end']}\nАудитория: {less_today['auditorium']}\n"
        else:
            text += f"\n{i+1}) Пара: {less_today['name']}\nНачало в: {less_today['time_start']}\nКонец в: {less_today['time_end']}\nАудитория: {less_today['auditorium']}\n"
    return text

# Получение расписания на завтра
def get_all_lessons_tomorrow():
    week = get_week('')
    day_tomorrow = get_day_number() + 1
    if get_week_number() == "Первая" and day_tomorrow == 7:
        week = get_week("Вторая")
        day_tomorrow = 0
    elif get_week_number() == "Вторая" and day_tomorrow == 7:
        week = get_week("Первая")
        day_tomorrow = 0
    week = week['day'][day_tomorrow]['lessons']
    text = ''
    if day_tomorrow == 6:
        text += "Пар нет"
    else:
        for i in range(0, len(week)):
            less_today = week[i]
            text += f"\n{i+1}) Пара: {less_today['name']}\nНачало в: {less_today['time_start']}\nКонец в: {less_today['time_end']}\nАудитория: {less_today['auditorium']}\n"
    return text

# Получение расписания на всю неделю, если неделя была выбрана, то расписание возвращается на выбранную, иначе на текущую
def get_all_lessons_weeks(name_week):
    if name_week == "":
        name_week = get_week_number()
    week = get_week(name_week)['day']
    text = f"\n<b>{name_week} неделя.</b>\n\n"
    for day in week:
        text = text + "———————————\n"
        text = text + f"<u><b>{day['name']}:</b></u>\n"
        i = 0
        for less in day['lessons']:
            i += 1
            less_today = less
            text += f"\n<b>{i}) Пара:</b> {less_today['name']}\n<b>Начало в:</b> {less_today['time_start']}\n<b>Конец в:</b> {less_today['time_end']}\n"
    return text


# Проверка, идет ли пара в данный момент
def check_lesson_now():
    lesson = get_lessons()
    return (lesson != "no lesson") and (lesson != "pause") and (lesson != "lessons are over") and (lesson != "lessons will start")


#Получение расписания на неделю
def get_week(week_name):
    if week_name == "Первая":
        return lessons['first_week']
    if week_name == "Вторая":
        return lessons['second_week']
    if get_week_number() == "Первая":
        return lessons['first_week']
    if get_week_number() == "Вторая":
        return lessons['second_week']

#Полцчение первой пары, используется тогда, когда, пары еще не начались
def get_first_lessons():
    week = get_week('')
    return week['day'][get_day_number()]['lessons'][0]

#Получение следующей пары, используется тогда, когда идет перемена
def get_next_lessons():
    day_now = get_day_number()
    week = get_week('')['day'][day_now]['lessons']
    for i in range(0, len(week) - 1):
        if get_time_now() >= week[i]['time_end'] and get_time_now() <= week[i+1]['time_start']:
            return week[i+1]