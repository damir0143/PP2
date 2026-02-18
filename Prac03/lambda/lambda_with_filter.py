# 1. Фильтрация чётных чисел
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print("Чётные числа:", result)


# 2. Фильтрация нечётных чисел
result = list(filter(lambda x: x % 2 != 0, numbers))
print("Нечётные числа:", result)


# 3. Фильтрация строк длиной больше 5
words = ["Python", "Hi", "Lambda", "Cat"]
result = list(filter(lambda x: len(x) > 5, words))
print("Длина > 5:", result)


# 4. Фильтрация положительных чисел
numbers = [-5, 3, -1, 8, 0]
result = list(filter(lambda x: x > 0, numbers))
print("Положительные числа:", result)


# 5. Фильтрация чисел больше 10
numbers = [5, 12, 7, 20, 3]
result = list(filter(lambda x: x > 10, numbers))
print("Числа больше 10:", result)
