from models.product import Product
from models.selecta import Selecta

if __name__ == '__main__':
    # global current_date_time
    init_products = [
        Product(code='A01', name='Smarlies', quantity=10, unit_price=1.60),
        Product(code='A02', name='Carampar', quantity=5, unit_price=0.60),
        Product(code='A03', name='Acril', quantity=2, unit_price=2.10),
        Product(code='A04', name='KokoKola', quantity=1, unit_price=2.95),
    ]

    selecta: Selecta = Selecta(place="Yverdon, gare voie B")
    selecta.add_products(init_products)

    selecta.insert(8.00)
    selecta.choose('A02')
    selecta.choose('A04')
    selecta.choose('A04')
    selecta.get_transactions()
    selecta.status()
    selecta.get_transactions_hours_by_hours()
