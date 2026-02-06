#1
for i in range(10):
    if i == 5:
        break
    print(i)

#2
for letter in "Python":
    if letter == "h":
        break
    print(letter)

#3
numbers = [1, 3, 5, 7, 9]
for n in numbers:
    if n > 5:
        break
    print(n)

#4
for i in range(1, 20):
    if i % 7 == 0:
        print("Нашли кратное 7:", i)
        break

#5
names = ["Alice", "Bob", "Charlie"]
for name in names:
    if name == "Bob":
        break
    print(name)
