import datetime
from employees_app.models import Department, Employee

# Departments
sales, _ = Department.objects.get_or_create(name="Sales")
engineering, _ = Department.objects.get_or_create(name="Engineering")
hr, _ = Department.objects.get_or_create(name="HR")
marketing, _ = Department.objects.get_or_create(name="Marketing")

# Employees
employees = [
    ("Max Müller", 3200.00, sales, datetime.date(2021, 3, 1)),
    ("Anna Schmidt", 2800.00, engineering, datetime.date(2022, 7, 10)),
    ("Clara Wagner", 4100.00, sales, datetime.date(2020, 6, 15)),
    ("David Fischer", 5000.00, engineering, datetime.date(2019, 1, 20)),
    ("Emma Becker", 2300.00, hr, datetime.date(2023, 1, 5)),
    ("Frank Zimmermann", 3900.00, marketing, datetime.date(2021, 11, 11)),
    ("Greta Meier", 3100.00, sales, datetime.date(2023, 8, 8)),
    ("Henry Schneider", 2700.00, hr, datetime.date(2022, 2, 2)),
]

for name, salary, department, hire_date in employees:
    Employee.objects.update_or_create(
        name=name,
        defaults={
            "salary": salary,
            "department": department,
            "hire_date": hire_date,
        },
    )
