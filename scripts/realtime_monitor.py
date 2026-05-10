import random
import time
import joblib
import pandas as pd
from datetime import datetime

# Carregar modelo treinado
model = joblib.load(
    "models/failure_detection_model.pkl"
)

print("\nIniciando monitoramento industrial...\n")

while True:

    # Simular sensores
    temperatura = random.randint(60, 120)
    vibracao = round(random.uniform(0.1, 5.0), 2)
    pressao = random.randint(20, 100)

    # Criar dataframe
    data = pd.DataFrame([{
        "temperatura": temperatura,
        "vibracao": vibracao,
        "pressao": pressao
    }])

    # Fazer previsão
    prediction = model.predict(data)

    status = (
        "CRITICO"
        if prediction[0] == 1
        else "NORMAL"
    )

    # Timestamp
    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Exibir resultado
    print(
        f"[{timestamp}] "
        f"Temp={temperatura}°C | "
        f"Vib={vibracao} | "
        f"Pressão={pressao} | "
        f"STATUS={status}"
    )

    # Intervalo
    time.sleep(2)