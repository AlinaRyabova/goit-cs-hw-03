import pymongo
from pymongo import MongoClient

# Підключення до MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['cats_db']  # створення бази даних
    collection = db['cats']  # створення колекції
    print("Підключення до MongoDB успішне!")
except Exception as e:
    print(f"Помилка підключення до MongoDB: {e}")
    exit()

# Структура документа
sample_data = {
    "name": "barsik",
    "age": 3,
    "features": ["ходит в капці", "дає себе гладити", "рудий"]
}

# Функція для додавання нового кота
def add_cat(cat_data):
    try:
        existing_cat = collection.find_one({"name": cat_data["name"]})
        if existing_cat:
            print(f"Кіт з ім'ям {cat_data['name']} вже існує.")
        else:
            collection.insert_one(cat_data)
            print(f"Кіт {cat_data['name']} доданий!")
    except Exception as e:
        print(f"Помилка при додаванні кота: {e}")

# Читання (Read) всієї колекції
def get_all_cats():
    try:
        cats = list(collection.find())
        if cats:
            for cat in cats:
                print(cat)
        else:
            print("Колекція порожня.")
    except Exception as e:
        print(f"Помилка при отриманні котів: {e}")

# Читання (Read) кота за ім'ям
def get_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при отриманні кота за ім'ям: {e}")

# Оновлення віку кота
def update_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(f"Вік кота {name} оновлений на {new_age}.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений для оновлення.")
    except Exception as e:
        print(f"Помилка при оновленні віку: {e}")

# Додавання нової характеристики коту
def add_feature(name, new_feature):
    try:
        result = collection.update_one(
            {"name": name},
            {"$addToSet": {"features": new_feature}}  # $addToSet уникає дублювання
        )
        if result.modified_count > 0:
            print(f"Нова характеристика додана коту {name}.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений або така характеристика вже існує.")
    except Exception as e:
        print(f"Помилка при додаванні характеристики: {e}")

# Видалення кота за ім'ям
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кіт з ім'ям {name} видалений.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений для видалення.")
    except Exception as e:
        print(f"Помилка при видаленні кота: {e}")

# Видалення всіх котів з колекції
def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"{result.deleted_count} котів видалено.")
    except Exception as e:
        print(f"Помилка при видаленні котів: {e}")

# Тестування функцій
if __name__ == "__main__":
    # Додати кота (як приклад)
    add_cat(sample_data)

    # Отримати всіх котів
    print("\nВсі коти в базі:")
    get_all_cats()

    # Отримати кота за ім'ям
    print("\nОтримати кота за ім'ям 'barsik':")
    get_cat_by_name("barsik")

    # Оновити вік кота
    print("\nОновлення віку кота:")
    update_age("barsik", 4)

    # Додати нову характеристику коту
    print("\nДодавання нової характеристики:")
    add_feature("barsik", "любить спати на дивані")

    # Видалити кота за ім'ям
    print("\nВидалення кота за ім'ям:")
    delete_cat_by_name("barsik")

    # Видалити всіх котів
    print("\nВидалення всіх котів:")
    delete_all_cats()
