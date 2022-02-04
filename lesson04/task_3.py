# ====================================== Задача 3 ======================================
"""
*(вместо 2) Доработать функцию currency_rates():
теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
Дата должна быть в виде объекта date.
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""

from task_2 import get_curs


def dec_show_cr_plus_date(function):
    """
    Декорирование функции вывода курса валют
    Вывод: дата, наименование валюты, курс к рублю
    """

    def wrapper(value):
        if curs := function(value):
            currency, dict_currency, date = curs
            return f'{date.date()}: {currency} - {dict_currency}'

    return wrapper


if __name__ == '__main__':
    # декорирование импортированной функции
    get_curs = dec_show_cr_plus_date(get_curs)

    currency1 = 'USD'
    currency2 = 'UsD'
    currency3 = ''
    currency4 = '43'
    print(1, get_curs(currency1))
    print(2, get_curs(currency2))
    print(3, get_curs(currency3))
    print(4, get_curs(currency4))
