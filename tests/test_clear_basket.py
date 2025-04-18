from base import BaseTestCase


class TestClearBasket(BaseTestCase):
    """Класс тестирования полной очистки корзины."""

    def test_clear_basket(self):
        """Проверяем корректность работы полной очистки корзины."""
        self.add_product_to_basket(self.first_product)
        self.add_product_to_basket(self.second_product, price=42, quantity=8)
        self.basket.clear_basket()
        self.assertEqual(self.basket.products, [])
