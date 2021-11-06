"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют

параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.

Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, clothes_atr: int):
        self.clothes_atr = clothes_atr

    @abstractmethod
    def fabric_consumption(self) -> int:
        pass


class Coat(Clothes):
    def __init__(self, clothes_atr):
        super().__init__(clothes_atr)  # clothes_atr - size

    @property
    def fabric_consumption(self):
        return self.clothes_atr / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, clothes_atr):
        super().__init__(clothes_atr)  # clothes_atr - height

    @property
    def fabric_consumption(self):
        return 2 * self.clothes_atr + 0.3


if __name__ == '__main__':
    coat = Coat(100)
    suit = Suit(100)
    all_fabric_consumption = sum([obj.fabric_consumption for obj in (coat, suit)])
    print(f'{all_fabric_consumption:.2f}')
