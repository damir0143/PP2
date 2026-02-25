#1 date.md
from datetime import datetime, date, timedelta


# 1. Вычесть пять дней из текущей даты

today_dt = datetime.now()
five_days_ago = today_dt - timedelta(days=5)
print("1. Today:", today_dt)
print("   Five days ago:", five_days_ago)
print("-----")


# 2. Вывести вчера, сегодня, завтра

today_d = date.today()
yesterday = today_d - timedelta(days=1)
tomorrow = today_d + timedelta(days=1)
print("2. Yesterday:", yesterday)
print("   Today:", today_d)
print("   Tomorrow:", tomorrow)
print("-----")


# 3. Убрать микросекунды из datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)
print("3. Original datetime:", now)
print("   Without microseconds:", no_microseconds)
print("-----")


# 4. Вычислить разницу между двумя датами в секундах

dt1 = datetime(2026, 2, 25, 12, 0, 0)
dt2 = datetime(2026, 2, 26, 14, 30, 0)
diff = dt2 - dt1
seconds = diff.total_seconds()
print("4. Difference in seconds:", seconds)

#2 generators.md
# 1. Генератор квадратов чисел до N
def squares_upto_n(n):
    for i in range(n+1):
        yield i * i

print("1. Squares up to N:")
N = 5
for sq in squares_upto_n(N):
    print(sq)
print("-----")

# 2. Генератор чётных чисел от 0 до n (ввод с консоли)
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("2. Enter n for even numbers: "))
print("Even numbers:", ",".join(str(num) for num in even_numbers(n)))
print("-----")

# 3. Генератор чисел, делящихся на 3 и 4, от 0 до n
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n_div = 50
print("3. Numbers divisible by 3 and 4 up to 50:")
for num in divisible_by_3_and_4(n_div):
    print(num)
print("-----")

# 4. Генератор квадратов чисел от a до b
def squares(a, b):
    for i in range(a, b+1):
        yield i * i

print("4. Squares from a to b (3 to 7):")
for value in squares(3, 7):
    print(value)
print("-----")

# 5. Генератор чисел от n до 0
def countdown(n):
    for i in range(n, -1, -1):
        yield i

print("5. Countdown from 10 to 0:")
for num in countdown(10):
    print(num)

#3 math.md
import math

# 1. Конвертация градусов в радианы
degree = 15
radian = math.radians(degree)
print("1. Convert degree to radian:")
print("Degree:", degree)
print("Radian:", radian)
print("-----")

# 2. Вычисление площади трапеции
height = 5
base1 = 5
base2 = 6
area_trapezoid = 0.5 * (base1 + base2) * height
print("2. Area of trapezoid:")
print("Height:", height)
print("Base1:", base1, "Base2:", base2)
print("Area:", area_trapezoid)
print("-----")

# 3. Вычисление площади правильного многоугольника
num_sides = 4
side_length = 25
area_polygon = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
print("3. Area of regular polygon:")
print("Number of sides:", num_sides)
print("Length of side:", side_length)
print("Area of polygon:", area_polygon)
print("-----")

# 4. Вычисление площади параллелограмма
base_parallelogram = 5
height_parallelogram = 6
area_parallelogram = base_parallelogram * height_parallelogram
print("4. Area of parallelogram:")
print("Base:", base_parallelogram)
print("Height:", height_parallelogram)
print("Area:", area_parallelogram)

#5 json.md
import json

# Загружаем данные из файла sample-data.json
with open("sample-data.json") as f:
    data = json.load(f)

# Печатаем заголовок
print("Interface Status")
print("=" * 79)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-" * 50, "-" * 20, "-" * 6, "-" * 6)

# Предположим, что интерфейсы находятся по пути data['imdata']
for interface in data.get('imdata', []):
    # Получаем информацию об интерфейсе
    intf = interface.get('l1PhysIf', {})
    dn = intf.get('dn', '')
    descr = intf.get('descr', '')
    speed = intf.get('speed', '')
    mtu = intf.get('mtu', '')
    
    # Выводим строку таблицы с форматированием
    print(f"{dn:<50} {descr:<20} {speed:<6} {mtu:<6}")