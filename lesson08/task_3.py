"""
3. Написать декоратор для логирования типов позиционных аргументов функции,

например:

def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

# >>> a = calc_cube(5)
5: <class 'int'>

Примечание:
если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:

# >>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = args + tuple(kwargs.values())
        return [f"{func.__name__}({arg}: {type(arg)})" for arg in args]

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    assert calc_cube(5) == ["calc_cube(5: <class 'int'>)"]
    assert calc_cube(5, 2) == ["calc_cube(5: <class 'int'>)", "calc_cube(2: <class 'int'>)"]
    assert calc_cube(a=3, b=3) == ["calc_cube(3: <class 'int'>)", "calc_cube(3: <class 'int'>)"]
    assert calc_cube(2, c=9) == ["calc_cube(2: <class 'int'>)", "calc_cube(9: <class 'int'>)"]
