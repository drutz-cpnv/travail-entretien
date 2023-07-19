import uuid
from copy import copy
from datetime import datetime
from models.product import Product
from models.transaction import Transaction


class Selecta:
    products: dict[str: Product] = {}
    transactions: list[Transaction] = []
    credit: int = 0
    balance: int = 0
    now: datetime

    def __init__(self, place: str):
        self.uuid = uuid.uuid4()
        self.place = place
        self.now = datetime.now()

    def set_now(self, date: str):
        self.now = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')

    def add_product(self, product: Product):
        self.products[product.code] = copy(product)

    def add_products(self, products: list):
        for product in products:
            self.add_product(product)

    def insert(self, amount: int | float):
        """

        :param amount: Montant insérer dans la machine sous forme d'entier soit la somme divisée par 100
        """
        if type(amount) is float:
            amount = amount * 100
        tr = Transaction(amount, self.now)
        self.transactions.append(tr)
        self.credit += amount

    def get_current_transaction(self):
        if self.transactions[-1].finished:
            t = Transaction(0, self.now)
            self.transactions.append(t)
        return self.transactions[-1]

    def get_change(self):
        print()
        template = "{:.2f} CHF"
        out = template.format(self.credit / 100)
        print(out)
        print()
        return out

    def get_balance(self):
        print()
        template = "{:.2f} CHF"
        out = template.format(self.balance / 100)
        print(out)
        print()
        return out

    def get_transactions(self):
        print()
        out = ""
        for transaction in self.transactions:
            out += transaction.__str__() + "\n"
        print(out)
        print()
        return out

    def status(self):
        print()
        string = "[Machine {}]\n - Emplacement: {}\n - Credit: {} CHF\n - Balance: {} CHF\n - Produits:\n"
        string = string.format(self.uuid, self.place, self.credit, self.balance)
        product_template = "   • [Produit {}] {} \t {} CHF\t Stock: {} \t Emplacement: {}\n"
        for product_key in self.products:
            product = self.products[product_key]
            string += product_template.format(
                product.uuid,
                product.name,
                product.unit_price / 100,
                product.quantity,
                product.code
            )
        print(string)
        print()
        return string

    def choose(self, code: str):
        """

        :param code: Code représentant l'emplacement du produit désiré
        """
        if code not in self.products.keys():
            print("Invalid selection!")
            return "Invalid selection!"
        product = self.products[code]
        if self.credit < product.unit_price:
            print("Not enough money!")
            return "Not enough money!"
        if product.quantity == 0:
            print(f'Item {product.name}: Out of stock!')
            return f'Item {product.name}: Out of stock!'

        self.get_current_transaction().inserted_amount = self.credit
        return self.make_transaction(product, self.get_current_transaction())

    def make_transaction(self, product: Product, transaction: Transaction):
        transaction.product = product
        product.quantity -= 1
        self.credit -= product.unit_price
        self.balance += product.unit_price
        transaction.finished = True
        print(f'Vending {product.__str__()}')
        return f'Vending {product.__str__()}'

    def finish_transaction(self):
        if self.get_current_transaction():
            transaction = self.get_current_transaction()
            transaction.finished = True
            string = "[Transaction {}] Terminée\nMontant retourné: {} CHF"
            print(string.format(transaction.uuid, self.credit))
            self.credit = 0
            return string.format(transaction.uuid, self.credit)

    def get_transactions_hours_by_hours(self):
        print()
        groups: dict = {}
        for tr in self.transactions:
            key = f'H{tr.created_at.strftime("%H")}'
            if key not in groups.keys():
                groups[key] = tr.product.unit_price
            else:
                groups[key] = tr.product.unit_price + groups[key]
        sorted_dict = dict(sorted(groups.items(), key=lambda x: x[1], reverse=True)[0:3])
        for hour in sorted_dict:
            value = sorted_dict[hour]
            template = "{} generated a revenue of {:.2f} CHF"
            print(template.format(hour, value / 100))
            return template.format(hour, value / 100)
        print()
