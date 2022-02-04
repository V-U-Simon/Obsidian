"""
4. Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы:
go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);

опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;

для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car():
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f"{self.color} {self.__class__.__name__}({self.name}) going")

    def stop(self):
        return print(f"{self.color} {self.__class__.__name__}({self.name}) stopped")

    def turn(self, direction):
        return print(f"{self.color} {self.__class__.__name__}({self.name}) turned to {direction}")

    def show_speed(self):
        return print(f"speed of {self.color} {self.__class__.__name__}({self.name}) is {self.speed} kilometers")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        message = (f"speed of {self.color} {self.__class__.__name__}({self.name}) is {self.speed} kilometers")
        if self.speed > 60: message += '\n-- превышение скорости'
        return print(message)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        message = (f"speed of {self.color} {self.__class__.__name__}({self.name}) is {self.speed} kilometers")
        if self.speed > 40: message += '\n-- превышение скорости'
        return print(message)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)


if __name__ == '__main__':
    # car = Car(60, 'red', 'volvo', is_police=False)

    cars = [
        (100, 'red', 'volvo', False),
        (110, 'red', 'fiat', False),
        (120, 'red', 'bmv', False),
        (130, 'red', 'ford', False),
    ]

    for car, cls in zip(cars, (TownCar, SportCar, WorkCar, PoliceCar)):
        machine = cls(*car)
        machine.go()
        machine.stop()
        machine.turn('left')
        machine.show_speed()
        print('-' * 50)
