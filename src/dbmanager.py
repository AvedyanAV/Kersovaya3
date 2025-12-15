import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DBManager:
    """Класс для создания баз данных и таблиц"""
    def __init__(self, params: dict):
        self.params = params

    def add_db(self, dbname: str = 'hh'):
        """Создание базы данных"""

        conn = psycopg2.connect(dbname='postgres', **self.params)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        cur.execute(f"""
            SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = '{dbname}'
            AND pid <> pg_backend_pid();
        """)

        cur.execute(f"DROP DATABASE IF EXISTS {dbname}")

        cur.execute(f"CREATE DATABASE {dbname}")
        print(f"База данных {dbname} успешно создана")

        cur.close()
        conn.close()

    def create_tables(self, dbname: str ):
        """Создание таблиц в базе данных"""

        conn = psycopg2.connect(dbname=dbname, **self.params)
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS employers (
                id VARCHAR(50) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                open_vacancies INTEGER
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS vacancies (
                id_company VARCHAR(50) REFERENCES employers(id),
                id_vacancy VARCHAR(50) PRIMARY KEY,
                company_name VARCHAR(50),
                vacancy VARCHAR(100),
                salary_from INTEGER,
                salary_to INTEGER,
                url TEXT
            )
        """)

        conn.commit()
        print("Таблицы успешно созданы")

        cur.close()
        conn.close()

    def save_data_employers(self, dbname: str ,data: list):
        """Функция для сохранения данных в таблицы"""

        conn = psycopg2.connect(dbname=dbname, **self.params)
        cur = conn.cursor()
        data_save_data_employers = data
        for emp in data_save_data_employers:
            cur.execute(
                """
                INSERT INTO employers (id, name, open_vacancies)
                VALUES (%s, %s, %s)
                """,
                (emp['id'], emp['name'], emp['open_vacancies'])
            )
        print("Данные занесены в таблицу employers")
        conn.commit()
        conn.close()

    def save_data_vacancies(self, dbname: str ,data: list):
        """Функция для сохранения данных в таблицы"""

        conn = psycopg2.connect(dbname=dbname, **self.params)
        cur = conn.cursor()
        data_save_data_employers = data
        for emp in data_save_data_employers:
            for i in emp:
                cur.execute(
                """
                INSERT INTO vacancies (id_company, id_vacancy, company_name, vacancy, 
                salary_from, salary_to, url)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (i['id_company'], i['id_vacancy'], i['company_name'], i['vacancy'],
                 i['salary_from'], i['salary_to'], i['url'])
            )
        print("Данные занесены в таблицу vacancies")
        conn.commit()
        conn.close()
















