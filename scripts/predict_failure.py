import joblib
import pandas as pd

# Carregar modelo treinado
model = joblib.load(
    "models/failure_detection_model.pkl"
)

# Novo dado de telemetria
new_data = pd.DataFrame([{
    "temperatura": 70,
    "vibracao": 1.5,
    "pressao": 50
}])

# Fazer previsão
prediction = model.predict(new_data)

# Interpretar resultado
if prediction[0] == 1:
    print("\nALERTA: Equipamento crítico!")
else:
    print("\nEquipamento operando normalmente.")