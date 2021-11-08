"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.

Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print('Сумма')
        return f'{self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print('Умножение')
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


k_1 = ComplexNumber(5, -4)
k_2 = ComplexNumber(6, 10)
print(k_1 + k_2)
print(k_1 * k_2)
