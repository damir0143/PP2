#1
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

#2
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print("Нечетное число:", n)

#3
i = 0
while i < 5:
    i += 1
    if i == 2 or i == 4:
        continue
    print("i =", i)

#4
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print("Count:", count)

#5
x = 1
while x <= 10:
    x += 1
    if x % 3 == 0:
        continue
    print("x =", x)
