import random


class Vehicle:
    __COLORE_VARIANTS = ["red", "orange", "green", "blue", "pink", "white", "black", "yellow"]
    color = random.choice(__COLORE_VARIANTS)

    marks_variable = ["BMW", "Ferrari", "VAZ", "FIAT", "Chevrolet", "Lamborghini",
                      "Volvo", "Reno", "Mercedes-Benz", "Opel", "Cherry", "Nissan",
                      "Subaru", "Porsche", "Lexus", "Audi", "UAZ", "Toyota", "Mitsubishi"]
    marks = random.choice(marks_variable)

    def __init__(self, owner, __model, __color, __engine_power):
        if __color is None:
            __color = Vehicle.color
        else:
            pass
        if __model is None:
            __model = Vehicle.marks

        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def set_color(self, new_color):
        if new_color.lower() in self.__COLORE_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на: {new_color}")

    def get_model(self):
        if self.__model == Vehicle.marks:
            print(f"Марка: {self.__model}")
        else:
            print(f"Модель: {self.__model}")

    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        print(f"Цвет транспорта: {self.__color}")

    def print_info(self):
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f"Владелец: {self.owner}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Brown')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

print(f"\n"
      f"##### Тест ####")

# Тест
vehicle2 = Sedan('Mark_Avrely', None, None, 500)

vehicle2.print_info()
