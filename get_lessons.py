import get_date
import setlessons

def get_lessons():
    week = get_week()
    day_now = get_date.get_day_number()
    timenow = get_date.get_time_now()
    if day_now == 6:
        return "no lesson"
    for i in range(0, len(week[day_now])):
        if (timenow >= get_date.set_time(week[day_now][i].time_start)) and (timenow <= get_date.set_time(week[day_now][i].time_end)):
            return week[day_now][i]
    for i in range(0, len(week[day_now]) - 1):
        if timenow >= (get_date.set_time(week[day_now][i].time_end)) and timenow <= (get_date.set_time(week[day_now][i+1].time_start)):
            return "pause"
    if timenow > get_date.set_time(week[day_now][len(week[day_now]) - 1].time_end):
        return "lessons are over"
    if timenow < get_date.set_time(week[day_now][0].time_start):
        return "lessons will start"

def get_all_lessons_today():
    week = get_week()
    day_now = get_date.get_day_number()
    text = ""
    les = get_lessons()
    if day_now == 6:
        text = text + "На сегодня пар нет"
    else:
        for i in range(0, len(week[day_now])):
            less_today = week[day_now][i]
            if check_lesson_now():
                if less_today == les:
                    text = text + "\n<b>{0}) Пара: {1}\nНачало в: {2}\nКонец в: {3}\nАудитория: {4}</b>\n".format(i+1,les.name,les.time_start, les.time_end,les.auditorium)
                else:
                    text = text + "\n{0}) Пара: {1}\nНачало в: {2}\nКонец в: {3}\nАудитория: {4}\n".format(i+1,less_today.name,less_today.time_start, less_today.time_end,less_today.auditorium)
            else:
                text = text + "\n{0}) Пара: {1}\nНачало в: {2}\nКонец в: {3}\nАудитория: {4}\n".format(i+1,less_today.name,less_today.time_start, less_today.time_end,less_today.auditorium)
    return text

def get_all_lessons_weeks():
    week = get_week()
    text = "\n<b>Сейчас {0} неделя.</b>\n\n".format(get_date.get_week_number())
    for day in range(0, len(week) - 1):
        text = text + "———————————\n"
        text = text + "<u><b>{0}:</b></u>\n".format(get_date.day_name[day])
        for less in range(0, len(week[day])):
            less_today = week[day][less]
            text = text + "\n<b>{0}) Пара:</b> {1}\n<b>Начало в:</b> {2}\n<b>Конец в:</b> {3}\n".format(less+1,less_today.name,less_today.time_start, less_today.time_end)
    return text

def check_lesson_now():
    lesson = get_lessons()
    return (lesson != 1) and (lesson != 0) and (lesson != 2) and (lesson != 3)

def get_week():
    if get_date.get_week_number() == "Первая":
        return setlessons.first_week_lessons
    if get_date.get_week_number() == "Вторая":
        return setlessons.second_week_lessons

def get_first_lessons():
    week = get_week()
    return week[get_date.get_day_number()][0]

def get_next_lessons():
    week = get_week()
    day_now = get_date.get_day_number()
    for i in range(0, len(week[day_now]) - 1):
        if get_date.get_time_now() >= (get_date.set_time(week[day_now][i].time_end)) and get_date.get_time_now() <= (get_date.set_time(week[day_now][i+1].time_start)):
            return week[day_now][i+1]