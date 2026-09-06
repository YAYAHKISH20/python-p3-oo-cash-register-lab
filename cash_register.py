class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
 
    @property
    def discount(self):
        return self._discount
 
    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0
 
    def add_item(self, item, price, quantity):
        self.items.append({"item": item, "price": price, "quantity": quantity})
        self.total += price * quantity
        print(f"Added {quantity} x {item} at ${price:.2f} each. "
              f"New total: ${self.total:.2f}")
 
    def apply_discount(self):
        if not self.items:
            print("There are no items to apply a discount to.")
            return
 
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
 
        print(f"Discount of {self.discount}% applied. "
              f"You saved ${discount_amount:.2f}. "
              f"New total: ${self.total:.2f}")
 
    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return
 
        last_transaction = self.previous_transactions.pop()
        print(f"Voided transaction: {last_transaction}")
 
    def checkout(self):
        if not self.items:
            print("No items to check out.")
            return
 
        self.previous_transactions.append({
            "items": self.items,
            "total": self.total,
        })
 
        print(f"Transaction complete. Total charged: ${self.total:.2f}")
 
        self.items = []
        self.total = 0
 
 
if __name__ == "__main__":
    register = CashRegister(discount=20)
 
    register.add_item("Coffee", 4.50, 2)
    register.add_item("Muffin", 3.00, 1)
    register.apply_discount()
    register.checkout()
 
    register.void_last_transaction()
 
    register2 = CashRegister(discount=150)
