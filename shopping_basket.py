from dataclasses import dataclass
from decimal import Decimal
from typing import Union


@dataclass
class Product:
    product_id: int
    name: str
    price: Decimal
    quantity: int


class ShoppingBasket:
    """Класс имитирует корзину в интернет-магазине."""
    def __init__(self):
        self.products: list[Product] = []

    def to_decimal(self, data: Union[int, float, str]) -> Decimal:
        """Метод преобразует данные в данные типа Decimal."""
        if isinstance(data, float):
            return Decimal(str(data))
        return Decimal(data)

    def add_product(
            self, product_id: int, name: str, price: Union[int, float, str], quantity: int
    ):
        """Метод добавляет товар в корзину."""
        for product in self.products:
            if product.product_id == product_id:
                product.quantity += quantity
                return
        self.products.append(Product(product_id, name, self.to_decimal(price), quantity))

    def remove_product(self, product_id: int, quantity_remove: int = None):
        """Метод удаляет товар из корзины, если он там есть."""
        new_products = []

        for product in self.products:
            if product.product_id == product_id:
                if quantity_remove is None or quantity_remove >= product.quantity:
                    continue
                else:
                    product.quantity -= quantity_remove
            new_products.append(product)
        
        self.products = new_products


    def total_price(self) -> Decimal:
        """Метод рассчитывает общую стоимость всех товаров в корзине."""
        return sum((p.price * p.quantity for p in self.products), Decimal(0))

    def discount_calc(self, discount: Union[int, str] = 0) -> Decimal:
        """Метод рассчитывает итоговую стоимость с учётом скидки.
        Максимальная скидка может быть 100%, минимальная — 0.
        Скидка применяется к общей стоимости всех товаров в корзине.
        """
        max_discount = 100
        min_discount = 0

        try:
            discount_int = int(discount)
        except (ValueError, TypeError):
            raise ValueError(
                'Скидка должна быть целым числом '
                f'от {min_discount} до {max_discount}.'
            )

        if min_discount <= discount_int <= max_discount:
            total_price: Decimal = self.total_price()
            fin_price = (
                total_price - total_price
                * self.to_decimal(discount) / Decimal(100)
            )

            return fin_price.quantize(Decimal('0.01'))
        else:
            raise ValueError(
                f'Неверное значение скидки. Скидка не может быть'
                f'меньше {min_discount} и больше {max_discount}. '
                'Также значение должно быть целым числом.'
            )

    def clear_basket(self):
        """Метод очищает корзину."""
        self.products.clear()


products_list = [
    {
        'product_id': 1,
        'name': 'chat_gpt',
        'price': 2500,
        'quantity': 3
    },
    {
        'product_id': 1,
        'name': 'chat_gpt',
        'price': 2500,
        'quantity': 7
    },
    {
        'product_id': 2,
        'name': 'deepseek',
        'price': 50,
        'quantity': 1
    },
    {
        'product_id': 3,
        'name': 'alisa',
        'price': 750.65,
        'quantity': 2
    }
]
