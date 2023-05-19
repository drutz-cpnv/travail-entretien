import uuid


class Product:
    def __init__(self, code: str, name: str, quantity: int = 0, unit_price: int | float = 100):
        if type(unit_price) is float:
            unit_price = unit_price * 100
        self.uuid = uuid.uuid4()
        self.unit_price: int = unit_price
        self.quantity = quantity
        self.name = name
        self.code = code

    def __str__(self):
        string = "{}: {:.2f} CHF"
        return string.format(self.name, self.unit_price / 100)
