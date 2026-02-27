#you have json file "car.json" там будут данные про машины например бренд модель и цена, 
# 4 машины достаточно. клиент пришел ипишет бренд и модель машины в терминал, я должен посмотреть есть ли такая машщина в этом json файле , 
# если есть то вывести цену,если нет то вывести что такой машины нет в салоне
# добавить когда человек напишет в терминал i have finished то программа завершится и создатся новый json
#file с название pricelist в котором будут все машины которые есть в салоне и их ввел клиент и их общая цена
import json
with open("car.json", "r", encoding="utf-8") as file:
    cars = json.load(file)
selected_cars = []
total_price = 0
while True:
    brand_input = input("Введите бренд машины (или 'i have finished' для выхода): ").strip()
    if brand_input.lower() == "i have finished":
        break
    model_input = input("Введите модель машины: ").strip()
    found = False
    for car in cars:
        if car["brand"].lower() == brand_input.lower() and \
           car["model"].lower() == model_input.lower():
            print(f"Цена автомобиля: {car['price']}$")
            selected_cars.append(car)
            total_price += car["price"]
            found = True
            break
    if not found:
        print("Такой машины нет в салоне")
pricelist = {
    "selected_cars": selected_cars,
    "total_price": total_price
}

with open("pricelist.json", "w", encoding="utf-8") as file:
    json.dump(pricelist, file, indent=4, ensure_ascii=False)

print("Программа завершена")
print(f"Общая стоимость выбранных машин: {total_price}$")