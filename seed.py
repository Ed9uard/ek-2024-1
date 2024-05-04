from faker import Faker
import sqlite3
import random

# Ініціалізуємо Faker для генерації випадкових даних
fake = Faker()

# Підключаємося до бази даних
conn = sqlite3.connect('testdb.db')
cursor = conn.cursor()

# Заповнюємо таблицю users
for _ in range(10):
    fullname = fake.name()
    email = fake.email()

    cursor.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", (fullname, email))

# Заповнюємо таблицю status зі списку унікальних статусів
status_list = ['new', 'in progress', 'completed']
for status in status_list:
    cursor.execute("INSERT INTO status (name) VALUES (?)", (status,))

# Заповнюємо таблицю tasks з випадковими значеннями
for _ in range(20):
    title = fake.text(max_nb_chars=100)
    description = fake.text()
    status_id = random.randint(1, len(status_list))
    user_id = random.randint(1, 10)

    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)",
                   (title, description, status_id, user_id))

# Зберігаємо зміни та закриваємо з'єднання
conn.commit()
conn.close()


