#1
i = 1
while i <= 5:
    print(i)
    i += 1

#2
n = 10
total = 0
while n > 0:
    total += n
    n -= 1
print("Сумма:", total)

#3
count = 0
while count < 3:
    print("Привет!")
    count += 1

#4
x = 2
while x < 20:
    print(x)
    x *= 2

#5
password = ""
while password != "secret":
    password = input("Введите пароль: ")
print("Пароль верный!")
