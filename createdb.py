import sqlite3

def create_tables():
    # Подключение к базе данных или создание новой, если она не существует
    conn = sqlite3.connect('testdb.db')
    cursor = conn.cursor()

    # Создание таблицы users
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fullname VARCHAR(100),
                    email VARCHAR(100) UNIQUE
                )''')

    # Создание таблицы status
    cursor.execute('''CREATE TABLE IF NOT EXISTS status (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50) UNIQUE
                )''')

    # Создание таблицы tasks
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title VARCHAR(100),
                    description TEXT,
                    status_id INTEGER,
                    user_id INTEGER,
                    FOREIGN KEY (status_id) REFERENCES status(id),
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
                )''')

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

def delete_tables():
    # Подключение к базе данных или создание новой, если она не существует
    conn = sqlite3.connect('testdb.db')
    cursor = conn.cursor()

    # Видалення таблиці tasks
    cursor.execute("DROP TABLE IF EXISTS tasks")

    # Видалення таблиці users
    cursor.execute("DROP TABLE IF EXISTS users")

    # Видалення таблиці status
    cursor.execute("DROP TABLE IF EXISTS status")

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

def clear_tables():
    # Подключение к базе данных или создание новой, если она не существует
    conn = sqlite3.connect('testdb.db')
    cursor = conn.cursor()

    # Видалення таблиці tasks
    cursor.execute("DELETE FROM users")

    # Видалення таблиці users
    cursor.execute("DELETE FROM status")

    # Видалення таблиці status
    cursor.execute("DELETE FROM tasks")

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

delete_tables()
# clear_tables()
create_tables()

