# 12.2.py
import json

try:
    with open('products.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    data = {"products": []}

print("Добавление нового продукта:")
name = input("Название: ")
price = int(input("Цена: "))
weight = int(input("Вес: "))
available = input("В наличии (да/нет): ").lower() == 'да'

new_product = {
    "name": name,
    "price": price,
    "weight": weight,
    "available": available
}

data['products'].append(new_product)

with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("\nОбновленный список продуктов:")
for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    print("В наличии" if product['available'] else "Нет в наличии!")
    print()
