from base import BaseTestCase
from decimal import Decimal


class TestAddProduct(BaseTestCase):
    """Класс для реализации проверки добавления товара."""

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

    def test_add_one_product(self):
        """Проверка возможности добавления одного товара."""
        product = self.get_product(1)
        self.assertEqual(
            product.product_id, self.first_product.get('product_id')
        )
        self.assertEqual(product.name, self.first_product.get('name'))
        self.assertEqual(product.price, Decimal('1500.50'))
        self.assertEqual(product.quantity, 1)

    def test_adding_the_same_product(self):
        """Проверка того, что при добавлении товара с тем же product_id
        увеличивается количество, а не создаётся дубликат
        """
        self.add_product_to_basket(self.first_product)
        product = self.get_product(1)
        self.assertEqual(product.quantity, 2)

    def test_zero_quantity(self):
        """Проверка того, что при добавлении товара
        с нулевым количеством вызывается исключение.
        """
        self.value_error_add_product(self.first_product, quantity=0)

    def test_negative_quantity(self):
        """Проверка того, что при добавлении товара
        с отрицательным количеством вызывается исключение."""
        self.value_error_add_product(self.first_product, quantity=-2)

    def test_negative_price(self):
        """Проверка того, что товар не может
        быть добавлен с отрицательной ценой.
        """
        self.value_error_add_product(self.first_product, price=-1500)

    def test_add_more_one_product(self):
        """Проверяем возможность добавления более одного товара."""
        self.add_product_to_basket(self.second_product, quantity=1, price=1743)
        self.assertEqual(len(self.basket.products), 2)
        product_one = self.get_product(1)
        product_two = self.get_product(2)
        with self.subTest('first product checks'):
            self.assertEqual(
                product_one.product_id, self.first_product.get('product_id')
            )
            self.assertEqual(product_one.name, self.first_product.get('name'))
            self.assertEqual(product_one.quantity, 1)
            self.assertEqual(product_one.price, Decimal('1500.50'))
        with self.subTest('second product cheks'):
            self.assertEqual(
                product_two.product_id, self.second_product.get('product_id')
            )
            self.assertEqual(product_two.name, self.second_product.get('name'))
            self.assertEqual(product_two.quantity, 1)
            self.assertEqual(product_two.price, Decimal('1743'))
