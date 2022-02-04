"""
6. Реализовать простую систему хранения данных о суммах продаж булочной.
Должно быть два скрипта с интерфейсом командной строки:
для записи данных и для вывода на экран записанных данных.
При записи передавать из командной строки значение суммы продаж.

Для чтения данных реализовать в командной строке следующую логику:

просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
равный второму числу, включительно.

Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.

Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.

Примеры запуска скриптов:
python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
"""

import os
# import sys

STORAGE = os.path.relpath('files/bakery.csv')


def add_sale(argv):
    """
    Запись в хранилище
    * импотируем в модуль add_sale.py
    """
    global STORAGE

    program, arg = argv
    arg = arg.replace(' ', '')
    with open(STORAGE, 'a', encoding='UTF-8') as storage:
        return storage.write(arg + '\n')


def change_sale(argv):
    """
    Запись в хранилище
    - импотируем в модуль add_sale.py
    """
    global STORAGE

    program, arg = argv
    arg = arg.replace(' ', '')
    with open(STORAGE, 'a', encoding='UTF-8') as storage:
        return storage.write(arg + '\n')


def view_sale(argv):
    """
    else - просто запуск скрипта — выводить все записи;
    1 - запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
    2 - запуск скрипта с двумя числами — выводить записи,
    начиная с номера, равного первому числу, по номер,равный второму числу, включительно.
    * импотируем в модуль show_sales.py
    """
    args = argv[1:]
    with open(STORAGE, 'r', encoding='UTF-8') as storage:
        if len(args) == 1:
            for n, line in enumerate(storage, start=1):
                if n == int(args[0]):  # cursor
                    print(f'{n} --- {line.strip()}')

        elif len(args) == 2:
            for n, line in enumerate(storage, start=1):
                if int(args[0]) <= n <= int(args[1]):  # start, stop
                    print(f'{n} --- {line.strip()}')

        else:
            for n, line in enumerate(storage, start=1):  # all
                print(f'{n} --- {line.strip()}')


if __name__ == '__main__':
    pass
