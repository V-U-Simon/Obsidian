"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.

А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""
from abc import ABC


class Warehouse:
    storage = {}
    available_volume = 3000

    def __init__(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}'


class Id:
    id_dict = {}

    def __init__(self, equipment):
        Id.id_dict[len(Id.id_dict)] = equipment


class OfficeEquipment(ABC):
    def __init__(self):
        self.id = Id(self.__class__)

    def __str__(self):
        return f'{self.__class__.__name__}'


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self._weight = 2
        self._cubic_volume = 0.2


class Xerox(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self._weight = 4
        self._cubic_volume = 0.5


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self._weight = 1
        self._cubic_volume = 0.2


if __name__ == '__main__':
    warehouse = Warehouse()

    printer1 = Printer()
    printer2 = Printer()
    xerox1 = Xerox()
    scanner = Scanner()
    print(scanner)
    print(Id.id_dict)
