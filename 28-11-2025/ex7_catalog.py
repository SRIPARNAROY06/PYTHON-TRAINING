
def generate_catalog(input_file="products.txt", output_file="catalog.txt"):
    products = []

    with open(input_file, "r") as file:
        for line in file:
            name, price = line.strip().split()
            products.append((name, price))

    with open(output_file, "w") as file:
        file.write(f"{'Product':<15}{'Price':>10}\n")
        file.write("-" * 25 + "\n")
        for name, price in products:
            file.write(f"{name:<15}{price:>10}\n")

    print(f"Catalog generated successfully in {output_file}.")


with open("products.txt", "w") as f:
    f.write("Laptop 55000\nMouse 800\nKeyboard 1500\nMonitor 12000\n")


generate_catalog()
