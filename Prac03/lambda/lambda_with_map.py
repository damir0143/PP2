# 1. Умножение каждого числа на 2
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print("Умножение на 2:", result)


# 2. Преобразование строк в верхний регистр
words = ["apple", "banana", "cherry"]
result = list(map(lambda x: x.upper(), words))
print("Верхний регистр:", result)


# 3. Получение длины каждой строки
words = ["Python", "Lambda", "Map"]
result = list(map(lambda x: len(x), words))
print("Длина строк:", result)


# 4. Возведение чисел в квадрат
numbers = [2, 4, 6, 8]
result = list(map(lambda x: x ** 2, numbers))
print("Квадраты чисел:", result)


# 5. Преобразование строк в числа
numbers_str = ["10", "20", "30"]
result = list(map(lambda x: int(x), numbers_str))
print("Строки в числа:", result)
