# 2. Написать программу, которая запрашивает у пользователя ввод числа.
# На введенное число она отвечает сообщением, целое оно или дробное.
# Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.

import locale


def compare_parts(string):
    try:
        number = float(string)
        if int(number) == number:
            print('целое')
        else:
            print('дробное')
            # не используем математические пакеты, чтобы избежать ошибок представления/округления дробной части
            # но при этом надо учесть, что разделитель дробной части может быть различым в зависимости от
            # языковых настроек
            decimal_point = locale.localeconv()['decimal_point']
            left, right = string.split(decimal_point)
            return left == right
    except ValueError:
        print('Не число!')


value = input('Введите число: ')
result = compare_parts(value)
if result in (True, False):
    print(result)
