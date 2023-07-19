import unittest

from models.product import Product
from models.selecta import Selecta

tests_initial_products = [
    Product(code='A01', name='Smarlies', quantity=10, unit_price=1.60),
    Product(code='A02', name='Carampar', quantity=5, unit_price=0.60),
    Product(code='A03', name='Avril', quantity=2, unit_price=2.10),
    Product(code='A04', name='KokoKola', quantity=1, unit_price=2.95),
]


def get_machine() -> Selecta:
    s = Selecta(place="Yverdon-les-Bains, gare, voie 1")
    s.add_products(tests_initial_products)
    return s


class MainTest(unittest.TestCase):

    def test_1(self):
        selecta = get_machine()
        selecta.insert(3.40)
        self.assertEqual(selecta.choose("A01"), 'Vending Smarlies')
        self.assertEqual(selecta.get_change(), '1.80 CHF')

    def test_2(self):
        selecta = get_machine()
        selecta.insert(2.10)
        self.assertEqual(selecta.choose("A03"), 'Vending Avril')
        self.assertEqual(selecta.get_change(), '0.00 CHF')
        self.assertEqual(selecta.get_balance(), '2.10 CHF')

    def test_3(self):
        selecta = get_machine()
        self.assertEqual(selecta.choose("A03"), 'Not enough money!')

    def test_4(self):
        selecta = get_machine()
        selecta.insert(1.00)
        self.assertEqual(selecta.choose("A01"), 'Not enough money!')
        self.assertEqual(selecta.get_change(), '1.00 CHF')
        self.assertEqual(selecta.choose("A02"), 'Vending Carampar')
        self.assertEqual(selecta.get_change(), '0.40 CHF')

    def test_5(self):
        selecta = get_machine()
        self.assertEqual(selecta.choose("A05"), 'Invalid selection!')

    def test_6(self):
        selecta = get_machine()
        selecta.insert(6.00)
        self.assertEqual(selecta.choose("A04"), 'Vending KokoKola')
        self.assertEqual(selecta.choose("A04"), 'Item KokoKola: Out of stock!')
        self.assertEqual(selecta.get_change(), '3.05 CHF')

    def test_7(self):
        selecta = get_machine()
        selecta.insert(6.00)
        self.assertEqual(selecta.choose("A04"), 'Vending KokoKola')
        selecta.insert(6.00)
        self.assertEqual(selecta.choose("A04"), 'Item KokoKola: Out of stock!')
        self.assertEqual(selecta.choose("A01"), 'Vending Smarlies')
        self.assertEqual(selecta.choose("A02"), 'Vending Carampar')
        self.assertEqual(selecta.choose("A02"), 'Vending Carampar')
        self.assertEqual(selecta.get_change(), '6.25 CHF')
        self.assertEqual(selecta.get_balance(), '5.75 CHF')


if __name__ == '__main__':
    unittest.main()
