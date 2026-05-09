cars = [
    {"brand": "BMW", "price": 12000},
    {"brand": "Audi", "price": 10000},
    {"brand": "Toyota", "price": 8000},
    {"brand": "Mercedes", "price": 15000}
]

print(cars)

for car in cars:
    print(car["brand"])

for car in cars:
    print(car["price"])


print("Max price cars:")
#1 way
maxCarPrice = cars[0]
for car in cars:
    if car["price"] > maxCarPrice["price"]:
        maxCarPrice = car
print(maxCarPrice)

#2 way
mostExpensiveCar = max(cars, key = lambda car: car["price"])
print(mostExpensiveCar)

print("Min price cars:")
#1 way
minCarPrice = cars[0]
for car in cars:
    if car["price"] < minCarPrice["price"]:
        minCarPrice = car
print(minCarPrice)

#2 way
mostExpensiveCar = min(cars, key = lambda car: car["price"])
print(mostExpensiveCar)

def averagePrice(cars):
    total = 0
    for car in cars:
        total += car["price"]
    return total/len(cars)

print("Average price cars:")
print(averagePrice(cars))

for car in cars:
    print(f'{car["brand"]} costs {car["price"]}$')

expensiveCar = [car for car in cars if car["price"] > 10000]
print(expensiveCar)

carsFromExpensive = sorted(cars, key = lambda car: car["price"], reverse = True)
carsFromCheapest = sorted(cars, key = lambda car: car["price"])
print(carsFromExpensive)
print(carsFromCheapest)