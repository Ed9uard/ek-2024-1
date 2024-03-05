import re

def normalize_phone(phone_number):
    # Видаляємо всі символи крім цифр та '+'
    digits_and_plus = re.sub(r'\D', '', phone_number)

    if digits_and_plus.startswith('380'):
        digits_and_plus = '+' + digits_and_plus
    else:
        digits_and_plus = '+38' + digits_and_plus 
   
    return digits_and_plus


# використання
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

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)