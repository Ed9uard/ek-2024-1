from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError
from pymongo.server_api import ServerApi
connected = False

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            if connected:
                return func(*args, **kwargs)
            else:
                print("Немає підключення до бази даних.")
        except DuplicateKeyError:
            print("Кіт з таким ім'ям вже існує.")
        except Exception as e:
            print("Помилка:", e)
    return wrapper

try:
    client = MongoClient(
        "mongodb+srv://ed9uard:MGuHLevfZhdvw3Ru@cluster0.wkfa92c.mongodb.net/",
        server_api=ServerApi('1')
    )
    
    print(client) # connect=True навіть коли невірний пас або login ... не зовсім ясно як відловити коннект 
    print()
    connected = True

    db = client.hm

    

    @handle_exceptions
    def insert_one_cat(name, age, features):
        result = db.cats.insert_one({"name": name, "age": age, "features": features})
        print("Додано кота з ім'ям", name)
        print("ID вставленого документа:", result.inserted_id)

    @handle_exceptions
    def insert_many_cats(cats):
        result = db.cats.insert_many(cats)
        print("Додано кілька котів.")
        print("ID вставлених документів:", result.inserted_ids)

    @handle_exceptions
    def display_all_cats():
        cats = db.cats.find()
        for cat in cats:
            print(cat)

    @handle_exceptions
    def display_cat_by_name(name):
        cat = db.cats.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Кіт з таким ім'ям не знайдений.")

    @handle_exceptions
    def update_cat_age(name, new_age):
        db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
        print("Вік кота оновлено.")
        cat = db.cats.find_one({"name": name})
        print(cat)

    @handle_exceptions
    def add_feature_to_cat(name, new_feature):
        db.cats.update_one({"name": name}, {"$push": {"features": new_feature}})
        print("Нова характеристика додана.")
        cat = db.hm.find_one({"name": name})
        print(cat)

    @handle_exceptions
    def delete_cat_by_name(name):
        result = db.cats.delete_one({"name": name})
        if result.deleted_count > 0:
            print("Кіт видалений за ім'ям " + name + ".")
        else:
            print("Кіт з ім'ям " + name + " не знайдений.")

    @handle_exceptions
    def delete_all_cats():
        db.cats.delete_many({})
        print("Всі коти видалені.")

    cats = [
        {"name": "Lama", "age": 2, "features": ["ходить в лоток", "не дає себе гладити", "сірий"]},
        {"name": "Liza", "age": 4, "features": ["ходить в лоток", "дає себе гладити", "білий"]}
    ]

    print("Функція для вставки одного документу в колекцію")
    print('insert_one_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])')
    insert_one_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    print()

    print("Функція для вставки кількох документів в колекцію.")
    print('insert_many_cats(cats)')
    insert_many_cats(cats)
    print()

    print("Функція для виведення всіх записів із колекції.")
    print("display_all_cats()")
    display_all_cats()
    print()

    print("Функція, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота.")
    print('display_cat_by_name("barisik")')
    display_cat_by_name("barsik")
    print()

    print("Функція, яка дозволяє користувачеві оновити вік кота за ім'ям.")
    print('update_cat_age("barsik", 4)')
    update_cat_age("barsik", 4)
    print()

    print("Функція, яка дозволяє додати нову характеристику до списку features кота за ім'ям.")
    print('add_feature_to_cat("barsik", "лінивий")')
    add_feature_to_cat("barsik", "лінивий")
    print()

    print("Функція для видалення запису з колекції за ім'ям тварини")
    print('delete_cat_by_name("murzik")')
    delete_cat_by_name("murzik")
    print()

    print("Функція для видалення запису з колекції за ім'ям тварини")
    print('delete_cat_by_name("barsik")')
    delete_cat_by_name("barsik")
    print()

    # print("Функція для видалення всіх записів із колекції.")
    # print("delete_all_cats()")
    # delete_all_cats()
    # print()

    client.close()

except Exception as e:
    print("Помилка підключення до бази даних:", e)
    exit()