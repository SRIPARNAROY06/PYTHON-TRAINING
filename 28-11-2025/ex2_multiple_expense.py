def expense_report(expenses):
    """
    expenses: list of tuples(item, amount)
    """
    report_lines=[]
    report_lines.append("EXPENSE REPORT\n")
    total=0

    for item,amount in expenses:
        report_lines.append(f"Item: {item} Amount: {amount} \n")
        total+=amount

    report_lines.append(f"TOTAL EXPENSE REPORT: {total} \n")

    with open("report.txt","w") as f:
        f.writelines(report_lines)
    print("Report created")

expenses_list=[
        ("Groceries",1200),
        ("Milk",100),
        ("Electricity Bill", 950)
    ]

expense_report(expenses_list)
