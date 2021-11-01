from datetime import datetime,time,timedelta

#Массив с наименованием дней недели, для расписания на неделю
day_name = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']

# Получене даты
def get_date_now():
    return datetime.today()

# Получене номера дня недели
def get_day_number():
    return (datetime.today().weekday())

#Метод установки времени
def set_time(timeset):
    time_set = timeset.split(':')
    return time(int(time_set[0]), int(time_set[1])).strftime('%H:%M')

# Получене текущего времени(+5 часов из-за разницы во времени с хостингом)
def get_time_now():
    time = datetime.today()
    time += timedelta(seconds = 18000)
    return time.strftime("%H:%M")

# Получене текущего времени
def get_time_now_normal():
    return datetime.today().strftime('%H:%M')

# Получене номера недели
def get_week_number():
    datenow = datetime.now()
    datetimefirst = datetime(2021,8,29)
    delta = datenow - datetimefirst
    if (int(delta.days) // 7) % 2 == 0:
        return "Первая"
    if (int(delta.days) // 7) % 2 == 1:
        return "Вторая"
