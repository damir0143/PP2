#1 The min() and max() functions can be used to find the lowest or highest value in an iterable:
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#2 The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)

print(x)

#3 The pow(x, y) function returns the value of x to the power of y (x^y)
x = pow(4, 3)

print(x)

#4 When you have imported the math module, you can start using methods and constants of the module.
#The math.sqrt() method for example, returns the square root of a number:
#После импорта математического модуля вы можете начать использовать методы и константы модуля.
#Например, метод math.sqrt() возвращает квадратный корень числа:
import math

x = math.sqrt(64)

print(x)

#5 The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
# Метод math.ceil() округляет число вверх до ближайшего целого числа, а метод math.floor() округляет число вниз до ближайшего целого числа и возвращает результат:
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#6  The math.pi constant, returns the value of PI (3.14...):
#константа math.pi возвращает значение PI (3.14...):
import math

x = math.pi

print(x)

import random

# 7. random() — случайное число от 0 до 1
print("random():", random.random())

# 8. randint(a, b) — случайное целое число от a до b включительно
print("randint(1, 10):", random.randint(1, 10))

# 9. choice(seq) — случайный элемент из последовательности
items = ['apple', 'banana', 'cherry']
print("choice:", random.choice(items))

# 10. shuffle(seq) — перемешивание списка на месте
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print("shuffled deck:", deck)