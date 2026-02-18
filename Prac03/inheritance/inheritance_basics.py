# 1. Простое наследование
class Animal:
    def speak(self):
        return "Животное издает звук"

class Dog(Animal):
    pass

d = Dog()
print(d.speak())


# 2. Наследование с добавлением метода
class Vehicle:
    def move(self):
        return "Транспорт движется"

class Car(Vehicle):
    def honk(self):
        return "Бип-бип!"

c = Car()
print(c.move())
print(c.honk())


# 3. Наследование атрибутов
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        return f"{self.name} учится"

s = Student("Анна")
print(s.study())


# 4. Проверка типа
class Bird:
    pass

class Eagle(Bird):
    pass

e = Eagle()
print(isinstance(e, Bird))


# 5. Доступ к методу родителя
class Parent:
    def greet(self):
        return "Привет от родителя"

class Child(Parent):
    pass

child = Child()
print(child.greet())
