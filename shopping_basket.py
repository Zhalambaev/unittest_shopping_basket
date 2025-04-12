from dataclasses import dataclass
from decimal import Decimal
from typing import Union


@dataclass
class Product:
    product_id: int
    name: str
    price: Decimal


class ShoppingBasket:
    """Класс имитирует корзину в интернет-магазине."""
    def __init__(self):
        self.products: list[Product] = []

    def to_decimal(self, data: Union[int, float, str]) -> Decimal:
        """Метод преобразует данные в данные типа Decimal."""
        if isinstance(data, float):
            return Decimal(str(data))
        else:
            return Decimal(data)

    def add_product(
            self, product_id: int, name: str, price: Union[int, float, str]
    ):
        """Метод добавляет товар в корзину."""
        self.products.append(
            Product(product_id, name, self.to_decimal(price))
        )

    def remove_product(self, product_id: int):
        """Метод удаляет товар из корзины, если он там есть."""
        self.products = [
                item for item in self.products
                if item.product_id != product_id
        ]

    def total_price(self):
        """Метод рассчитывает общую стоимость всех товаров в корзине."""
        return sum(price.price for price in self.products)

    def discount_calc(self, discount: Union[int, str]) -> Decimal:
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
                * self.to_decimal(discount) / 100
            )

            return fin_price.quantize(Decimal('0.01'))
        else:
            raise ValueError(
                f'Неверное значение скидки. Скидка не может быть'
                f'меньше {min_discount} и больше {max_discount}. '
                'Также значение должно быть целым числом.'
            )


products_list = [
    {
        'product_id': 1,
        'name': 'chat_gpt',
        'price': 2500
    },
    {
        'product_id': 2,
        'name': 'deepseek',
        'price': 50
    },
    {
        'product_id': 3,
        'name': 'alisa',
        'price': 750.65
    }
]
basket = ShoppingBasket()

for item in products_list:
    basket.add_product(
        product_id=item.get('product_id'),
        name=item.get('name'),
        price=item.get('price')
    )

print(basket.discount_calc(10))
