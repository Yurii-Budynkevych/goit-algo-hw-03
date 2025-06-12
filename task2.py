import random

def get_numbers_ticket(min, max, quantity=1):
    try:
        if min < 1 or max > 1000:
            return []
        lotery = sorted(random.sample(range(min, max + 1), quantity))
        return lotery
    except Exception as error:
        return []

print(get_numbers_ticket(1, 1000, 6))