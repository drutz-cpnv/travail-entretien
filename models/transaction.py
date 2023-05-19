import datetime
import uuid
from models.product import Product


class Transaction:
    product: Product
    created_at: datetime
    finished: bool = False
    inserted_amount: int

    def __init__(self, inserted_amount: int, now: datetime):
        self.inserted_amount = inserted_amount
        self.uuid = uuid.uuid4()
        self.created_at = now

    def add_product(self, product: Product):
        self.product = product

    def get_formatted_amount(self):
        return

    def __str__(self):
        string = "[Transaction {}]\n - montant inséré: {} CHF\n - transaction débutée le: {}\n - transaction terminée: {}\n - produit: {}"
        return string.format(
            self.uuid.__str__(),
            (self.inserted_amount / 100).__str__(),
            self.created_at.strftime("%x %X"),
            self.finished,
            self.product.__str__()
        )
