# 4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение.
# Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
# Для создания списков использовать генераторы. Применить к спискам функцию zip().
# Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
# чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
# В нее должна передаваться ссылка на созданный файл.
# Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
# Вся программа должна запускаться по вызову первой функции.

import os
import random
import string


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
        f.writelines([f'{n} {s}\n' for n, s in zip(numbers, strings)])
        return f


def print_file(path):
    with open(path.name, 'r', encoding='utf-8') as f:
        for l in f.readlines():
            print(l, end='')


filename = 'test_lesson_3_task_4.txt'

f = create_file(filename)
if f:
    print('Содержимое файла: ')
    print_file(f)
