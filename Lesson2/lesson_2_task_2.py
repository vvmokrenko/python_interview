# Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        # пытаемся достучаться до скрытых значений.
        # как результат - ошибка выполнения, т.к. нет таких атрибутов в дочернем классе
        print(self.__name, self.__price)


parent = ItemDiscount('item1', 10)
child = ItemDiscountReport('item2', 20)
child.get_parent_data()
