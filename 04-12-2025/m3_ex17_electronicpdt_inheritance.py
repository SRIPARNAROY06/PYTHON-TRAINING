class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = float(price)

    def final_price(self, tax_rate=0.0):
        """Return price after applying tax_rate (e.g., 0.18 for 18%)."""
        return round(self.price * (1 + tax_rate), 2)

    def info(self):
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price:.2f})"


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, warranty_years=1):
        # Call base class constructor
        super().__init__(product_id, name, price)
        self.warranty_years = int(warranty_years)

    def info(self):
        # Extend the base `info` with warranty
        base = super().info()
        return f"{base}, warranty={self.warranty_years} year(s)"


# ---- Example Usage ----
if __name__ == "__main__":
    p = Product("P001", "Notebook", 199.99)
    e = ElectronicProduct("E101", "Smartphone", 29999, warranty_years=2)

    print(p.info())
    print("Final price with 18% tax:", p.final_price(0.18))
    print(e.info())