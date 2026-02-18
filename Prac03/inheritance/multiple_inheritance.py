# 1. Простое множественное наследование
class A:
    def method_a(self):
        return "Метод A"

class B:
    def method_b(self):
        return "Метод B"

class C(A, B):
    pass

c = C()
print(c.method_a())
print(c.method_b())


# 2. Конфликт методов (MRO)
class X:
    def hello(self):
        return "X"

class Y:
    def hello(self):
        return "Y"

class Z(X, Y):
    pass

z = Z()
print(z.hello())  # Будет вызван метод X


# 3. Использование super() при множественном наследовании
class Base:
    def greet(self):
        return "Base"

class Left(Base):
    def greet(self):
        return super().greet() + " -> Left"

class Right(Base):
    def greet(self):
        return super().greet() + " -> Right"

class Child(Left, Right):
    def greet(self):
        return super().greet() + " -> Child"

child = Child()
print(child.greet())


# 4. Наследование атрибутов из двух классов
class Father:
    def skill1(self):
        return "Программирование"

class Mother:
    def skill2(self):
        return "Дизайн"

class Child(Father, Mother):
    pass

kid = Child()
print(kid.skill1())
print(kid.skill2())


# 5. Проверка порядка разрешения методов
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
