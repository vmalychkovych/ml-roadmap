import pandas as pd

cars = pd.read_csv('../datasets/used_cars.csv')
print(cars)
print(cars.head(5))
print(cars.tail(5))
print(cars.info())
print(cars.describe())
print(cars.columns)
print(cars["manufacturing_year"])

print(f'Average price - {cars["price(in lakhs)"].mean()}')
print(f'Max price - {cars["price(in lakhs)"].max()}')
print(f'Min price - {cars["price(in lakhs)"].min()}')

diesel_cars = cars[cars["fuel_type"] == "Diesel"]
print(f'Diesel cars\n{diesel_cars}')

automatic_cars = cars[cars["transmission"] == "Automatic"]
print(f'Automatic cars\n{automatic_cars}')

auto_after_2020 = cars[
    pd.to_numeric(cars["manufacturing_year"], errors="coerce") > 2020
]
print(f'Auto after 2020\n{auto_after_2020}')

expensive_auto = cars[
    pd.to_numeric(cars["price(in lakhs)"], errors="coerce") > 160
]
print(f'Expensive auto\n{expensive_auto}')

bad_seats = cars[cars["seats"] > 10]
print(bad_seats)

very_expensive_cars = cars[cars["price(in lakhs)"] > 100]
print(very_expensive_cars)

suspicious_kms = cars[cars["kms_driven"] > 300000]
print(suspicious_kms)

missing_values = cars.isnull().sum()
print(missing_values)

clean_cars = cars[
    (cars["seats"] < 10) &
    (cars["price(in lakhs)"] < 100)
]
print(clean_cars)

most_expensive_cars = clean_cars.sort_values(by="price(in lakhs)", ascending=False)
print(most_expensive_cars)

cheapest_cars = clean_cars.sort_values(by="price(in lakhs)")
print(cheapest_cars)

fuel_type_counts = clean_cars["fuel_type"].value_counts()
print(fuel_type_counts)

automatic_avg_price = clean_cars[
    clean_cars["transmission"] == "Automatic"
]["price(in lakhs)"].mean()

print(f"Average automatic price: {automatic_avg_price}")

diesel_avg_price = clean_cars[
    clean_cars["fuel_type"] == "Diesel"
]["price(in lakhs)"].mean()

print(f"Average diesel price: {diesel_avg_price}")