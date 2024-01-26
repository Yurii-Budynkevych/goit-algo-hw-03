import datetime as dt

users = [
    {"name": "John Smith", "birthday": "1991.01.30"},
    {"name": "Jane Smith", "birthday": "1994.01.27"},
    {"name": "Mytsy Brush", "birthday": "1975.11.15"},
    {"name": "Abby Errty", "birthday": "2005.08.05"},
    {"name": "John Doe", "birthday": "2004.01.23"},
    {"name": "Sally Doe", "birthday": "1995.12.25"}
]

def get_upcoming_birthdays (b_list):
    in7_days_cograts = []
    now = dt.datetime.now().date()
    for user in b_list:
        birthday = user['birthday']
        paresd_birthday = dt.datetime.strptime(birthday, '%Y.%m.%d').date()
        paresd_birthday = paresd_birthday.replace(year=now.year)

        if paresd_birthday < now:
            paresd_birthday = paresd_birthday.replace(year=now.year + 1)

        if paresd_birthday.weekday() == 5:
            paresd_birthday = paresd_birthday.replace(day=paresd_birthday.day + 2)
        elif paresd_birthday.weekday() == 6:
            paresd_birthday = paresd_birthday.replace(day=paresd_birthday.day + 1)     

        difference = (paresd_birthday - now).days    
        if difference <= 7:
            in7_days_cograts.append({"name": user['name'], "congrats_date": paresd_birthday})

    return(in7_days_cograts)

print(get_upcoming_birthdays(users))