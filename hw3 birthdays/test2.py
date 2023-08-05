#DO NOT DELETE 8 HOME WORK ALTERNATIVE

li = ["Pa","Sa"]
print(f"{el for el in li}")

users = [
        {"name": "Tom", "birthday": datetime(year=1990, month=9, day=7)},
        {"name": "Sam", "birthday": datetime(year=1985, month=8, day=3)},
        {"name": "Paul", "birthday": datetime(year=1975, month=8, day=6)}
    ]

'[{"name": "Tom", "birthday": datetime(year=1990, month=9, day=7)}, {"name": "Sam", "birthday": datetime(year=1985, month=8, day=3)}, {"name": "Paul", "birthday": datetime(year=1975, month=8, day=6)}]'

# today = datetime.today()
# next_week_start = today + timedelta(days=(7 - today.weekday()))  #2023-08-07 10:46:38.676184
# next_week_end = next_week_start + timedelta(days=6) #2023-08-13 12:27:52.335353

# for user in users:
#     user_fakebirthday = user["birthday"].replace(2023)
#     if next_week_start.date() <= user_fakebirthday.date() <= next_week_end.date():
#         week_day = user_fakebirthday.weekday()
#         users_congrat[user["name"]] = week[week_day]

________________________________

# defin of Sun (calendar.firstweekday() + 6)
#datetime object .weekday()
#four_weeks_interval = timedelta(weeks=4)

# str(datetime(year=1990, month=7, day=7)) #1990-07-07 00:00:00
# current_datetime = str(datetime.now()) #2023-07-31 09:38:52.758325

# next_mon = 14 - datetime.now().weekday()
# next_sun = 7 - datetime.now().weekday()
# nextweek_range = range((next_sun), (next_mon))  #7-13

# current_month = (str(datetime.now())).split("-")[1]   
# current_day = (str(datetime.now())).split("-")[2]

# for el in users:
#     for name, birthdate in el:
#         birth_month = (str(birthdate)).split("-")[1] 
#         birth_day = (str(birthdate)).split("-")[2]