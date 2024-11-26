from faker import Faker
import psycopg2

# Ініціалізація об'єкта Faker для генерації фейкових даних
fake = Faker()

# Параметри підключення до бази даних
conn = psycopg2.connect(
    dbname="task_management",  # Назва бази даних
    user="postgres",           # Ім'я користувача
    password="Dfcbkmrj0111",   # Пароль користувача
    host="localhost",          # Хост
    port="5432"                # Порт для підключення до бази даних
)

# Створення курсора для виконання SQL-запитів
cursor = conn.cursor()

# Вставка 10 фейкових користувачів у таблицю users
for _ in range(10):
    fullname = fake.name()  # Генерація випадкового імені
    email = fake.email()    # Генерація випадкової електронної пошти
    cursor.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s)", 
        (fullname, email)  # Вставка згенерованих даних в таблицю
    )

# Збереження змін у базі даних
conn.commit()

# Закриття курсора та з'єднання з базою даних
cursor.close()
conn.close()
