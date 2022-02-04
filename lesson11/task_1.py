"""
1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».

В рамках класса реализовать два метода.

Первый,
с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».

Второй,
с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
"""

from __future__ import annotations
import re


class Date():
    date = None  # todo: насколько тут нужна заглушка? (для очевидности наличия переменной)
    _months = {
        r'январ[ья]': 31,
        r'феврал[ья]': 28,  # todo: учесть высокосные года
        r'март[а]?': 31,
        r'апрел[ья]': 30,
        r'ма[яй]': 31,
        r'июн[ья]': 30,
        r'июл[ья]': 31,
        r'август[а]?': 31,
        r'сентябр[ья]': 30,
        r'октябр[ья]': 31,
        r'ноябр[ья]': 30,
        r'декабр[ь]': 31,
    }

    @classmethod
    def set_date(cls, date: str):
        cls.date_validation(date)  # валидация при присвоении даты (гарантирует что в последующем данные будут валидны)
        cls.date = date

    @classmethod
    def convert_int_date(cls) -> int:
        """Извлекает число, месяц, год и преобразовывать их тип к типу «Число»."""
        day, month, year = Date.date.split('-')
        day = int(day)

        for k in cls._months:
            pattern = re.compile(k)
            if re.fullmatch(pattern, month):
                month = cls._months[k]
                break

        year = int(year) * 365  # todo: учесть высокосные года
        return year + month + day

    @staticmethod
    def date_validation(date: str) -> bool:
        pattern = re.compile(r"\d{2}-\w*-\d{4}")
        if re.fullmatch(pattern, date):
            return True
        raise ValueError(f'Неверные формат: {Date.date} | пример: 14-августа-1992')


if __name__ == '__main__':
    Date.date = '14-августа-2021'  # валидация происходит при присвоении
    Date.convert_int_date()
