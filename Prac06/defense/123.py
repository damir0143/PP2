import os
from functools import reduce

folder = "sales"
product_dict = {}

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    with open(path, "r") as f:
        for line in f:
            name, qty = line.strip().split(",")
            qty = int(qty)

            if name in product_dict:
                product_dict[name] += qty
            else:
                product_dict[name] = qty


products = list(product_dict.items())


total_records = len(products)
total_quantity = sum(q for _, q in products)
average = total_quantity / total_records if total_records else 0

max_product = max(products, key=lambda x: x[1])
min_product = min(products, key=lambda x: x[1])

increased = list(map(lambda x: (x[0], x[1] + 2), products))
filtered = list(filter(lambda x: x[1] > 5, products))

product_all = reduce(lambda a, b: a * b, [q for _, q in products], 1)

print()
for i, (name, qty) in enumerate(products, start=1):
    print(i, name, qty)

names = [name for name, _ in products]
quantities = [qty for _, qty in products]
zipped = list(zip(names, quantities))

sorted_products = sorted(products, key=lambda x: x[1])


with open("sales_report.txt", "w") as f:
    f.write(f"Total records: {total_records}\n")
    f.write(f"Average quantity sold: {average:.2f}\n")
    f.write(f"Highest quantity sold: {max_product[1]}\n")
    f.write(f"Lowest quantity sold: {min_product[1]}\n\n")

    f.write("Popular products:\n")
    for name, qty in filtered:
        f.write(f"{name} {qty}\n")