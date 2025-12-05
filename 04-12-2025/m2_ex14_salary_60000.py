def filter_salary_above(employees: dict, threshold: int = 60000):
    return {
        name: data
        for name, data in employees.items()
        if isinstance(data, dict) and data.get("salary", 0) > threshold
    }

# Example
employees = {
    "Asha": {"salary": 72000, "dept": "IT"},
    "Ravi": {"salary": 58000, "dept": "HR"},
    "Imran": {"salary": 90000, "dept": "Sales"},
}
print(filter_salary_above(employees))

