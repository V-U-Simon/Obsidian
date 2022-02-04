"""
6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
# Валидация проходит через анатаци≈≈ю типов
from __future__ import annotations

import datetime
from abc import ABC


class Storage:
    db = {}  # место хранения, заглушка sql
    id = 0  # start # свой id для возможности отслеживания истории транзакций одного оборудования

    @staticmethod
    def write(departure: Company | Warehouse,
              destination: Company | Warehouse,
              content: list[OfficeEquipment,]):

        __time = datetime.datetime.now()

        data = {
            'departure': departure,
            'destination': destination,
            'time': __time,
            'content_list': content,  # list of equipment
        }

        last = len(Storage.db)
        Storage.db[last] = data

        return data

    @staticmethod
    def get_equipment(id_equipment: int) -> OfficeEquipment | None:
        for id, data in Storage.db.items():
            for key, value in data.items():
                if key == 'content_list':
                    for content in value:
                        # todo: int(str(value.id)) в связи с чем необходимо двойное оборачивание int(str(x))?
                        if int(str(content.id)) == id_equipment:
                            return value
        print(f'Оборудование: id {id_equipment} отсутствет на складе')
        return None

    @staticmethod
    def show():
        for id, data in Storage.db.items():
            print(f'id: {id}')
            for key, value in data.items():
                if key == 'content_list':
                    print('Содержание транзакции:')
                    for content in value:
                        print(f'- {content} (id: {content.id})')
                else:
                    print(f'{key:<12}: {value}')
            print('-' * 20)


class Warehouse:
    available_volume = 3000

    def __str__(self):
        return f'{self.__class__.__name__}'

    # todo
    def show_available_volume(self):
        """Показвает доступный объем склада"""
        pass

    # todo
    def show_equipment(self):
        """Показывает всю оргтехнику(+id) доступную на складе"""
        pass

    def transfer_to_warehouse(self,
                              from_place: Company,
                              equipment: OfficeEquipment | list[OfficeEquipment,] | type,
                              count: int = 1):
        """Транзакция в склад
        P.S. equipment - только экземпляры класса"""

        to_place = self

        if isinstance(equipment, type):  # если передается класс todo: подробнее изучить type и object
            equipment = [equipment() for _ in range(count)]
        elif isinstance(equipment, OfficeEquipment):  # если передается класс
            equipment = [equipment, ]

        Storage.write(from_place, to_place, equipment)

    def transfer_from_warehouse(self,
                                to_place: Company,
                                equipment: OfficeEquipment | list[OfficeEquipment,],
                                count: int = 1):
        """Транзакция из склада
        P.S. equipment - только экземпляры класса"""
        from_place = self

        if isinstance(equipment, type):  # если передается класс
            equipment = [equipment() for _ in range(count)]
        elif isinstance(equipment, OfficeEquipment):  # если передается класс
            equipment = [equipment, ]

        Storage.write(from_place, to_place, equipment)


class Company:
    def __init__(self, name):
        self.name = name
        self.divisions = []

    # todo: допилить возможность добавления структурных подразделений
    # def add_division(self, name_division):
    #     self.divisions.append(CompanyDivision(name_division))

    def __str__(self):
        # if self.divisions:
        #     divisions = [div.name for div in self.divisions]
        #     return f'{self.name}: {divisions}'
        # else:
        return f'{self.name}'

    # todo
    def show_equipment(self):
        """Показывает всю оргтехнику(+id) находящцюся в организации"""
        pass


# todo: допилить возможность добавления структурных подразделений
# class CompanyDivision(Company):
#     # storage = {}
#
#     def __init__(self, division, name=):
#         a = .__class__.__name__
#         super().__init__(name)
#         self.name = division
#
#     def __str__(self):
#         if self.name:
#             divisions = [div.name for div in self.divisions]
#             return f'{self.name}: {divisions}'
#         else:
#             return f'{self.name}'


class ID:
    """Генератор и хранилище ID орг. техники"""
    id_dict = {}

    def __init__(self, equipment):
        id = len(ID.id_dict)
        ID.id_dict[id] = equipment
        self.id = id

    def __str__(self):
        return f'{self.id}'

    @staticmethod
    def add(equipment):
        """Добавляет уникальный номер"""
        ID.id_dict.setdefault(0, equipment)


class OfficeEquipment(ABC):
    list_of_id = []

    def __init__(self):
        self.id = ID(self)

    def __str__(self):
        return f'{self.__class__.__name__}'


class Printer(OfficeEquipment):
    list_of_id = []

    def __init__(self):
        super().__init__()
        self._weight = 2
        self._cubic_volume = 0.2


class Xerox(OfficeEquipment):
    list_of_id = []

    def __init__(self):
        super().__init__()
        self._weight = 4
        self._cubic_volume = 0.5


class Scanner(OfficeEquipment):
    list_of_id = []

    def __init__(self):
        super().__init__()
        self._weight = 1
        self._cubic_volume = 0.2


if __name__ == '__main__':
    # Канцелярское оборудование и id
    printer1 = Printer()
    printer2 = Printer()
    xerox1 = Xerox()
    scanner = Scanner()

    # Склад, компании
    warehouse = Warehouse()
    ooo = Company('Комус')
    # todo: допилить возможность добавления структурных подразделений
    # ooo.add_division('ЦАО')
    # ooo.add_division('СЗАО')
    provider = Company('Поставщик')
    print(ooo)
    print(provider)

    # Транзакции
    warehouse.transfer_to_warehouse(provider, Printer, 5)
    warehouse.transfer_to_warehouse(provider, xerox1)

    # Перемеещение сущетсвующего принтера со склада в организацию
    my_printer1 = Storage.get_equipment(999)
    my_printer2 = Storage.get_equipment(2)
    warehouse.transfer_from_warehouse(ooo, my_printer2)

    # Содержимое базы данных
    Storage.show()
