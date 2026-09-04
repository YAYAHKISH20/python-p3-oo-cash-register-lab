class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0
        self.last_transaction_count = 0

    def format_money(self, amount):
        amount = round(amount, 2)
        if amount == int(amount):
            return str(int(amount))
        return str(amount)

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
        item_total = price * quantity
        self.total += item_total
        self.last_transaction_amount = item_total
        self.last_transaction_count = quantity

    def apply_discount(self):
        if self.discount:
            self.total = self.total - (self.total * self.discount / 100)
            print("After the discount, the total comes to $" + self.format_money(self.total) + ".")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        for _ in range(self.last_transaction_count):
            if self.items:
                self.items.pop()
        self.last_transaction_amount = 0
        self.last_transaction_count = 0
        if not self.items:
            self.total = 0
