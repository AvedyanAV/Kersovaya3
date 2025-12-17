import requests


class HHEmployerAPI:
    """Класс для работы с api hh"""

    BASE_URL = "https://api.hh.ru"

    def get_employer(
        self, company_name: str, only_with_vacancies: bool = True, limit: int = 1
    ):
        """Функция для поиска компании по ее названию"""

        url = f"{self.BASE_URL}/employers"

        params = {
            "text": company_name,
            "only_with_vacancies": only_with_vacancies,
            "per_page": limit,
        }

        company = requests.get(url, params=params, timeout=10)
        company.raise_for_status()
        data = company.json()

        for company in data["items"][:limit]:
            company = {
                "id": company.get("id"),
                "name": company.get("name"),
                "open_vacancies": company.get("open_vacancies", 0),
            }

        return company

    def get_vacancies(self, employer_id: str, only_with_salary: bool = True):
        """Функция для поиска вакансии по id компании"""

        url = f"{self.BASE_URL}/vacancies"
        all_vacancies = []

        params = {"employer_id": employer_id}
        if only_with_salary:
            params["only_with_salary"] = True

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        for vacancy in data["items"]:
            company_info = {
                "id_company": vacancy.get("employer", {}).get("id"),
                "id_vacancy": vacancy.get("id"),
                "company_name": vacancy.get("employer").get("name"),
                "vacancy": vacancy.get("name"),
                "salary_from": vacancy.get("salary").get("from"),
                "salary_to": vacancy.get("salary").get("to"),
                "url": vacancy.get("alternate_url"),
            }
            all_vacancies.append(company_info)

        return all_vacancies
