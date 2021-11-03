"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError.

Пример:

# >>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
"""

import re


def email_parse(email_address):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    res = re.findall(pattern, email_address)
    if res:
        return dict(zip(['username', 'domain'], str(*res).split('@')))
    raise ValueError(f'wrong email: {email_address}')


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    # {'username': 'someone', 'domain': 'geekbrains.ru'}
    # print(email_parse('someone@geekbrainsru'))
    # ValueError: wrong email: someone@geekbrainsru
