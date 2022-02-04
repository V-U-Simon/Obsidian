# ====================================== Задача 2 ======================================
"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.

Рекомендация:
выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.

Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте:
есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
"""
import datetime
import requests
from requests.exceptions import HTTPError, ConnectionError


def show_currency_rate(function):
    """
    Декорирование функции вывода курса валют
    Вывод: наименование валюты, курс к рублю
    """

    def wrapper(value):
        if curs := function(value):
            currency, dict_currency, date = curs
            return f'{currency} - {dict_currency}'

    return wrapper


def get_curs(currency: str) -> tuple:
    """
    Принимает в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
    Возвращающат курс этой валюты по отношению к рублю.
    Получает курс  валют с сайта ЦБ
    """

    def get_response(url) -> requests.Response or None:
        """ Check connection """
        try:
            response = requests.get(url)
            # todo почему нет ошибки 404 при ошибочном url 'http://www.cbr.ru/scripts/XML_ddddddafily.asp'
            # print(response.status_code)
            # print('Successful connection')
            return response
        except ConnectionError or HTTPError:
            print('Ошибка в HTTP')
            return None
            # todo: как передать возникающую ошибку в str?

    def parse_currency_rate(response) -> tuple:  # todo: как указать тип datetime.time?
        """
        Из ответа сервера ЦБ формирует словарь: {Валюта: курс}
        From response of the Central Bank make a dict: {Валюта: курс}
        """
        currency_rate = {}
        currency = None
        nominal = None
        xml_text = response.text.split('>' '<')

        date = xml_text[1].split('"')[1]
        date = datetime.datetime.strptime(date, '%d.%m.%Y')

        for row in xml_text[2:]:
            if row.startswith('CharCode'):
                currency = row.split('>')[1].split('<')[0]
            elif row.startswith('Nominal'):
                nominal = int(row.split('>')[1].split('<')[0])
            elif row.startswith('Value'):
                value = row.split('>')[1].split('<')[0]
                currency_rate[currency] = float(value.replace(',', '.')) / nominal

        return currency_rate, date

    def get_validation_args(arg, dict_currency) -> str:
        """
        Проверка на ввод с косоли и приведение к общему для функции типу
        Проверка вводимых пользователем данных на наличие ошибок в наименовании валюты
        """
        if isinstance(arg, list):  # Проверка на ввод в консоль
            if len(arg) == 2:
                arg = arg[1]
            else:
                arg = arg[1]
        arg = arg.upper()
        return arg if arg in dict_currency else print('Введите корректную валюту из списка: {}'
                                                      .format(', '.join([k for k in dict_currency])))

    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    resource = get_response(url)  # проверяем корректность соединения
    dict_currency, date = parse_currency_rate(resource)  # парсим xml
    if currency := get_validation_args(currency, dict_currency):  # Проверяем корректнгсть введения пользователем валюты
        return currency, dict_currency[currency], date  # выводим данные для последующего вывода через декораторы


if __name__ == '__main__':
    # декорирование функции
    get_curs = show_currency_rate(get_curs)

    currency1 = 'USD'
    currency2 = 'UsD'
    currency3 = ''
    currency4 = '43'
    print(1, get_curs(currency1))
    print(2, get_curs(currency2))
    print(3, get_curs(currency3))
    print(4, get_curs(currency4))
