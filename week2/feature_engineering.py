import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

cars = pd.read_csv('../datasets/used_cars.csv')
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

clean_cars["power_per_engine"] = clean_cars["max_power(bhp)"] / clean_cars["engine(cc)"]

encoded_cars = pd.get_dummies(
    clean_cars,
    columns=["fuel_type", "transmission"],
    drop_first=True
)

features = [
    "kms_driven",
    "mileage(kmpl)",
    "engine(cc)",
    "max_power(bhp)",
    "car_age",
    "power_per_engine",
    "fuel_type_Diesel",
    "fuel_type_Petrol",
    "transmission_Manual"
]

X = encoded_cars[features]
y = encoded_cars["price(in lakhs)"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions[:10])

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"R2 Score: {r2}")

feature_importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="importance",
    ascending=False
)

print(feature_importance)