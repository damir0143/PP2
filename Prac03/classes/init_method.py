# 1. Инициализация имени
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Иван")
print("Имя:", p.name)


# 2. Два параметра
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Мария", 20)
print("Студент:", s.name, s.age)


# 3. Класс автомобиля
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c = Car("BMW", 2022)
print("Машина:", c.brand, c.year)


# 4. Значение по умолчанию
class User:
    def __init__(self, username, role="user"):
        self.username = username
        self.role = role

u1 = User("admin", "administrator")
u2 = User("guest")
print(u1.username, u1.role)
print(u2.username, u2.role)


# 5. Вычисление внутри __init__
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

r = Rectangle(5, 4)
print("Площадь:", r.area)
