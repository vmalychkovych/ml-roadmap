import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


cars = pd.read_csv("../datasets/used_cars.csv")

clean_cars = cars[
    (cars["seats"] < 10) &
    (cars["price(in lakhs)"] < 100) &
    (cars["kms_driven"] < 300000) &
    (cars["fuel_type"].isin(["Petrol", "Diesel", "CNG"]))
].copy()

clean_cars["manufacturing_year"] = pd.to_numeric(
    clean_cars["manufacturing_year"],
    errors="coerce"
)

clean_cars = clean_cars.dropna()

clean_cars["car_age"] = 2026 - clean_cars["manufacturing_year"]

clean_cars["is_expensive"] = clean_cars["price(in lakhs)"].apply(
    lambda price: 1 if price > 15 else 0
)

X = clean_cars[
    [
        "kms_driven",
        "mileage(kmpl)",
        "engine(cc)",
        "max_power(bhp)",
        "car_age"
    ]
]

y = clean_cars["is_expensive"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=50,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "../models/car_price_model.pkl")

print("Model saved successfully!")