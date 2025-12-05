
class Payment:
    def __init__(self, amount):
        self.amount = float(amount)

    def process_payment(self):
        return f"Processing payment of ₹{self.amount:.2f}"


class CreditCardPayment(Payment):
    def __init__(self, amount, card_number, holder_name):
        super().__init__(amount)
        self.card_number = str(card_number)
        self.holder_name = holder_name

    def process_payment(self):
        masked = "*" * (len(self.card_number) - 4) + self.card_number[-4:]
        return f"Charged ₹{self.amount:.2f} to credit card {masked} (Holder: {self.holder_name})"


class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def process_payment(self):
        return f"Paid ₹{self.amount:.2f} via UPI ({self.upi_id})"


if __name__ == "__main__":
    cc = CreditCardPayment(1999.50, "4111111111111111", "Asha")
    upi = UPIPayment(850.00, "asha@upi")

    print(cc.process_payment())
    print(upi.process_payment())
