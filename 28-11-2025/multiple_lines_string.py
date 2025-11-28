def write_employee_record(emp_id,name,salary):
    record=f"""
    Employee Record
    ID: {emp_id}
    Name: {name}
    Salary: {salary}
    """
    with open("employee.txt","w") as f:
        f.write(record)

write_employee_record(101,"Aman",750000)
