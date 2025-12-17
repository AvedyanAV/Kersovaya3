import os

from dotenv import load_dotenv

from src.dbmanager import DBAdd
from src.hh_api import HHEmployerAPI
from src.db_request import DBManager

load_dotenv()
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

params = {"host": DATABASE_HOST, "user": DATABASE_USER, "password": DATABASE_PASSWORD}


def main():
    """Основная функция"""

    api = HHEmployerAPI()
    db = DBAdd(params)
    db_manager = DBManager(params)

    data_employ = []
    data_vacancies = []

    print("Список компании для проверки работы программы")
    print(
        "1.Яндекс",
        "2.АльфаБанк",
        "3.Магнит",
        "4.DNS",
        "5.Emex",
        "6.Ростелеком",
        "7.Т-Банк",
        "8.VK",
        "9.HH",
        "10.585 Золотой",
        sep="\n"
    )

    employ = [
        "Яндекс",
        "АльфаБанк",
        "МАГНИТ, Розничная сеть",
        "DNS",
        "Emex",
        "Ростелеком",
        "Т-Банк",
        "VK",
        "HH",
        "585 Золотой",
    ]
    for i in employ:
        companies = api.get_employer(i)
        data_employ.append(companies)

        vacancies = api.get_vacancies(companies["id"])
        data_vacancies.append(vacancies)
    print("Данные успешно получены")

    db.add_db("test")
    db.create_tables("test")
    db.save_data_employers("test", data_employ)
    db.save_data_vacancies("test", data_vacancies)

    print("\nПользователю доступны взаимодействие с данными таблиц")
    print("1.Поиск вакансии по заданному слову")
    print("2.Получить список компаний и количество вакансий у каждой компании")
    print("3.Получить список всех вакансии")
    print("4.Получить среднюю зарплату по вакансиям")
    print("5.Получить список всех вакансий, у которых зарплата выше средней")

    choice = input("\nВыберите действие (1-5): ").strip()
    if choice == '1':
        words = input("Ведите слова для поиска: ")
        db_manager.get_vacancies_with_keyword("test", words)

    elif choice == '2':
        db_manager.get_companies_and_vacancies_count("test")

    elif choice == "3":
        db_manager.get_all_vacancies("test")

    elif choice == "4":
        db_manager.get_avg_salary("test")

    elif choice == "5":
        db_manager.get_vacancies_with_higher_salary("test")


if __name__ == "__main__":
    main()
