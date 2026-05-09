import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
from sklearn.model_selection import train_test_split, GridSearchCV


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
    random_state=42,
    stratify=y
)

base_model = RandomForestClassifier(
    random_state=42
)

param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2]
}

grid_search = GridSearchCV(
    estimator=base_model,
    param_grid=param_grid,
    cv=5,
    scoring="f1",
    n_jobs=1
)

grid_search.fit(X_train, y_train)

print("Best parameters:")
print(grid_search.best_params_)

print("Best CV score:")
print(grid_search.best_score_)

best_model = grid_search.best_estimator_

predictions = best_model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy}")

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("Classification Report:")
print(classification_report(y_test, predictions))

feature_importance = pd.DataFrame({
    "feature": X.columns,
    "importance": best_model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="importance",
    ascending=False
)

print("Feature Importance:")
print(feature_importance)