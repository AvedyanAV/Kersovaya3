import requests

class HHEmployerAPI():
    """Класс для работы с api hh"""

    BASE_URL = "https://api.hh.ru"

    def get_employer(self, company_name: str, only_with_vacancies: bool = True):
        """Функция для поиска компании по ее названию"""

        url = f"{self.BASE_URL}/employers"

        params = {
            "text": company_name,
            "only_with_vacancies": only_with_vacancies
        }

        company = requests.get(url, params=params, timeout=10)
        company.raise_for_status()
        data = company.json()

        if "items" not in data or not data["items"]:
            print(f"Компании по запросу '{company_name}' не найдены.")
            return []

        companies = []

        for company in data["items"]:
            company_info = {
                "id": company.get("id"),
                "name": company.get("name"),
                "open_vacancies": company.get("open_vacancies", 0),
            }
            companies.append(company_info)

        return companies


    def get_vacancies(self, employer_id: str, only_with_salary: bool = True):
        """Функция для поиска вакансии по id компании"""

        url = f"{self.BASE_URL}/vacancies"
        all_vacancies = []

        params = {
            "employer_id": employer_id
        }
        if only_with_salary:
            params["only_with_salary"] = True

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "items" not in data or not data["items"]:
               print(f"Вакансии не найдены.")
               return []

        for vacancy in data["items"]:
            company_info = {
                "company_name": vacancy.get("employer").get("name"),
                "vacancy": vacancy.get("name"),
                "salary": vacancy.get("salary").get("from"),
                "url": vacancy.get("alternate_url")
            }
            all_vacancies.append(company_info)

        return all_vacancies
