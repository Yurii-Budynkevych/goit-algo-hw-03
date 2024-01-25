import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_numbers):
    normalized_list = []

    for number in phone_numbers:
        pattern = r"[^\d+]"
        normalized_number = re.sub(pattern, "", number)

        if normalized_number.find('+') == 0:
            pass
        elif normalized_number.find('380') == 0:
            normalized_number = '+' + normalized_number
        elif normalized_number.find('0') == 0:
            normalized_number = '+38' + normalized_number     

        normalized_list.append(normalized_number)

    return(normalized_list)

print(normalize_phone(raw_numbers))