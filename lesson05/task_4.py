'''
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего,

например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

Подсказка: использовать возможности python, изученные на уроке.
'''

# решение в лоб
def bigger_then_previous(list_of_numbers: list):
    list_for_return = []
    for num, el in enumerate(list_of_numbers):
        if el > list_of_numbers[num-1]:
            if num > 0:
                list_for_return.append(el)
    return list_for_return


if __name__ == '__main__':
    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = [12, 44, 4, 10, 78, 123]
    assert bigger_then_previous(src) == result
