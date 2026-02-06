#1 Проверка возраста и допуска
age = 20
has_ticket = True
can_enter = bool(age >= 18 and has_ticket)
print(can_enter)  # True, возраст >=18 и билет есть

#2 Проверка имени и статуса
name = "Alice"
is_admin = False
access = bool(name == "Alice" or is_admin)
print(access)  # True, имя Alice или админ

#3 Логическое НЕ
is_raining = True
stay_home = bool(not is_raining)
print(stay_home)  # False, идёт дождь

#4 Сложное логическое выражение
x = 5
y = 10
z = 15
result = bool((x < y and y < z) or x == z)
print(result)  # True, x<y<z

#5 Проверка делимости и диапазона
number = 12
check = bool((number % 2 == 0) and (number > 10 and number < 20))
print(check)  # True, число чётное и в диапазоне 10-20
