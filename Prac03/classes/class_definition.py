# 1. Простой класс
class Person:
    pass

p = Person()
print("Объект класса Person создан:", p)


# 2. Класс с методом
class Dog:
    def bark(self):
        return "Гав!"

d = Dog()
print("Собака говорит:", d.bark())


# 3. Класс с атрибутом
class Car:
    brand = "Toyota"

c = Car()
print("Марка машины:", c.brand)


# 4. Класс с несколькими методами
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print("Сложение:", calc.add(3, 4))
print("Умножение:", calc.multiply(3, 4))


# 5. Класс с методом приветствия
class Greeter:
    def greet(self, name):
        return f"Привет, {name}!"

g = Greeter()
print(g.greet("Анна"))
