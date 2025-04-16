import unittest

from decimal import Decimal
from shopping_basket import ShoppingBasket


first_product = {
    'product_id': 1,
    'name': 'first_product',
}
second_product = {
    'product_id': 2,
    'name': 'second_product',
}


class TestAddProduct(unittest.TestCase):
    """Класс для реализации проверки добавления товара."""

    def add_product_to_basket(
            self, product: dict, quantity: int = 1, price: float = 1500.50
    ):
        """Метод добавляет продукт в корзину."""
        self.basket.add_product(
            product_id=product.get('product_id'),
            name=product.get('name'),
            price=price,
            quantity=quantity
        )

    def get_product(self, product_id: int):
        return next(
            (p for p in self.basket.products if p.product_id == product_id),
            None
        )

    def value_error_add_product(
            self, product: dict, quantity: int = 1, price: int = 1500.50
    ):
        """Базовый метод для проверок на выброс
        исключения при добавлении товара.
        """
        with self.assertRaises(ValueError):
            self.add_product_to_basket(
                product, quantity=quantity, price=price
            )

    def setUp(self):
        self.basket = ShoppingBasket()
        self.add_product_to_basket(first_product)
        self.products = self.get_product(1)

    def test_add_one_product(self):
        """Проверка возможности добавления одного товара."""
        self.assertEqual(
            self.products.product_id, first_product.get('product_id')
        )
        self.assertEqual(self.products.name, first_product.get('name'))
        self.assertEqual(self.products.price, Decimal('1500.50'))
        self.assertEqual(self.products.quantity, 1)

    def test_adding_the_same_product(self):
        """Проверка того, что при добавлении товара с тем же product_id
        увеличивается количество, а не создаётся дубликат
        """
        self.add_product_to_basket(first_product)
        self.assertEqual(self.products.quantity, 2)

    def test_zero_quantity(self):
        """Проверка того, что при добавлении товара
        с нулевым количеством вызывается исключение.
        """
        self.value_error_add_product(first_product, quantity=0)

    def test_negative_quantity(self):
        """Проверка того, что при добавлении товара
        с отрицательным количеством вызывается исключение."""
        self.value_error_add_product(first_product, quantity=-2)

    def test_negative_price(self):
        """Проверка того, что товар не может
        быть добавлен с отрицательной ценой.
        """
        self.value_error_add_product(first_product, price=-1500)

    def test_add_more_one_product(self):
        """Проверяем возможность добавления более одного товара."""
        self.add_product_to_basket(second_product, quantity=1, price=1743)
        self.assertEqual(len(self.basket.products), 2)
        product_one = self.get_product(1)
        product_two = self.get_product(2)
        with self.subTest('first product checks'):
            self.assertEqual(
                product_one.product_id, first_product.get('product_id')
            )
            self.assertEqual(product_one.name, first_product.get('name'))
            self.assertEqual(product_one.quantity, 1)
            self.assertEqual(product_one.price, Decimal('1500.50'))
        with self.subTest('second product cheks'):
            self.assertEqual(
                product_two.product_id, second_product.get('product_id')
            )
            self.assertEqual(product_two.name, second_product.get('name'))
            self.assertEqual(product_two.quantity, 1)
            self.assertEqual(product_two.price, Decimal('1743'))
