#1 Проверка диапазона
age = 25
print(age >= 18 and age <= 30)  # True, возраст между 18 и 30

#2 Сравнение строк
name = "Alice"
print(name == "Alice" or name == "Bob")  # True, имя Alice

#3 Проверка остатка от деления
number = 15
print(number % 2 == 0)  # False, 15 нечетное

#4 Сравнение нескольких чисел
x = 10
y = 20
z = 10
print(x == z and y > x)  # True, x=z и y>x

#5 Сложная логическая проверка
score = 85
passed = score >= 60
excellent = score >= 90
print(passed and not excellent)  # True, прошел, но не отлично
