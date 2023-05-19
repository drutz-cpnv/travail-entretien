from models.product import Product
from models.selecta import Selecta

init_products = [
    Product(code='A01', name='Smarlies', quantity=100, unit_price=1.60),
    Product(code='A02', name='Carampar', quantity=50, unit_price=0.60),
    Product(code='A03', name='Acril', quantity=20, unit_price=2.10),
    Product(code='A04', name='KokoKola', quantity=10, unit_price=2.95),
]

selecta: Selecta = Selecta(place="Yverdon, gare voie B")
selecta.add_products(init_products)

selecta.set_now("2020-01-01T20:30:00")
selecta.insert(1000.00)
selecta.choose('A01')
selecta.set_now("2020-03-01T23:30:00")
selecta.choose('A01')
selecta.set_now("2020-03-04T09:22:00")
selecta.choose('A01')
selecta.set_now("2020-04-01T23:00:00")
selecta.choose('A01')
selecta.set_now("2020-04-01T23:59:59")
selecta.choose('A01')
selecta.set_now("2020-04-04T09:12:00")
selecta.choose('A01')

selecta.get_transactions_hours_by_hours()
