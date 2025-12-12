from src.hh_api import HHEmployerAPI

if __name__ == "__main__":
    api = HHEmployerAPI()

    companies = api.get_employer("АльфаБанк")
    print(companies)
    vacancy = api.get_vacancies(companies[0]["id"])
    print(vacancy)
