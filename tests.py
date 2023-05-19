from models.product import Product
from models.selecta import Selecta

tests_initial_products = [
    Product(code='A01', name='Smarlies', quantity=10, unit_price=1.60),
    Product(code='A02', name='Carampar', quantity=5, unit_price=0.60),
    Product(code='A03', name='Acril', quantity=2, unit_price=2.10),
    Product(code='A04', name='KokoKola', quantity=1, unit_price=2.95),
]


def get_test_machine():
    s = Selecta(place="Yverdon-les-Bains, gare, voie 1")
    s.add_products(tests_initial_products)
    return s


print()
print("// TEST CASE 1")
print()

selecta_test1 = get_test_machine()
selecta_test1.insert(3.40)
selecta_test1.choose("A01")
selecta_test1.get_change()

print()
print()
print("// TEST CASE 2")
print()

selecta_test2 = get_test_machine()
selecta_test2.insert(2.10)
selecta_test2.choose("A03")
selecta_test2.get_change()
selecta_test2.get_balance()

print()
print()
print("// TEST CASE 3")
print()

selecta_test3 = get_test_machine()
selecta_test3.choose("A01")

print()
print()
print("// TEST CASE 4")
print()

selecta_test4 = get_test_machine()
selecta_test4.insert(1.00)
selecta_test4.choose("A01")
selecta_test4.get_change()
selecta_test4.choose("A02")
selecta_test4.get_change()

print()
print()
print("// TEST CASE 5")
print()

selecta_test5 = get_test_machine()
selecta_test5.insert(1.00)
selecta_test5.choose("A05")

print()
print()
print("// TEST CASE 6")
print()

selecta_test6 = get_test_machine()
selecta_test6.insert(6.00)
selecta_test6.choose("A04")
selecta_test6.choose("A04")
selecta_test6.get_change()

print()
print()
print("// TEST CASE 7")
print()

selecta_test7 = get_test_machine()
selecta_test7.insert(6.00)
selecta_test7.choose("A04")
selecta_test7.insert(6.00)
selecta_test7.choose("A04")
selecta_test7.choose("A01")
selecta_test7.choose("A02")
selecta_test7.choose("A02")
selecta_test7.get_change()
selecta_test7.get_balance()
