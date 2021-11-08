"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание:
длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
При этом скрипт завершается, сформированный список с числами выводится на экран.

Подсказка:
для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class OnlyIntException(Exception):
    def __init__(self, *message):
        if message:
            self.message = message[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'OnlyIntException: могут передаваться только int\n{self.message}'
        return f'OnlyIntException: могут передаваться только int'


class OnlyIntList:
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            values = [self.convert_to_int(val) for val in values]
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # если значение или тип ключа некорректны, list выбросит исключение
        return self.values[key]

    def __setitem__(self, key, value):
        value = self.convert_to_int(value)
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return OnlyIntList(reversed(self.values))

    def __str__(self):
        return f'{self.values}'

    def append(self, value):
        value = self.convert_to_int(value)
        self.values.append(value)

    @staticmethod
    def convert_to_int(value):
        try:
            value = int(value)
        except:
            print(f'{OnlyIntException("Попоробуйте ввести число")}')
        else:
            return value


if __name__ == '__main__':
    l = OnlyIntList()
    while True:
        inp = input('Введите число для добавления в список "OnlyIntList" (для выхода exit): ')
        if inp == 'exit':
            print(l)
            break
        l.append(inp)
