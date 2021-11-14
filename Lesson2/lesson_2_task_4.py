# 4. Реализовать возможность переустановки значения цены товара.
# Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
# Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего
# (функция, отвечающая за отображение информации о товаре в одной строке).


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
    def get_parent_data(self):
        # пытаемся достучаться до скрытых значений через геттеры
        print(self.get_name, self.get_price)


parent = ItemDiscount('item1', 10)
child = ItemDiscountReport('item2', 20)
# устанавливаем новые значения через сеттеры
child.set_name('new_item')
child.set_price(200)
child.get_parent_data()
