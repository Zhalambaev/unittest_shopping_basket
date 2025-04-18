# ShoppingBasket Unit Tests 🛒

Демонстрационные юнит-тесты, покрывающие логику корзины: добавление, удаление и расчёт итоговой стоимости, включая работу со скидками.

## Файл base.py Содержит класс с набором базовых и вспомогательных методов для работы с тестами.
- `setUp` - Подготовка данных для тестирования
- `add_product_to_basket()` - Добавление продукта в корзину
- `get_product()` - Поиск продукта по id

## Что проверяется:

### Файл test_initialization_basket.py
- ✅ Корзина создаётся пустой

### Файл test_add_product.py
- ✅ Добавление одного товара
- ✅ Повторное добавление товара (увеличивает количество)
- ✅ Обработка нулевого и отрицательного количества
- ✅ Проверка на отрицательную цену
- ✅ Добавление нескольких товаров
- ✅ Вспомогательные методы: `value_error_add_product`

### Файл test_remove_product.py
- ✅ При удалении части товара его количество уменьшается на заданное число
- ✅ Товар удаляется из корзины, если его количество равно нулю
- ✅ При попытке удалить больше, чем есть в наличии, товар полностью удаляется из корзины
- ✅ При попытке удалить несуществующий товар вызывается исключение

### Файл test_cost.py
- ✅ Правильно рассчитывается итоговая стоимость товара без скидки
- ✅ Правильно рассчитывается итоговая стоимость товара co скидки
- ✅ Правильно рассчитывается итоговая стоимость при максимальной скидке 100%
- ✅ Правильно рассчитывается итоговая стоимость при минимальной скидке 0%

### Файл test_clear_basket.py
- ✅ Полная очистка корзины работает исправно

## Как запустить

```bash
python3 -m unittest discover -s tests