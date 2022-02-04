"""
7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
передаём ему номер записи и новое значение.
При этом файл не должен читаться целиком — обязательное требование.
Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.
"""

import os
import sys


def change_sale(argv):
    # todo: сделать еще один вариант через FileInput
    """ Запись в хранилище
        * импотируем в модуль add_sale.py """

    global f

    num_line = int(argv[1])
    new_data = str(argv[2]) + '\n'

    with open(STORAGE, 'r+', encoding='UTF-8') as f:
        date = f.readlines()

    # with open(STORAGE, 'w+', encoding='UTF-8') as f: todo: почему не работает?
    with open('files/bakery.csv', 'w+', encoding='UTF-8') as f:
        date[num_line - 1] = new_data
        f.writelines(date)


STORAGE = os.path.relpath('files/bakery.csv', start=os.curdir)

if __name__ == '__main__':
    pass
    # change_sale(('program', 1, 1999.99))
    # """
    # 5978,5
    # 7879,1
    # 9999
    # 14,05
    # 2654,09
    # """
