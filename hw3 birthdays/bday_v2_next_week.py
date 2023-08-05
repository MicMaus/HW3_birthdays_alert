
from datetime import datetime, timedelta


def get_birthdays_per_week(users):

    Monday = []
    Tuesday = []
    Wednesday = []
    Thursday = []
    Friday = []

    week = {0: Monday, 1:Tuesday,2:Wednesday,3:Thursday,4:Friday,5:Monday,6:Monday}

    result = {'Monday': Monday, 'Tuesday': Tuesday, 'Wednesday': Wednesday, 'Thursday': Thursday, 'Friday': Friday}

    today = datetime.today()
    next_week_start = today + timedelta(days=(5 - today.weekday()))  #2023-08-07 10:46:38.676184
    next_week_end = next_week_start + timedelta(days=6) #2023-08-13 12:27:52.335353

    for user in users:
        user_fakebirthday = user["birthday"].replace(2023)
        if next_week_start.date() <= user_fakebirthday.date() <= next_week_end.date():
            week_day = user_fakebirthday.weekday()
            week[week_day].append(user["name"]) #adding names to resp list

    for day, list in result.items():
        if list:
            print(f'{day}: {", ".join(list)}')

def main():
    users = [
        {"name": "Tom", "birthday": datetime(year=1990, month=9, day=1)},
        {"name": "Sam", "birthday": datetime(year=1985, month=8, day=9)},
        {"name": "Paul", "birthday": datetime(year=1975, month=8, day=5)}
    ]
    get_birthdays_per_week(users)
if __name__ == "__main__":
    main()
