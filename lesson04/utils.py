import datetime
import requests
from requests import HTTPError

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

@dec_show_cr_plus_date
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
            # todo: как передать возникающую ошибку? Или лучше просто исключить проверку овтета (get_response)?
            # todo на сколько крректно тут указывать None для последующей проверки ошибку? или всетаки raise?

    def parse_currency_rate(response) -> tuple:  # todo: как указать тип date -> tuple(dict, datetime.time):?
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
            # учесть номинал
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
        return currency, dict_currency[currency], date


if __name__ == '__main__':
    currency1 = 'USD'
    currency2 = 'UsD'
    currency3 = ''
    currency4 = '43'
    print(1, get_curs(currency1))
    print(2, get_curs(currency2))
    print(3, get_curs(currency3))
    print(4, get_curs(currency4))
