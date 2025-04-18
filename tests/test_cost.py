from base import BaseTestCase
from decimal import Decimal


class TestCost(BaseTestCase):
    """Класс тестирует расчёт стоимости корзины."""

    FIRST_PRICE = 1500.50
    SECOND_PRICE = 2787

    def setup_basket(self):
        """Метод добавляет товары в корзину для тестов"""
        self.add_product_to_basket(self.first_product, quantity=2)
        self.add_product_to_basket(
            self.second_product, price=self.SECOND_PRICE
        )

    def base_price(self, discount: int = None) -> Decimal:
        """Метод подготавливает необходимые данные для тестирования
        правильности расчёта общей стоимости корзины.
        """
        total = self.FIRST_PRICE * 3 + self.SECOND_PRICE

        if discount:
            total -= total * discount / 100

        return Decimal(str(total))

    def test_cost_without_discount(self):
        """Проверка того что правильно рассчитывается
        итоговая стоимость товара без скидки.
        """
        self.setup_basket()
        self.assertEqual(self.base_price(), self.basket.total_price())

    def test_cost_with_discount(self):
        """Проверка того что правильно рассчитывается
        итоговая стоимость товара со скидкой.
        """
        self.setup_basket()
        self.assertEqual(self.base_price(10), self.basket.discount_calc(10))

    def test_max_discount(self):
        """Проверяем то что правильно рассчитывается
        итоговая стоимость при максимальной скидке 100%
        """
        self.setup_basket()
        self.assertEqual(Decimal(0), self.basket.discount_calc(100))

    def test_min_discount(self):
        """Проверяем то что правильно рассчитывается
        итоговая стоимость при минимальной скидке 0%
        """
        self.setup_basket()
        self.assertEqual(self.base_price(), self.basket.discount_calc(0))
