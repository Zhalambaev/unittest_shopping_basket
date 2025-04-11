class ShoppingBascket():
    """Класс имитирует корзину в интернет-магазине."""
    def __init__(self):
        self.products = []

    def add_product(self, product: str, price: int):
        """Метод добавляет товар в корзину."""
        self.products.append({'product': product, 'price': price})

    def remove_product(self, product: str):
        pass


products_dict = {
    'chat_gpt': 2450,
    'deepseek': 0,
    'умение кодить': 100500100500
}
basket = ShoppingBascket()

for product, price in products_dict.items():
    basket.add_product(product, price)

basket.remove_product('deepseek')

print(basket.products)
