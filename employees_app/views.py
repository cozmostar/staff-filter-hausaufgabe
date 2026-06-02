from datetime import date
from decimal import Decimal, ROUND_HALF_UP

from django.db.models import Avg, Q
from django.shortcuts import render

from .models import Employee


def employee_overview(request):
    employees = Employee.objects.select_related("department").all().order_by("id")
    employees_over_3000 = Employee.objects.filter(salary__gt=3000).order_by("id")
    employees_5000_or_more_count = Employee.objects.filter(salary__gte=5000).count()

    sales_average = Employee.objects.filter(department__name="Sales").aggregate(
        average_salary=Avg("salary")
    )["average_salary"]
    sales_average_salary = (
        sales_average.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if sales_average is not None
        else Decimal("0.00")
    )

    hired_before_2022_not_hr = Employee.objects.filter(
        Q(hire_date__lt=date(2022, 1, 1)) & ~Q(department__name="HR")
    ).order_by("id")

    context = {
        "employees": employees,
        "employees_over_3000": employees_over_3000,
        "employees_5000_or_more_count": employees_5000_or_more_count,
        "sales_average_salary": sales_average_salary,
        "hired_before_2022_not_hr": hired_before_2022_not_hr,
    }

    return render(request, "employee_list.html", context)
