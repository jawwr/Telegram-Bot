from datetime import datetime,time, timedelta
import calendar

day_name = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']

def get_date_now():
    return datetime.today()

def get_day_number():
    return (datetime.today().weekday())

def set_time(timeset):
    time_set = timeset.split(':')
    return time(int(time_set[0]), int(time_set[1])).strftime('%H:%M')

def get_time_now():
    return datetime.today().strftime("%H:%M")

def get_week_number():
    datenow = datetime.now()
    datetimefirst = datetime(2021,8,29)
    delta = datenow - datetimefirst
    if (int(delta.days) // 7) % 2 == 0:
        return "Первая"
    if (int(delta.days) // 7) % 2 == 1:
        return "Вторая"
