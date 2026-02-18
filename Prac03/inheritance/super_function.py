# 1. Использование super() в __init__
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Иван", 5)
print(s.name, s.grade)


# 2. Добавление нового поведения
class Animal:
    def speak(self):
        return "Звук"

class Dog(Animal):
    def speak(self):
        return super().speak() + " Гав!"

d = Dog()
print(d.speak())


# 3. Наследование с расширением
class Employee:
    def __init__(self, salary):
        self.salary = salary

class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

m = Manager(50000, 10000)
print("Доход:", m.salary + m.bonus)


# 4. Вызов метода родителя
class Shape:
    def area(self):
        return "Площадь неизвестна"

class Rectangle(Shape):
    def area(self):
        return super().area() + " (переопределяется)"

r = Rectangle()
print(r.area())


# 5. Многоуровневое наследование
class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return super().hello() + " -> B"

class C(B):
    def hello(self):
        return super().hello() + " -> C"

c = C()
print(c.hello())
