import os


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """

    # Делаем рекурсивные вызовы. Пустые папки не выводим
    for file_or_directory in os.listdir(sPath):
        filename = os.path.join(os.path.abspath(sPath), file_or_directory)
        if os.path.isfile(filename):
            print(filename)
        else:
            # для директорий вытаскиваем их содержимое
            print_directory_contents(filename)


print_directory_contents('c:/temp/1')
