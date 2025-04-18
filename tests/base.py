import unittest

from shopping_basket import ShoppingBasket


first_product = {
    'product_id': 1,
    'name': 'first_product',
}
second_product = {
    'product_id': 2,
    'name': 'second_product',
}


class BaseTestCase(unittest.TestCase):
    """Класс содержит базовые методы для тестирования корзины."""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.first_product = first_product
        self.second_product = second_product

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
        """Метод выполняет поиск товара по product_id"""
        return next(
            (p for p in self.basket.products if p.product_id == product_id),
            None
        )

    def setUp(self):
        self.basket = ShoppingBasket()
        self.add_product_to_basket(self.first_product)
