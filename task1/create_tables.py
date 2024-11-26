import psycopg2

# Параметри підключення до бази даних
conn_params = {
    "dbname": "task_management",
    "user": "postgres",
    "password": "Dfcbkmrj0111",
    "host": "localhost",
    "port": "5432"
}

# SQL для створення таблиць
create_tables_sql = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER REFERENCES status(id),
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
"""

# Виконання SQL
def create_tables():
    try:
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute(create_tables_sql)
                conn.commit()
                print("Таблиці створено успішно!")
    except Exception as e:
        print(f"Помилка під час створення таблиць: {e}")

if __name__ == "__main__":
    create_tables()
