import requests


class TestDataParser(object):
    """Class which grab information about all persons from
    list_of_companies_url using test json data."""

    @staticmethod
    def _get_test_json(url_type, input_json=None):
        """
        A method that returns test data depending on url_type.
        """
        if input_json is None:
            input_json = dict()

        if url_type == "person_url":
            return {
                "id": input_json.get("id"),
                "full_name": "Joe Doe",
                "job_title": "CEO",
                "profile_url": input_json.get("profile_url", ""),
                "location": "Italy",
                "email": "mail@domain.com",
                "phone_number": "+1-354-489-4804"
            }
        elif url_type == "list_of_persons_url":
            return [{
                "id": 1,
                "full_name": "Joe Doe",
                "profile_url": "https://linkedin.com/in/joedoe"
            },
                {
                "id": 2,
                "full_name": "Mike Tyson",
                "profile_url": "https://linkedin.com/in/mike"
            }]
        elif url_type == "company_url":
            return {
                "id": input_json.get("id"),
                "name": input_json.get("name", ""),
                "company_url": input_json.get("company_url", ""),
                "location": "Italy, Roma",
                "revenue": "$365M"
            }
        elif url_type == "list_of_companies_url":
            return [{
                "id": 1,
                "name": "Apple",
                "company_url": "https://linkedin.com/company/apple"
            },
                {
                "id": 2,
                "name": "Facebook",
                "company_url": "https://linkedin.com/company/facebook"
            }]

    def _get_list_of_companies_info(self, list_of_companies_url):
        """
        Method which grab information about all companies from
        list_of_companies_url using test json.
        """
        # list_of_companies = requests.get(list_of_companies_url).json()
        list_of_companies = self._get_test_json(
            url_type="list_of_companies_url")
        companies = []
        for company_json in list_of_companies:
            companies.append(self._get_company_info(company_json))
        return companies

    def _get_company_info(self, company_json):
        """
        Method which grab information about the company from company_url.
        """
        # company = requests.get(company_json["company_url"]).json()
        company = self._get_test_json("company_url", company_json)
        return company

    def _get_list_of_persons_url(self, company):
        """
        Method which create list_of_persons_url from company_id.
        """
        persons_url = company.get("persons_url", None)
        if persons_url:
            return persons_url
        else:
            return f"https://www.linkedin.com/search/results/people/?currentCompany={company['id']}"

    def _get_list_of_persons_info(self, list_of_persons_url, company_id):
        """
        Method which grab information about all persons of the company from
        list_of_persons_url.
        """
        # list_of_persons = requests.get(list_of_persons_url).json()
        list_of_persons = self._get_test_json("list_of_persons_url")
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
        # person = requests.get(profile_json["profile_url"]).json()
        person = self._get_test_json("person_url", profile_json)
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
    list_of_companies_url = "https://www.linkedin.com/search/results/companies/"
    data_parser = TestDataParser()
    persons_info = data_parser.get_persons_info(list_of_companies_url)
    print(persons_info)


if __name__ == "__main__":
    main()
