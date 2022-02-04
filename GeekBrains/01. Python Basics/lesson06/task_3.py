"""
3. Есть два файла:
в одном хранятся ФИО пользователей сайта,
а в другом — данные об их хобби.

Известно, что при хранении данных используется принцип:
одна строка — один пользователь,
разделитель между значениями — запятая.

Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО,
значения — данные о хобби.

Сохранить словарь в файл.
Проверить сохранённые данные.

Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None
Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать,
что объём данных в файлах во много раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):

скалолазание,охота
горные лыжи
"""

import os
import sys
from itertools import zip_longest


def users_and_hobby(csv_users: str, csv_hobby: str) -> dict:
    """Объединение юзеров и хобби"""
    with \
            open(csv_users, 'r', encoding='UTF-8') as csv_users, \
            open(csv_hobby, 'r', encoding='UTF-8') as csv_hobby:
        users = [user.strip().replace(',', ' ') for user in csv_users]
        hobby = [hobby.strip() for hobby in csv_hobby]

        # if users < hobby: todo: почему возвращает True?
        if len(users) < len(hobby): return sys.exit(1)
        return {k: v for k, v in zip_longest(users, hobby)}


if __name__ == '__main__':
    csv_users = os.path.join(os.getcwd(), 'files', 'users.csv')
    csv_hobby = os.path.join(os.getcwd(), 'files', 'hobby.csv')

    print(users_and_hobby(csv_users, csv_hobby))
