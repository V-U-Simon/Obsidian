"""
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).

Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество
для пользователей и название каждого хобби:
преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
В словаре должны храниться данные, полученные в результате парсинга.
"""

import os
import sys
from itertools import zip_longest


def users_and_hobby(csv_users: str, csv_hobby: str) -> tuple:
    """Объединение юзеров и хобби через генератор"""
    with \
            open(csv_users, 'r', encoding='UTF-8') as csv_users, \
            open(csv_hobby, 'r', encoding='UTF-8') as csv_hobby:

        users = (user.strip().split(',') for user in csv_users)
        hobby = (hobby.strip().split(',') for hobby in csv_hobby)

        for user, hobby_ in zip_longest(users, hobby):
            if user is None: sys.exit(1)
            yield user, hobby_


if __name__ == '__main__':
    csv_users = os.path.join(os.getcwd(), 'files', 'users.csv')
    csv_hobby = os.path.join(os.getcwd(), 'files', 'hobby.csv')
    print(*users_and_hobby(csv_users, csv_hobby))
