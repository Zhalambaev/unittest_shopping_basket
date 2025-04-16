import unittest

from shopping_basket import ShoppingBasket


first_product = {
    'product_id': 1,
    'name': 'first_product',
    'price': 1500.50,
    'quantity': 1
}
second_product = {
    'product_id': 2,
    'name': 'second_product',
    'price': 2137,
    'quantity': 1
}


class TestAddProduct(unittest.TestCase):
    """Класс для реализации проверки добавления товара."""

    def setUp(self):
        self.basket = ShoppingBasket()

    def test_add_one_product(self):
        """Проверка возможности добавления одного товара."""
        self.basket.add_product(
            product_id=first_product.get('product_id'),
            name=first_product.get('name'),
            price=first_product.get('price'),
            quantity=first_product.get('quantity')
        )
        products = self.basket.products
        self.assertNotEqual(products, [])
