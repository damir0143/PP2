# 1. Общая переменная класса
class Dog:
    species = "Canis familiaris"

d1 = Dog()
d2 = Dog()
print("Вид:", d1.species)
print("Вид:", d2.species)


# 2. Подсчёт созданных объектов
class Person:
    count = 0

    def __init__(self):
        Person.count += 1

p1 = Person()
p2 = Person()
print("Количество объектов:", Person.count)


# 3. Общий процент налога
class Product:
    tax = 0.2

    def __init__(self, price):
        self.price = price

    def price_with_tax(self):
        return self.price * (1 + Product.tax)

item = Product(100)
print("Цена с налогом:", item.price_with_tax())


# 4. Изменение переменной класса
class Company:
    country = "USA"

print("Страна до изменения:", Company.country)
Company.country = "Germany"
print("Страна после изменения:", Company.country)


# 5. Использование class variable в методе
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

circle = Circle(3)
print("Площадь круга:", circle.area())
