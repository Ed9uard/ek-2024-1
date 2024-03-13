def total_salary(path):
    total_salary = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]  # Отримати список рядків без пробілів 
            for line in lines:
                try:
                    name, salary = line.split(',')
                    total_salary += int(salary) 
                    count += 1
                except ValueError:
                    print(f"Помилка у форматі рядка: {line}")
    except FileNotFoundError:
        print("Файл не знайдено.")
        return count,total_salary
    
    except IOError:
        print("Помилка відкриття файлу.")
        return count,total_salary

    if count == 0:
        print("У файлі немає даних.")
        return count,total_salary

    average_salary = total_salary / count
    return total_salary, int(average_salary)


# Приклад використання
total, average = total_salary("fileForTask1.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")