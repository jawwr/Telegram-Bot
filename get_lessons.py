import get_date
import setlessons

# Полчение текущей пары, если таковой не оказывается, то отправляется одна из причин
def get_lessons():
    week = get_week('')
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


# Получение расписания пар на сегодня,
def get_all_lessons_today():
    week = get_week('')
    day_now = get_date.get_day_number()
    text = ""
    les = get_lessons()
    if day_now == 6:
        text = text + "На сегодня пар нет"
    else:
        for i in range(0, len(week[day_now])):
            less_today = week[day_now][i]
            #Если в данный момент идет какая-то из пар, то она выделяется жирным шрифтом, иначе обычным
            if check_lesson_now():
                if less_today == les:
                    text = text + "\n<b>{0}) Пара: {1}\nНачало в: {2}\nКонец в: {3}\nАудитория: {4}</b>\n".format(i+1,les.name,les.time_start, les.time_end,les.auditorium)
                else:
                    text = text + "\n{0}) Пара: {1}\nНачало в: {2}\nКонец в: {3}\nАудитория: {4}\n".format(i+1,less_today.name,less_today.time_start, less_today.time_end,less_today.auditorium)
            else:
                text = text + "\n{0}) Пара: {1}\nНачало в: {2}\nКонец в: {3}\nАудитория: {4}\n".format(i+1,less_today.name,less_today.time_start, less_today.time_end,less_today.auditorium)
    return text


# Получение расписания на всю неделю, если неделя была выбрана, то расписание возвращается на выбранную, иначе на текущую
def get_all_lessons_weeks(name_week):
    week = get_week(name_week)
    if name_week == "":
        name_week = get_date.get_week_number()
    text = "\n<b>{0} неделя.</b>\n\n".format(name_week)
    for day in range(0, len(week)):
        text = text + "———————————\n"
        text = text + "<u><b>{0}:</b></u>\n".format(get_date.day_name[day])
        for less in range(0, len(week[day])):
            less_today = week[day][less]
            text = text + "\n<b>{0}) Пара:</b> {1}\n<b>Начало в:</b> {2}\n<b>Конец в:</b> {3}\n".format(less+1,less_today.name,less_today.time_start, less_today.time_end)
    return text


# Проверка, идет ли пара в данный момент
def check_lesson_now():
    lesson = get_lessons()
    return (lesson != "no lesson") and (lesson != "pause") and (lesson != "lessons are over") and (lesson != "lessons will start")


#Получение расписания на неделю из "БД"
def get_week(week_name):
    if week_name == "Первая":
        return setlessons.first_week_lessons
    if week_name == "Вторая":
        return setlessons.second_week_lessons
    if get_date.get_week_number() == "Первая":
        return setlessons.first_week_lessons
    if get_date.get_week_number() == "Вторая":
        return setlessons.second_week_lessons

#Полцчение первой пары, используется тогда, когда, пары еще не начались
def get_first_lessons():
    week = get_week('')
    return week[get_date.get_day_number()][0]

#Получение следующей пары, используется тогда, когда идет перемена
def get_next_lessons():
    week = get_week('')
    day_now = get_date.get_day_number()
    for i in range(0, len(week[day_now]) - 1):
        if get_date.get_time_now() >= (get_date.set_time(week[day_now][i].time_end)) and get_date.get_time_now() <= (get_date.set_time(week[day_now][i+1].time_start)):
            return week[day_now][i+1]