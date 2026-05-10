from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Carregar modelo
model = joblib.load(
    "models/failure_detection_model.pkl"
)

@app.get("/")
def home():
    return {
        "message": "Industrial Failure Detection API"
    }

@app.post("/predict")
def predict(
    temperatura: float,
    vibracao: float,
    pressao: float
):

    data = pd.DataFrame([{
        "temperatura": temperatura,
        "vibracao": vibracao,
        "pressao": pressao
    }])

    prediction = model.predict(data)

    result = (
        "critico"
        if prediction[0] == 1
        else "normal"
    )

    return {
        "prediction": result
    }