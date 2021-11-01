"""
5. Реализовать класс Stationery (канцелярская принадлежность).

определить в нём атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw.
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery():
    title = 'Stationery'

    def draw(self):
        return print(f'Запуск отрисовки {self.title}')


class Pen():
    title = 'Pen'

    def draw(self):
        return print(f'Запуск отрисовки {self.title}')


class Pencil():
    title = 'Pencil'

    def draw(self):
        return print(f'Запуск отрисовки {self.title}')


class Handle():
    title = 'Handle'

    def draw(self):
        return print(f'Запуск отрисовки {self.title}')


if __name__ == '__main__':
    pass

for cls in (Stationery, Pen, Pencil, Handle):
    cls().draw()
