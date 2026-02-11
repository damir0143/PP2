# 1. Возвращает сумму двух чисел
def add(a, b):
    return a + b


# 2. Возвращает квадрат числа
def square(num):
    return num * num


# 3. Возвращает большее из двух чисел
def maximum(a, b):
    if a > b:
        return a
    else:
        return b


# 4. Возвращает приветственное сообщение
def greet(name):
    return "Привет, " + name + "!"


# 5. Возвращает True, если число чётное
def is_even(num):
    return num % 2 == 0


# Проверка функций
print(add(3, 4))        # 7
print(square(5))        # 25
print(maximum(10, 7))   # 10
print(greet("Алиса"))   # Привет, Алиса!
print(is_even(8))       # True
print(is_even(5))       # False
