#1
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1

#2
while True:
    word = input("Введите слово: ")
    if word == "exit":
        break
    print("Вы ввели:", word)

#3
x = 0
while True:
    x += 1
    if x % 7 == 0:
        print("Нашли число, делящееся на 7:", x)
        break

#4
count = 0
while True:
    count += 1
    if count > 3:
        break
    print("Счет:", count)

#5
while True:
    age = int(input("Введите возраст: "))
    if age >= 18:
        print("Доступ разрешен")
        break
