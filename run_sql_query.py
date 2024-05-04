import sqlite3

# З'єднання з базою даних
conn = sqlite3.connect('testdb.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# Читання SQL запитів з файлу
with open('queries.sql', 'r') as file:
    queries = file.readlines()

# Видалення порожніх рядків та символів нового рядка
queries = [query.strip() for query in queries if query.strip()]

# Виконання кожного запиту та вивід результату
for query in queries:
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)

conn.commit()
conn.close()