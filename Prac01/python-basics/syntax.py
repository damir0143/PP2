#1
# Простейший вывод
print("Hello, Python!")

#2
# Объявление и использование переменных
x = 10
y = 5
z = x + y
print("Сумма:", z)

#3
# Использование условного оператора
age = 18
if age >= 18:
    print("Взрослый")
else:
    print("Ребенок")

#4
# Определение функции и вызов
def greet(name):
    return f"Привет, {name}!"

print(greet("Alice"))

#5
# Цикл for и список
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Я люблю", fruit)
