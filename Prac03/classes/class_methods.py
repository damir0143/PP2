# 1. Обычный метод
class Person:
    def say_hello(self):
        return "Здравствуйте!"

p = Person()
print(p.say_hello())


# 2. Метод изменяет состояние объекта
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c = Counter()
c.increment()
print("Счётчик:", c.count)


# 3. Метод с параметрами
class Math:
    def power(self, base, exp):
        return base ** exp

m = Math()
print("Степень:", m.power(2, 3))


# 4. Метод возвращает строку с данными объекта
class Book:
    def __init__(self, title):
        self.title = title

    def info(self):
        return f"Книга: {self.title}"

b = Book("Python для начинающих")
print(b.info())


# 5. Класс-банковский счёт
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(1000)
account.deposit(500)
print("Баланс:", account.balance)
