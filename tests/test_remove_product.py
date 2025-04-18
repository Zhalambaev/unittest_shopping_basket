from base import BaseTestCase


class TestRemoveProduct(BaseTestCase):
    """Класс для тестирования возможности удаления объектов из корзины."""

    def test_quantity_product_remove(self):
        """Проверяем, что при удалении части товара его
        количество уменьшается на заданное число.
        """
        self.add_product_to_basket(self.first_product)
        product = self.get_product(1)
        self.assertEqual(product.quantity, 2)
        self.basket.remove_product(product_id=1, quantity_remove=1)
        self.assertEqual(product.quantity, 1)

    def test_product_remove_if_quantity_zero(self):
        """Проверяем, что товар удаляется из корзины,
        если его остаток в корзине после удаления равен нулю или меньше.
        """
        product = self.get_product(1)
        self.assertEqual(product.quantity, 1)
        self.basket.remove_product(product_id=1, quantity_remove=10)
        self.assertNotIn(product, self.basket.products)

    def test_value_error(self):
        """Проверяем, что при попытке удалить несуществующий
        товар вызывается исключение
        """
        with self.assertRaises(ValueError):
            self.basket.remove_product(product_id=42)
