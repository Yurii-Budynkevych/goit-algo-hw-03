import datetime as dt

def get_days_from_today(date):
    NOW = dt.datetime.now().date()

    try:
        paresd_date = dt.datetime.strptime(date, '%Y-%m-%d').date()
        delta = NOW - paresd_date
        if delta.days < 0:
            return "date is in the future" 
        return delta.days
    except Exception as error:
        return error

user_input = input('enter your date (YYYY-MM-DD): ')
print(get_days_from_today(user_input)) 