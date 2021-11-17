# 5. Усовершенствовать первую функцию из предыдущего примера.
# Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число).
# Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод первого вхождения,
# вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
# состоящих из букв и цифр - например, example345.

import os
import random
import string
import re


# генерация рандомной строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


# функция, возвращающая список рандомных чисел
def get_random_int_list(cnt):
    return [random.randint(0, 100) for _ in range(cnt)];


# функция, возвращающая список рандомных строк
def get_random_string_list(cnt):
    return [generate_random_string(20) for _ in range(cnt)]


# функция создания файла
def create_file(path):
    if os.path.isfile(path):
        print('Файл с таким именем уже существует')
        return False

    with open(path, 'w', encoding='utf-8') as f:
        numbers = get_random_int_list(10)
        strings = get_random_string_list(10)
        # формируем строку+число для случайных строк
        f.writelines([f'{n} {s}\n' if (n % 3 == 0) else f'{n} {s + str(n)}\n' for n, s in zip(numbers, strings)])
        return f


def print_file(path, substr):
    c = '\n\r'
    with open(path.name, 'r', encoding='utf-8') as f:
        for l in f.readlines():
            print(l, end='')
        f.seek(0)
        for l in f.readlines():
            if l.find(substr) > 0:
                print(f'Первое вхождение строки "{substr}" в строке "{l.rstrip(c)}"')
                break
        f.seek(0)
        print(f'Список всех вхождений строки "{substr}": ')
        for l in f.readlines():
            if l.find(substr) > 0:
                print(l, end='')
        f.seek(0)
        print(f'Заменяем все вхождения строки "{substr}" на "{substr.upper()}": ')
        for l in f.readlines():
            if l.find(substr) > 0:
                print(l.replace(substr, substr.upper()), end='')
        f.seek(0)
        print(f'Выводим все подстроки, состоящие из букв и цифр: ')
        for l in f.readlines():
            for m in l.split():
                if re.match("^[A-Za-z]+[0-9]+$", m):
                    print(m)


filename = 'test_lesson_3_task_5.txt'
# будем искать подстроку
substr = "z"

f = create_file(filename)
if f:
    print('Содержимое файла и статистика: ')
    print_file(f, substr)
