import datetime as dt
# print(type(dt))  # module

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day   # 1-31
date = now.date() #%Y-%m-%d
day_of_week = now.weekday()  #0(Monday)-6(Sunday)
date_strf = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")



# print(now)  # datatime.datetime
# print(type(year))  # int
# print(type(now))  # int
# print(year)
# print(date)
# print(f'date from now: {date}')
# print(day_of_week)
# print(f'date from now().strftime(): {date_strf}') 
# print(f'type from now().strftime(): {type(date_strf)}')  # str
# print(time)

# today = dt.datetime.today()
# date_today = today.date() #%Y-%m-%d
# print(f'date from today().date(): {date_today}')
# print(f'type from today().date(): {type(date_today)}') #datetime.date

# ----------------------------------------------------
from datetime import datetime,timezone

# get current time in utc
utc_now = datetime.now(timezone.utc)
print(f'Current UTC time: {utc_now}')   # at utc

# convert specific time to UTC
local_time = datetime(2024,10,26,12,30)   # approximate time is fine
utc_time = local_time.replace(tzinfo=timezone.utc)
print(f'Specific UTC time: {utc_time}')

# convert new reference point UTC time to different timezone
from datetime import timedelta

moscow_time= utc_now.astimezone(timezone(timedelta(hours=3)))
print("Moscow time:", moscow_time)


# ----------------------------------------------------

import pytz
# # using pytz
timezone = pytz.timezone("Asia/Bangkok")
current_time = datetime.now(timezone)
print(f'timezone as specific: {current_time}')

# ----------------------------------------------------


# date_of_birth =  dt.datetime(year= 1990,month=12,day=15)
# print(date_of_birth)

# https://docs.python.org/3/library/datetime.html#datetime.timezone.utc
# print(dt.timezone.utc)