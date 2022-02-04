# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield,
#
# например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

# Основние задание
def odd_nums(loop):
    for number in range(1, loop + 1, 2):
        yield number


# Разбор реализации итерируэмых объектов и итераторов (генераторов)
class MyIterator:
    """Кастомный итератор возвращающий четный индекс (iterator)"""

    def __init__(self, sequence):
        self.sequence = sequence
        self._length = len(self.sequence)
        self.index = 0  # Сохраняет информацию о состоянии между итерациями

    def __next__(self):
        if self.index >= self._length:  # если выходит за пределы индекса
            raise StopIteration
        item = self.sequence[self.index]
        self.index += 2
        return item


class MyObject:
    """Итерируемый объект (iterable)"""

    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return MyIterator(self.sequence)


if __name__ == '__main__':
    # Основние задание
    generator_odd_nums = odd_nums(15)  # Генератор и иные итерируемые объекты имеют генератор
    print(*generator_odd_nums)

    # Разбор реализации итерируэмых объектов и итераторов (генераторов)
    iterable_object = MyObject([0, 1, 2, 3, 4, 5])
    iterator = iterable_object.__iter__()
    print(iterable_object)
    print(iterator)

    print(iterator.__next__())
    print(iterator.__next__())

    # todo: сделать итератор для цифр (integer)
