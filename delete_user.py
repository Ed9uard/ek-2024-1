import sqlite3

def delete_user():
    # Подключение к базе данных или создание новой, если она не существует
    conn = sqlite3.connect('testdb.db')

    conn.execute("PRAGMA foreign_keys = ON")

    cursor = conn.cursor()
    # Видалення користувача за його ідентифікатором з каскадним видаленням його завдань
    user_id = 3
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    
    # Збереження змін у базі даних
    conn.commit()

    # Закриття з'єднання з базою даних
    conn.close()

delete_user()