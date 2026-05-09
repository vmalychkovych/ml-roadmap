import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cars = pd.read_csv('../datasets/used_cars.csv')
clean_cars = cars[
    (cars["seats"] < 10) &
    (cars["price(in lakhs)"] < 100) &
    (cars["kms_driven"] < 300000) &
    (cars["fuel_type"].isin(["Petrol", "Diesel", "CNG"]))
]

plt.hist(clean_cars["price(in lakhs)"])
plt.show()

fuel_counts = clean_cars["fuel_type"].value_counts()
plt.bar(fuel_counts.index, fuel_counts.values)
plt.show()

plt.scatter(
    clean_cars["kms_driven"],
    clean_cars["price(in lakhs)"]
)
plt.show()

sns.boxplot(
    x="fuel_type",
    y="price(in lakhs)",
    data=clean_cars
)
plt.show()

numeric_cars = clean_cars.select_dtypes(include=["float64", "int64"])
correlation = numeric_cars.corr()
sns.heatmap(correlation)
plt.show()