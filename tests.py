import unittest

from shopping_basket import ShoppingBasket


class TestInitialization(unittest.TestCase):
    """Класс проверяет корректность инициализации корзины."""

    def setUp(self):
        self.basket = ShoppingBasket()

    def test_empty_basket(self):
        """Метод тестирует то, что корзина создаётся пустой."""
        self.assertEqual(self.basket.products, [])


unittest.main()
