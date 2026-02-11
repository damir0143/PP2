# function_arguments.py

# 1. Обычные (позиционные) аргументы
def greet(name):
    print("1) Привет,", name)

greet("Анна")


# 2. Несколько аргументов
def add(a, b):
    result = a + b
    print("2) Сумма:", result)

add(5, 3)


# 3. Аргументы по умолчанию
def greet_default(name="Гость"):
    print("3) Привет,", name)

greet_default()
greet_default("Иван")


# 4. Именованные аргументы
def introduce(name, age):
    print("4) Имя:", name)
    print("   Возраст:", age)

introduce(age=25, name="Ольга")


# 5. Произвольное количество аргументов (*args)
def sum_all(*numbers):
    total = sum(numbers)
    print("5) Сумма всех чисел:", total)

sum_all(1, 2, 3, 4)
