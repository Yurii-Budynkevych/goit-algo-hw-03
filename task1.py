import datetime as dt

NOW = dt.datetime.now().date()
input = input('enter your date (YYYY-MM-DD): ')

def get_days_from_today(date):
    try:
        paresd_date = dt.datetime.strptime(date, '%Y-%m-%d').date()
        delta = NOW - paresd_date
        print(delta.days, 'days passed')
    except Exception as error:
        print('Error occured:', error, sep=' ')    

get_days_from_today(input)    