from datetime import datetime, timedelta
from collections import defaultdict


def get_next_week():
    return ((datetime.now() + timedelta(7 - datetime.now().weekday())).replace(hour=0, minute=0, second=0), 
(datetime.now() + timedelta(7 - datetime.now().weekday() + 6)).replace(hour=23, minute=59, second=59))

def is_weekend(date):
    day = date.weekday()
    return day == 5 or day == 6



def get_birthdays_per_week(users):
    start_of_week, end_of_week = get_next_week()
    weekend = timedelta(days=2)

    birthday_dic = defaultdict(list)

    for user in users:
        birthday = user["birthday"].replace(year=datetime.now().year)
        if start_of_week - weekend <= birthday <= end_of_week - weekend:
            if is_weekend(birthday):
                birthday_dic["Monday"].append(user["name"])
            else:
                birthday_dic[birthday.strftime("%A")].append(user["name"])

    return birthday_dic
        
