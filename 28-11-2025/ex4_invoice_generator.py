
import csv
import os

def create_orders_and_invoice():
    # Step 1: Create orders.csv with sample data
    orders_file = "orders.csv"
    sample_orders = [
        {"item": "Pen", "quantity": 10, "price": 5},
        {"item": "Notebook", "quantity": 5, "price": 20},
        {"item": "Eraser", "quantity": 2, "price": 3},
        {"item": "Marker", "quantity": 4, "price": 8}
    ]

    with open(orders_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["item", "quantity", "price"])
        writer.writeheader()
        writer.writerows(sample_orders)

    print(f"{orders_file} created successfully with sample data.")

    # Step 2: Generate invoice.txt from orders.csv
    invoice_file = "invoice.txt"
    total = 0
    lines = []

    with open(orders_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            item = row["item"]
            quantity = int(row["quantity"])
            price = float(row["price"])
            cost = quantity * price
            total += cost
            lines.append(f"{item}\t{quantity}\t{price:.2f}\t{cost:.2f}")

    with open(invoice_file, "w") as inv_file:
        inv_file.write("INVOICE\n\n")
        inv_file.write("Item\tQty\tPrice\tCost\n")
        inv_file.write("-" * 40 + "\n")
        for line in lines:
            inv_file.write(line + "\n")
        inv_file.write("-" * 40 + "\n")
        inv_file.write(f"Total Amount: {total:.2f}\n")

    print(f"Invoice generated successfully in {invoice_file}.")

# Run the function
create_orders_and_invoice()
