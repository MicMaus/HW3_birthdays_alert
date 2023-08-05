from datetime import datetime, timedelta

def get_birthdays_per_week(users):

    Monday = []
    Tuesday = []
    Wednesday = []
    Thursday = []
    Friday = []

    week = {0: Monday, 1:Tuesday,2:Wednesday,3:Thursday,4:Friday,5:Monday,6:Monday}

    result = {'Monday': Monday, 'Tuesday': Tuesday, 'Wednesday': Wednesday, 'Thursday': Thursday, 'Friday': Friday}

    start = datetime.today()+ timedelta(days=1)
    next_week_end = start + timedelta(days=7)

    for user in users:
        user_fakebirthday = user["birthday"].replace(2023)
        if start.date() <= user_fakebirthday.date() <= next_week_end.date():
            week_day = user_fakebirthday.weekday()  #weekday of the birthday
            week[week_day].append(user["name"]) #adding names to resp list
    for day, list in result.items():
        if list:
            print(f'{day}: {", ".join(list)}')

def main():
    users = [
        {"name": "Tom", "birthday": datetime(year=1990, month=9, day=7)},
        {"name": "Sam", "birthday": datetime(year=1985, month=8, day=10)},
        {"name": "Paul", "birthday": datetime(year=1975, month=8, day=15)}
    ]
    get_birthdays_per_week(users)
if __name__ == "__main__":
    main()
