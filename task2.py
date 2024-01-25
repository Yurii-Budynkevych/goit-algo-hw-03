import random

def get_numbers_ticket(min, max, quantity=1):
    try:
        lotery = random.sample(range(min, max+1), quantity)
        print(lotery)
    except Exception as error:
        print('Error occured:', error, sep=' ')    

get_numbers_ticket(1, 1000, 6)