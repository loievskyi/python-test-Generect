import json
import requests


class APIDataParser(object):
    """Class which grab information about all persons from
    list_of_companies_url using API."""

    def _get_list_of_companies_info(self, list_of_companies_url):
        """
        Method which grab information about all companies from
        list_of_companies_url using API.
        """
        list_of_companies = requests.get(list_of_companies_url).json()
        companies = []
        for company_json in list_of_companies:
            companies.append(self._get_company_info(company_json))
        return companies

    def _get_company_info(self, company_json):
        """
        Method which grab information about the company from company_url.
        """
        company = requests.get(company_json["company_url"]).json()
        return company

    def _get_list_of_persons_url(self, company_json):
        """
        Method which create list_of_persons_url from company_json.
        """
        persons_url = company_json.get("persons_url", None)
        if persons_url:
            return persons_url
        else:
            return f"https://www.linkedin.com/search/results/people/?currentCompany={company['id']}"

    def _get_list_of_persons_info(self, list_of_persons_url, company_id):
        """
        Method which grab information about all persons of the company from
        list_of_persons_url.
        """
        list_of_persons = requests.get(list_of_persons_url).json()
        persons = []
        for person in list_of_persons:
            p = self._get_person_info(person)
            p["company_id"] = company_id
            persons.append(p)
        return persons

    def _get_person_info(self, profile_json):
        """
        Method which grab information about the person from profile_urls.
        """
        person = requests.get(profile_json["profile_url"]).json()
        return person

    def get_persons_info(self, list_of_companies_url):
        """
        Method which grab information about all persons from
        list_of_companies_url.
        """
        companies = self._get_list_of_companies_info(list_of_companies_url)
        persons = []
        for company in companies:
            list_of_persons_url = self._get_list_of_persons_url(company)
            persons += self._get_list_of_persons_info(
                list_of_persons_url, company["id"])
        return persons


def main():
    """
    Main function.
    """
    list_of_companies_url = "http://localhost:8000/api/v1/companies/"
    data_parser = APIDataParser()
    persons_info = data_parser.get_persons_info(list_of_companies_url)
    print(json.dumps(persons_info, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
