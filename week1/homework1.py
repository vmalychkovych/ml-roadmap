phones = [
    {"brand": "iPhone", "price": 900},
    {"brand": "Samsung", "price": 700},
    {"brand": "Xiaomi", "price": 500},
    {"brand": "Google Pixel", "price": 800}
]

for phone in phones:
    print(phone["brand"])

for phone in phones:
    print(phone["price"])

mostExpensivePhone = max(phones, key=lambda phone: phone["price"])
print(mostExpensivePhone)

cheapestPhone = min(phones, key=lambda phone: phone["price"])
print(cheapestPhone)

def average_price(price_list):
    return sum(phone["price"] for phone in price_list) / len(price_list)

print(f'Average price - {average_price(phones)}')

expensivePhones = [phone for phone in phones if phone["price"] > 750]
print(expensivePhones)

phonesFromExpensive = sorted(phones, key=lambda phone: phone["price"], reverse=True)
print(phonesFromExpensive)
