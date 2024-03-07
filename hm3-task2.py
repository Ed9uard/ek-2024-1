import random

def get_numbers_ticket(min , max , quantity):
    # Перевірка вхідних параметрів
        #min - мінімальне можливе число у наборі (не менше 1).
        #max - максимальне можливе число у наборі (не більше 1000).
        #quantity - кількість чисел, які потрібно вибрати (значення між min і max).
    
    if not (1 <= min <= max <= 1000):
        print("Неправильний діапазон чисел у наборі. Вони повинні бути між 1 і 1000.") 
        return [] 

                   
    if not (min < quantity < max):
        print("Неправильне значення кількості чисел. Потрібно вибрати (значення між min і max)")
        return []

    numbers_set = set() 
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min, max))  # додання рандомних чисел до сету (множина унікальних елементів)

    
    lottery_numbers = sorted(list(numbers_set)) # сортування 
    return lottery_numbers


lottery_numbers = get_numbers_ticket(1, 49, 9)
#print(not (1 <= 0 <= 49 <= 1000)) перевірка перевірок
if lottery_numbers:
    print("Ваші лотерейні числа:", lottery_numbers)