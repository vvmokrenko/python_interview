# 3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        # пытаемся достучаться до скрытых значений через геттеры
        print(self.get_name, self.get_price)


parent = ItemDiscount('item1', 10)
child = ItemDiscountReport('item2', 20)
child.get_parent_data()
