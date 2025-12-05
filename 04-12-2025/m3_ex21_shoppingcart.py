
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, name, price, qty=1):
        if name in self.items:
            self.items[name]["qty"] += qty
            self.items[name]["price"] = price
        else:
            self.items[name] = {"price": price, "qty": qty}
        print(f"Added {qty} x {name} at ₹{price} each.")

    def remove(self, name, qty=None):
        if name not in self.items:
            print(f"{name} not found in cart.")
            return
        if qty is None or qty >= self.items[name]["qty"]:
            del self.items[name]
            print(f"Removed {name} from cart.")
        else:
            self.items[name]["qty"] -= qty
            print(f"Removed {qty} of {name}. Remaining: {self.items[name]['qty']}")

    def total(self):
        total_amount = sum(d["price"] * d["qty"] for d in self.items.values())
        print(f"Total amount: ₹{total_amount:.2f}")
        return total_amount

    def apply_discount(self, percent=None, fixed=None):
        total_amount = self.total()
        if percent is not None:
            discounted = total_amount * (1 - percent / 100)
            print(f"Applied {percent}% discount. New total: ₹{discounted:.2f}")
        elif fixed is not None:
            discounted = total_amount - fixed
            print(f"Applied ₹{fixed} discount. New total: ₹{discounted:.2f}")
        else:
            discounted = total_amount
        return discounted


# ---- Example Usage ----
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add("Keyboard", 1499, 1)
    cart.add("Mouse", 599, 2)
    cart.add("Headset", 1999, 1)

    cart.total()
    cart.apply_discount(percent=10)
    cart.apply_discount(fixed=500)

    cart.remove("Mouse", 1)
    cart.total()
    cart.remove("Headset")
