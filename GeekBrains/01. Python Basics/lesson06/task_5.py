"""
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу со словарём.
Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
"""

import os
import sys
from itertools import zip_longest


def dec_show_console(function):
    """
    Декорирование для взаимодествия с консолью
    Ввести относительный путь:      1. к ФИО
                                    2. к хобби
    """

    def wrapper(argv):
        args = argv[1:]
        if len(args) == 2:
            paths = [os.path.relpath(path) for path in args]        # create rel paths
            if all(map(lambda path: os.path.exists(path), paths)):  # checked that path is real
                return function(paths[0], paths[1])
        else:
            print('введите пути(относительные) к двум файлам')
            sys.exit(1)

    return wrapper


@dec_show_console
def users_and_hobby(csv_users: str, csv_hobby: str) -> dict:
    """Объединение юзеров и хобби через генератор"""
    with \
            open(csv_users, 'r', encoding='UTF-8') as csv_users, \
            open(csv_hobby, 'r', encoding='UTF-8') as csv_hobby:
        users = [user.strip().replace(',', ' ') for user in csv_users]
        hobby = [hobby.strip() for hobby in csv_hobby]

        if len(users) < len(hobby): return sys.exit(1)
        return {k: v for k, v in zip_longest(users, hobby)}


print(users_and_hobby(sys.argv).items())

if __name__ == '__main__':
    # в консоли код тут не выполнится
    pass
