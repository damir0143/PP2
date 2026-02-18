# 1. Простое переопределение
class Animal:
    def speak(self):
        return "Звук"

class Cat(Animal):
    def speak(self):
        return "Мяу"

c = Cat()
print(c.speak())


# 2. Переопределение с super()
class Person:
    def introduce(self):
        return "Я человек"

class Student(Person):
    def introduce(self):
        return super().introduce() + " и студент"

s = Student()
print(s.introduce())


# 3. Изменение логики метода
class Calculator:
    def calculate(self, a, b):
        return a + b

class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        return a * b

calc = AdvancedCalculator()
print(calc.calculate(3, 4))


# 4. Переопределение с проверкой
class Vehicle:
    def speed(self):
        return 60

class SportsCar(Vehicle):
    def speed(self):
        return 200

car = SportsCar()
print("Скорость:", car.speed())


# 5. Разные реализации
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

shape = Circle()
print("Площадь круга:", shape.area())
