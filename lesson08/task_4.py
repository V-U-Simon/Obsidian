"""
4. Написать декоратор с аргументом-функцией (callback),
позволяющий валидировать входные значения функции и выбрасывать исключение ValueError,
если что-то не так, например:

def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


# >>> a = calc_cube(5)
125
# >>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5

Примечание:
сможете ли вы замаскировать работу декоратора?
"""


def val_checker(decor_func):
    def _val_checker(fucn):
        def wrapper(*args):

            check = map(decor_func, args)  # == lambda x: x > 0
            for ch, arg in zip(check, args):
                if ch:
                    return fucn(arg)
                else:
                    raise ValueError('Передано значение меньше 0')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    assert calc_cube(5) == 125
    assert calc_cube(0) == 0
    calc_cube(-5)  # ValueError('Передано значение меньше 0')
