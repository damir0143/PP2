# 1. Сортировка чисел по возрастанию
numbers = [5, 2, 9, 1]
result = sorted(numbers, key=lambda x: x)
print("По возрастанию:", result)


# 2. Сортировка чисел по убыванию
result = sorted(numbers, key=lambda x: x, reverse=True)
print("По убыванию:", result)


# 3. Сортировка строк по длине
words = ["apple", "kiwi", "banana", "fig"]
result = sorted(words, key=lambda x: len(x))
print("По длине:", result)


# 4. Сортировка списка кортежей по второму элементу
pairs = [(1, 3), (2, 1), (4, 2)]
result = sorted(pairs, key=lambda x: x[1])
print("По второму элементу:", result)


# 5. Сортировка слов по последней букве
words = ["cat", "dog", "elephant", "bee"]
result = sorted(words, key=lambda x: x[-1])
print("По последней букве:", result)
