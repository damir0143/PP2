# Пример использования *args
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


# Пример использования **kwargs
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Пример использования и *args, и **kwargs вместе
def example_function(*args, **kwargs):
    print("Позиционные аргументы (args):")
    for arg in args:
        print(arg)

    print("\nИменованные аргументы (kwargs):")
    for key, value in kwargs.items():
        print(f"{key} = {value}")


# Проверка функций
print("Сумма чисел:", sum_numbers(1, 2, 3, 4))

print("\nИнформация о пользователе:")
print_user_info(name="Анна", age=25, city="Москва")

print("\nПример функции с args и kwargs:")
example_function(10, 20, 30, name="Иван", country="Россия")
