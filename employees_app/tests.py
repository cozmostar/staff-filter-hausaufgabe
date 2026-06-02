from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Department, Employee


class EmployeeOverviewViewTest(TestCase):
    def setUp(self):
        sales = Department.objects.create(name="Sales")
        engineering = Department.objects.create(name="Engineering")
        hr = Department.objects.create(name="HR")
        marketing = Department.objects.create(name="Marketing")

        Employee.objects.create(name="Max Müller", salary=3200, department=sales, hire_date=date(2021, 3, 1))
        Employee.objects.create(name="Anna Schmidt", salary=2800, department=engineering, hire_date=date(2022, 7, 10))
        Employee.objects.create(name="Clara Wagner", salary=4100, department=sales, hire_date=date(2020, 6, 15))
        Employee.objects.create(name="David Fischer", salary=5000, department=engineering, hire_date=date(2019, 1, 20))
        Employee.objects.create(name="Emma Becker", salary=2300, department=hr, hire_date=date(2023, 1, 5))
        Employee.objects.create(name="Frank Zimmermann", salary=3900, department=marketing, hire_date=date(2021, 11, 11))
        Employee.objects.create(name="Greta Meier", salary=3100, department=sales, hire_date=date(2023, 8, 8))
        Employee.objects.create(name="Henry Schneider", salary=2700, department=hr, hire_date=date(2022, 2, 2))

    def test_employee_overview_filters_and_aggregates_staff_data(self):
        response = self.client.get(reverse("employee_overview"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["employees"]), 8)
        self.assertEqual(
            list(response.context["employees_over_3000"].values_list("name", flat=True)),
            ["Max Müller", "Clara Wagner", "David Fischer", "Frank Zimmermann", "Greta Meier"],
        )
        self.assertEqual(response.context["employees_5000_or_more_count"], 1)
        self.assertEqual(response.context["sales_average_salary"], Decimal("3466.67"))
        self.assertEqual(
            list(response.context["hired_before_2022_not_hr"].values_list("name", flat=True)),
            ["Max Müller", "Clara Wagner", "David Fischer", "Frank Zimmermann"],
        )

    def test_employee_overview_renders_filter_results(self):
        response = self.client.get(reverse("employee_overview"))
        content = response.content.decode("utf-8")

        self.assertIn("Max Müller", content)
        self.assertIn("Sales", content)
        self.assertIn("Mitarbeiter mit mehr als 3000", content)
        self.assertIn("Anzahl Mitarbeiter mit 5000", content)
        self.assertIn("3466,67", content)
        self.assertIn("vor dem 1. Januar 2022", content)
        self.assertIn("1. März 2021", content)

    def test_root_redirects_to_employee_overview(self):
        response = self.client.get("/")

        self.assertRedirects(response, reverse("employee_overview"), fetch_redirect_response=False)
