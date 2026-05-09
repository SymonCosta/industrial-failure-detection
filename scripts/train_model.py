import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Carregar dados
df = pd.read_csv("data/telemetry.csv")

# Converter status para valores numéricos
df["status"] = df["status"].map({
    "normal": 0,
    "critico": 1
})

# Features
X = df[[
    "temperatura",
    "vibracao",
    "pressao"
]]

# Target
y = df["status"]

# Separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Criar modelo
model = RandomForestClassifier()

# Treinar modelo
model.fit(X_train, y_train)

# Fazer previsões
predictions = model.predict(X_test)

# Relatório de avaliação
print("\nRELATÓRIO DO MODELO:\n")
print(classification_report(y_test, predictions))

# Salvar modelo treinado
joblib.dump(
    model,
    "models/failure_detection_model.pkl"
)

print("\nModelo treinado e salvo com sucesso!")