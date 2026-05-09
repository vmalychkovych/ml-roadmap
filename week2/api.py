import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

model = joblib.load("models/car_price_model.pkl")


class CarFeatures(BaseModel):
    kms_driven: int
    mileage: float
    engine: float
    max_power: float
    car_age: int


@app.get("/")
def home():
    return {"message": "Car Price ML API"}


@app.post("/predict")
def predict(car: CarFeatures):

    data = pd.DataFrame([
        {
            "kms_driven": car.kms_driven,
            "mileage(kmpl)": car.mileage,
            "engine(cc)": car.engine,
            "max_power(bhp)": car.max_power,
            "car_age": car.car_age
        }
    ])

    prediction = model.predict(data)[0]

    return {
        "prediction": int(prediction),
        "result": (
            "Expensive Car"
            if prediction == 1
            else "Cheap Car"
        )
    }