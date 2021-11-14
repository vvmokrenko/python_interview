# 6. Проверить на практике возможности полиморфизма.
# Необходимо разделить дочерний класс ItemDiscountReport на два класса.
# Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
# которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
# Далее реализовать выполнение каждой из функции тремя способами.


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

    def get_info(self):
        return f'Родитель'


class ItemDiscountReportName(ItemDiscount):

    def get_info(self):
        return f'Наименование={self.get_name}'


class ItemDiscountReportPrice(ItemDiscount):

    def get_info(self):
        return f'Цена={self.get_price}'


# Способ 1 - вызываем методы конкретных экземпляров
n = ItemDiscountReportName('item1', 50)
print(n.get_info())

p = ItemDiscountReportPrice('item2', 100)
print(p.get_info())

# Способ 2 - вызываем методы экземпляров из списка объектов
for obj in (n, p):
    print(obj.get_info())


# Способ 3 - используем интерфейсную функцию для вывода
def obj_handler(obj):
    print(obj.get_info())


obj_handler(n)
obj_handler(p)
