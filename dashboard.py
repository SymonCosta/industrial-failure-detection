import streamlit as st
import random
import time
import pandas as pd
import joblib
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Industrial Monitoring",
    layout="wide"
)

# Carregar modelo
model = joblib.load(
    "models/failure_detection_model.pkl"
)

# Título
st.title("Monitoramento Industrial Inteligente")

st.markdown("""
Dashboard de monitoramento operacional com IA aplicada para detecção de falhas industriais.
""")

# Linha operacional
status_line = st.empty()

# Containers
chart = st.empty()
table = st.empty()
alert = st.empty()

# Histórico
history = []
critical_count = 0

while True:

    # Simulação de sensores
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

    # Contador de eventos críticos
    if status == "CRITICO":
        critical_count += 1

    # Timestamp
    timestamp = datetime.now().strftime(
        "%H:%M:%S"
    )

    # Linha do histórico
    row = {
        "horario": timestamp,
        "temperatura": temperatura,
        "vibracao": vibracao,
        "pressao": pressao,
        "status": status
    }

    history.append(row)

    # Converter histórico para dataframe
    df = pd.DataFrame(history)

    # Linha operacional superior
    status_line.info(
        f"""
        Última leitura operacional |
        Temperatura: {temperatura} °C |
        Vibração: {vibracao} |
        Pressão: {pressao} |
        Status: {status} |
        Eventos Críticos: {critical_count}
        """
    )

    # ALERTA
    if status == "CRITICO":
        alert.error(
            "ALERTA CRÍTICO DETECTADO!"
        )
    else:
        alert.success(
            "Operação Normal"
        )

    # Gráfico em tempo real
    chart.line_chart(
        df[[
            "temperatura",
            "vibracao",
            "pressao"
        ]]
    )

    # Tabela histórica
    table.dataframe(
        df.tail(15),
        use_container_width=True
    )

    # Intervalo de atualização
    time.sleep(2)