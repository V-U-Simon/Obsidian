"""
5. Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
"""
from __future__ import annotations

import datetime
from abc import ABC


class Storage:
    db = {}  # место хранения, заглушка sql
    id = 0  # start # свой id для возможности отслеживания истории транзакций одного оборудования

    @staticmethod
    def write(departure, destination, content):
        __time = datetime.datetime.now()

        data = {
            'departure': departure,
            'destination': destination,
            'time': __time,
            'content': content,
        }

        last = len(Storage.db)
        Storage.db[last] = data

    @staticmethod
    def get_equipment(id_equipment: int) -> OfficeEquipment | None:
        for id, data in Storage.db.items():
            for key, value in data.items():

                if key == 'content':
                    # todo: int(str(value.id)) в связи с чем необходимо двойное оборачивание
                    if int(str(value.id)) == id_equipment:
                        return value
        print(f'Оборудование: id {id_equipment} отсутствет на складе')
        return None

    @staticmethod
    def show():
        for id, data in Storage.db.items():
            print(f'id: {id}')
            for key, value in data.items():
                if key == 'content':
                    print(f'{key:<12}: {value} ({value.id})')
                else:
                    print(f'{key:<12}: {value}')
            print('-' * 20)


class Warehouse:
    available_volume = 3000

    def __init__(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}'

    def transfer_to_warehouse(self, from_place: Company, equipment: OfficeEquipment):
        """Транзакция в склад"""
        to_place = self
        Storage.write(from_place, to_place, equipment)

    def transfer_from_warehouse(self, to_place: Company, equipment: OfficeEquipment):
        """Транзакция из склада"""
        from_place = self
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
    def __init__(self):
        self.id = ID(self)

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
    # Канцелярское оборудование и id
    printer1 = Printer()
    printer2 = Printer()
    xerox1 = Xerox()
    scanner = Scanner()

    # Склад, компании и транзакции
    warehouse = Warehouse()
    ooo = Company('Комус')
    # ooo.add_division('ЦАО')
    # ooo.add_division('СЗАО')
    print(ooo)

    provider = Company('Поставщик')
    print(provider)

    # Получение
    warehouse.transfer_to_warehouse(provider, Printer())
    warehouse.transfer_to_warehouse(provider, xerox1)

    # Перемеещение сущетсвующего принтера со склада в организацию
    my_printer1 = Storage.get_equipment(999)
    my_printer2 = Storage.get_equipment(2)
    warehouse.transfer_from_warehouse(ooo, my_printer2)
    Storage.show()
