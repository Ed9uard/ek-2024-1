def get_cats_info(path):
    cat_records = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat_record = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2]
                    }
                    cat_records.append(cat_record)
                else:
                    print(f"Виявлено недопустимий формат у рядку: {line.strip()}.")

    except FileNotFoundError:
        print("Файл не знайдено.")
    
    except IOError:
        print("Помилка відкриття файлу.")

    except Exception as e:
        print(f"Виникла помилка: {str(e)}")

    return cat_records

# Приклад використання
cats_info = get_cats_info("fileForTask2.txt")
print(cats_info)