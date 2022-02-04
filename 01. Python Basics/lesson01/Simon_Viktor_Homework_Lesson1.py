# ====================================== Задача 1 ======================================
"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""


def date_convector(date: int) -> str:
    seconds = date % 60
    date = date // 60
    if not date: return f'{seconds} сек'

    minutes = date % 60
    date = date // 60
    if not date: return f'{minutes} мин {seconds} сек'

    hours = date % 24
    date = date // 24
    if not date: return f'{hours} час {minutes} мин {seconds} сек'

    days = date % 7
    date = date // 7
    if not date: return f'{days} дн {hours} час {minutes} мин {seconds} сек'


# ====================================== Задача 2 ======================================
"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
    a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
    Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. 
    Внимание: использовать только арифметические операции!
    
    b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, 
    сумма цифр которых делится нацело на 7. 
    
    c. * Решить задачу под пунктом b, не создавая новый список.
"""
# ====================================== Вариант "a"
cube = [x ** 3 for x in range(1000) if x % 2]


def sum_of_numbers(numbers: list[int]) -> str:
    """
    сумма чисел каждого элемента списка, которая делится на 7
    """
    for number in numbers:
        if (temp := number) % 7 == 0:
            total = 0
            while temp:
                total += temp % 10
                temp //= 10
            yield f'{number} = {total}'


# ====================================== Вариант "b"
# Создание исходного списка через генератор
cube_17 = [(x + 17) ** 3 for x in range(1, 1000) if x % 2]
# через цикл for
# cube_17 = []
# for x in range(1000):
#     x += 17
#     if x % 2:
#         cube_17.append(x ** 3)

# ====================================== Вариант "с"
# Вариант без создания нового списка
pass

# ====================================== Задача 3 ======================================
"""
Реализовать склонение слова «процент» во фразе «N процентов». 
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
    1 процент
    2 процента
    3 процента
    4 процента
    5 процентов
    6 процентов
    ...
    100 процентов
"""


def numeral_words(number):
    """
    1. После числительного один и составных числительных, оканчивающихся на один,
    ставится существительное в именительном падеже.
    2. После числительных два, три, четыре и составных числительных, оканчивающихся на два, три, четыре,
    ставится существительное в родительном падеже единственного числа.
    3. После числительного пять, шесть и т.д. и после слов много, мало, несколько, сколько и т.д.
    ставится существительное в родительном падеже множественного числа.

    thanks: https://qna.habr.com/q/903897
    """
    temp = number
    temp %= 10
    if temp == 1 and number != 11:
        return f'{number} процент'
    if (2 <= temp < 5) and all([number != 12,
                                number != 13,
                                number != 14,
                                number != 15, ]):
        return f'{number} процента'
    else:
        return f'{number} процентов'


if __name__ == '__main__':
    print('====================================== Задача 1 ======================================')
    # Исключение в данных случаях
    # print(date_convector(''))
    # print(date_convector('text'))
    # print(date_convector(None))
    print(date_convector(True))
    print(date_convector(False))
    print(date_convector(0))
    print(date_convector(-53))
    print(date_convector(0.93))

    assert date_convector(53) == "53 сек"
    assert date_convector(153) == "2 мин 33 сек"
    assert date_convector(4153) == "1 час 9 мин 13 сек"
    assert date_convector(400153) == "4 дн 15 час 9 мин 13 сек"
    print('Tests of the first task completed successfully')

    print('====================================== Задача 2 ======================================')
    print('initial list', cube)
    print('cube done   ', list(sum_of_numbers(cube)))
    print('init list +17', cube_17)
    print('cube+17 done', list(sum_of_numbers(cube_17)))

    print('====================================== Задача 3 ======================================')
    assert numeral_words(1) == '1 процент'
    assert numeral_words(2) == '2 процента'
    assert numeral_words(5) == '5 процентов'
    assert numeral_words(11) == '11 процентов'
    assert numeral_words(12) == '12 процентов'
    assert numeral_words(13) == '13 процентов'
    assert numeral_words(14) == '14 процентов'
    assert numeral_words(20) == '20 процентов'
    assert numeral_words(21) == '21 процент'
    assert numeral_words(22) == '22 процента'
    assert numeral_words(23) == '23 процента'
    assert numeral_words(24) == '24 процента'
    assert numeral_words(25) == '25 процентов'
    assert numeral_words(91) == '91 процент'
    assert numeral_words(100) == '100 процентов'
    print('Tests of the third task completed successfully')

    for i in range(1, 101):
        print(numeral_words(i))