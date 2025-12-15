import os
from dotenv import load_dotenv
from src.hh_api import HHEmployerAPI
from src.dbmanager import DBmanager

load_dotenv()
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

def main():
    """Основная функция"""

    api = HHEmployerAPI()

    print("Выберите компанию из списка: ")
    print("1.Яндекс", "2.АльфаБанк", "3.Магнит", "4.DNS", "5.Emex",
          "6.Ростелеком", "7.Т-Банк", "8.VK", "9.HH", "10.585 Золотой", sep="\n")

    choice = input(f"Ведите номер компании: ").strip()

    if choice == '1':
        input_companies = "Яндекс"
    elif choice == '2':
        input_companies = "АльфаБанк"
    elif choice == '3':
        input_companies = "МАГНИТ, Розничная сеть"
    elif choice == '4':
        input_companies = "Сеть магазинов цифровой и бытовой техники DNS"
    elif choice == '5':
        input_companies = "EMEX"
    elif choice == '6':
        input_companies = "Ростелеком"
    elif choice == '7':
        input_companies = "Т-Банк"
    elif choice == '8':
        input_companies = "VK"
    elif choice == '9':
        input_companies = "HH"
    elif choice == '10':
        input_companies = "585, Золотой"

    companies = api.get_employer(input_companies)[0]
    print("Компания")
    print(companies)

    vacancies = api.get_vacancies(companies['id'])
    print("Список вакансии")
    print(vacancies)


if __name__ == "__main__":
    main()
