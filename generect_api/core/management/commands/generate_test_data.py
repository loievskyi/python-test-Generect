import random

from django.core.management.base import BaseCommand

from core.models import Company, Person


class Command(BaseCommand):
    """Command for generating test data: 10  companies and 100 persons"""
    help = "Generates 10 test companies and 100 persons."

    names = (
        "Liam",
        "Noah",
        "Oliver",
        "William",
        "Elijah",
        "James",
        "Benjamin",
        "Lucas",
        "Mason",
        "Ethan",
        "Olivia",
        "Emma",
        "Ava",
        "Sophia",
        "Isabella",
        "Charlotte",
        "Amelia",
        "Mia",
        "Harper",
        "Evelyn",
    )

    def handle(self, *args, **kwargs):
        total_companies = 10
        total_persons = 100
        companies = []
        persons = []

        try:

            for num_company in range(1, total_companies+1):
                company = self._generate_company(f"Company-{str(num_company)}")
                companies.append(company)
            companies = Company.objects.bulk_create(companies, batch_size=100)

            companies = Company.objects.only("id")
            for num_person in range(1, total_persons+1):
                persons.append(self._generate_person(random.choice(companies)))
            Person.objects.bulk_create(persons, batch_size=100)

        except Exception as ex:
            self.stdout.write(self.style.ERROR(f"An error has occurred: {ex}"))
        else:
            self.stdout.write(self.style.SUCCESS(
                f"Successfully created {total_companies} companies and "
                f"{total_persons} persons"))

    def _generate_person(self, company):
        """Method for generating Person object."""
        return Person(
            full_name=random.choice(self.names),
            job_title="test_title",
            location="test_location",
            email="email@example.com",
            phone_number="1234567890",
            company=company
        )

    def _generate_company(self, name):
        """Method for generating Company object."""
        return Company(
            name=name,
            location="test_location",
            revenue=random.randint(0, 10000)
        )
