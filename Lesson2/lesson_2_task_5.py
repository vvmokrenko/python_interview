# 5. Реализовать расчет цены товара со скидкой.
# Величина скидки должна передаваться в качестве аргумента в дочерний класс.
# Выполнить перегрузку методов конструктора дочернего класса (метод init,
# в который должна передаваться переменная — скидка), и перегрузку метода str дочернего класса.
# В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
# Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
# (вторая и третья строка после объявления дочернего класса).


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    @property
    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value


class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__discount = discount

    def get_parent_data(self):
        # пытаемся достучаться до скрытых значений через геттеры
        print(self.get_name, self.get_price)

    def __str__(self):
        return str(round(self.get_price * self.__discount / 100))


parent = ItemDiscount('item1', 10)
# Скидка в 60% к цене товара
child = ItemDiscountReport('item2', 20, 60)
print(f'Цена товара со скидкой: {str(child)}')
