import time

# утилита
f = lambda val, mn, mx: int(val * (mx - mn) + mn)

# базовое значение для генратора случайных чисел
seed = 0
# Результрующий список
l = []
# Результрующий словарь
d = dict()


def custom_random(start, stop):
    """
    :param start: начальное число генерации
    :param stop: конечное число генерации (нуль исключаем)
    :return: Генратор случайных чисел, основанный на алгоритме Лемера
    """
    global seed

    if start <= 0:
        print('Некорректная левая граница диапазона')
        return
    if stop <= 0:
        print('Некорректная правая граница диапазона')
        return

    # Константы Лемера
    a = 16807
    m = 2147483647
    q = 127773
    r = 2836
    # Базовое значение
    if seed == 0:
        seed = int((time.time() - float(str(time.time()).split('.')[0])) * 1000000000)
        val = f(seed / m, start, stop)
        l.append(val)
        d['elem_' + str(len(l))] = val
    else:
        hi = seed / q
        lo = seed % q
        seed = (a * lo) - (r * hi)
        #  print('a', seed)
        if (seed <= 0):
            seed = seed + m
        val = f(seed / m, start, stop)
        l.append(val)
        d['elem_' + str(len(l))] = val


# Генерируем 10 чисел от 30 до 60
for i in range(10):
    custom_random(30, 60)

print('Список: ', l)
print('Словарь:\n', d)
