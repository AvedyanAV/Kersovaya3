import os
from dotenv import load_dotenv
from src.hh_api import HHEmployerAPI
from src.dbmanager import DBManager

load_dotenv()
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')


params = {
  "host": DATABASE_HOST,
  "user": DATABASE_USER,
  "password": DATABASE_PASSWORD
}

def main():
    """Основная функция"""

    api = HHEmployerAPI()
    db = DBManager(params)

    data_employ = []
    data_vacancies = []


    print("Список компании для проверки работы программы")
    print("1.Яндекс", "2.АльфаБанк", "3.Магнит", "4.DNS", "5.Emex",
          "6.Ростелеком", "7.Т-Банк", "8.VK", "9.HH", "10.585 Золотой", sep="\n")

    employ = ["Яндекс", "АльфаБанк", "МАГНИТ, Розничная сеть", "DNS", "Emex",
          "Ростелеком", "Т-Банк", "VK", "HH", "585 Золотой"]
    for i in employ:
        companies = api.get_employer(i)
        data_employ.append(companies)

        vacancies = api.get_vacancies(companies['id'])
        data_vacancies.append(vacancies)

    # print(data_employ)
    # print(data_vacancies)

    db.add_db("test")
    db.create_tables("test")
    db.save_data_employers("test", data_employ)
    db.save_data_vacancies("test", data_vacancies)





if __name__ == "__main__":
    main()
