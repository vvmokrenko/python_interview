show_table = lambda result, rows, cols: \
    '\n'.join(['\t'.join([str(result[r][c]) for c in range(cols + 1)]) for r in range(rows + 1)])


def multiply_table(rows, cols):
    """
    :param rows: количество строк в таблице умножения
    :param cols: количество столбцов в таблице умножения
    :return: возвращает таблицу умножения (rows X cols)
    """
    # Инициализация таблицы
    result = [[0] * (cols + 1) for r in range(rows + 1)]
    # Заполенение таблицы
    for r in range(rows + 1):
        for c in range(cols + 1):
            if r == 0:
                result[r][c] = c  # номер столбца
            elif c == 0:
                result[r][c] = r  # номер строки
            else:
                result[r][c] = r * c

    # вывод на экран через лямбду
    print(show_table(result, rows, cols))


# Вывод таблицы умножения
multiply_table(10, 10)
