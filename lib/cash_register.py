class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self._last_item_total = 0
 
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
 
    def add_item(self, title, price, quantity=1):
        self.items += [title] * quantity
        item_total = price * quantity
        self.total += item_total
        self._last_item_total = item_total
 
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            total_display = int(self.total) if self.total == int(self.total) else self.total
            print(f"After the discount, the total comes to ${total_display}.")
        else:
            print("There is no discount to apply.")
 
    def void_last_transaction(self):
        self.total -= self._last_item_total
        self._last_item_total = 0