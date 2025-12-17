import psycopg2


class DBManager:
    """Класс для фильтрации данных таблиц"""

    def __init__(self, params: dict):
        self.params = params

    def get_vacancies_with_keyword(self, dbname: str, words: str):
        """Функция для поиска вакансии по заданному слову"""

        conn = psycopg2.connect(dbname=dbname, **self.params)
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM vacancies WHERE vacancy LIKE '{words}%'")
        conn.commit()

        rows = cur.fetchall()
        if len(rows) == 0:
            print("Вакансии по заданному слову не найдено")
        else:
            for row in rows:
                print(row)

        cur.close()
        conn.close()

    def get_companies_and_vacancies_count(self, dbname: str):
        """Функция для получения списка всех компании и количества их вакансии"""

        conn = psycopg2.connect(dbname=dbname, **self.params)
        cur = conn.cursor()

        cur.execute("SELECT name, open_vacancies FROM employers")
        conn.commit()

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        conn.close()

    def get_all_vacancies(self, dbname: str):
        """Функция для получения списка всех вакансии"""

        conn = psycopg2.connect(dbname=dbname, **self.params)
        cur = conn.cursor()

        cur.execute("SELECT company_name, vacancy, salary_from, url FROM vacancies")
        conn.commit()

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        conn.close()

    def get_avg_salary(self, dbname: str):
        """Функция для получения средней зарплаты"""

        conn = psycopg2.connect(dbname=dbname, **self.params)
        cur = conn.cursor()

        cur.execute("SELECT AVG(salary_from) FROM vacancies")
        conn.commit()

        rows = cur.fetchall()
        print(rows)

        cur.close()
        conn.close()

    def get_vacancies_with_higher_salary(self, dbname: str):
        """Функция для получения вакансии у которых зарплата выше средней"""

        conn = psycopg2.connect(dbname=dbname, **self.params)
        cur = conn.cursor()

        cur.execute("""SELECT * FROM vacancies
        WHERE salary_from > (SELECT AVG(salary_from)
        FROM vacancies WHERE salary_from IS NOT NULL)
        ORDER BY salary_from DESC
        """)
        conn.commit()

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        conn.close()
