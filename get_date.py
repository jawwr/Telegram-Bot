from datetime import datetime,time,timedelta,timezone
from enum import Enum
from pytz import timezone

# Получене даты
def get_date_now():
    zone = timezone("Asia/Yekaterinburg")
    return datetime.now(zone)

# Получене номера дня недели
def get_day_number():
    zone = timezone("Asia/Yekaterinburg")
    date = datetime.now(zone)
    return date.weekday()

# Получене текущего времени
def get_time_now():
    zone = timezone("Asia/Yekaterinburg")
    time = datetime.now(zone)
    return time.strftime("%H:%M")

# Получене номера недели
def get_week_number():
    datenow = get_date_now()
    datetimefirst = datetime(2021,8,30).astimezone()
    delta = datenow - datetimefirst
    if (int(delta.days) // 7) % 2 == 0:
        return "Первая"
    if (int(delta.days) // 7) % 2 == 1:
        return "Вторая"

def parse_time(time):
    if(len(time) == 4):
        time = '0' + time
    return time