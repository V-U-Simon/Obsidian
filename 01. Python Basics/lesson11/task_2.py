"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyDivisionZeroError(Exception):
    def __init__(self, *message):
        if message:
            self.message = message[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'MyDivisionZeroError (Деление на 0 не допустимо)\n{self.message} '
        else:
            return 'MyDivisionZeroError (Деление на 0 не допустимо)'


if __name__ == '__main__':
    while True:
        arg = int(input('Введите число на которе будет делится 1: '))
        try:
            res = 1 / arg
        except:
            print(MyDivisionZeroError())  # без вызова ошибки
        # except MyDivisionZeroError as err: # вызов ошибки
        #     print(err)
