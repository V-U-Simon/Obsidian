"""
2. Реализовать класс Road (дорога).

определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;

определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу:
длина *
ширина *
масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см *
число см толщины полотна;

проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road():

    def __init__(self, length, width, weight_for_one_sq_meter, thickness):
        self._length = length
        self._width = width
        self._weight_for_one_sq_meter = weight_for_one_sq_meter / 1000
        self._thickness = thickness


    def get_asphalt(self):
        return self._length * self._width * self._weight_for_one_sq_meter * self._thickness

if __name__ == '__main__':
    r = Road(20, 5000, 25, 5)
    print(r.get_asphalt())