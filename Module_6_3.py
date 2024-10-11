class PrintDouble:
    def __init__(self):
        print(f"\n")


class TestNumber:
    def __init__(self, test_number):
        self.test_number = test_number
        print(f"Тест: {test_number}")


class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = "Frrr"

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = "I train, eat, sleep, and repeat"

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


#Тест_Horse
TestNumber(1)
my_horse = Horse()
print(my_horse.x_distance)
print(my_horse.sound)
my_horse.run(10)
print(my_horse.x_distance)
my_horse.run(15)
print(my_horse.x_distance)
PrintDouble()

# Тест_Eagle
TestNumber(2)
my_eagle = Eagle()
print(my_eagle.y_distance)
print(my_eagle.sound)
my_eagle.fly(39)
print(my_eagle.y_distance)
PrintDouble()

# Задание
print("Задание урока")
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
