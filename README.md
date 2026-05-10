# Detecção de Falhas Industriais com Machine Learning

## Visão Geral

Este projeto simula uma solução de monitoramento industrial utilizando Machine Learning para identificar condições operacionais críticas em equipamentos industriais.

A solução foi desenvolvida para representar cenários reais de analytics industrial encontrados em operações de mineração, ferrovia, porto, logística e manufatura.

O pipeline contempla:
- Geração de dados de telemetria
- Processamento de dados
- Treinamento de modelo de Machine Learning
- Predição de falhas operacionais
- Analytics operacional

---

## Problema de Negócio

Ambientes industriais geram grandes volumes de dados operacionais provenientes de sensores, máquinas e sistemas de telemetria.

Este projeto demonstra como Inteligência Artificial pode ser aplicada para:
- Detectar comportamentos operacionais anormais
- Identificar condições críticas de equipamentos
- Apoiar estratégias de manutenção preditiva
- Melhorar a confiabilidade operacional

---

## Tecnologias Utilizadas

- Python
- Pandas
- Scikit-Learn
- Joblib
- AWS S3
- AWS Athena
- SQL
- Git & GitHub

---

## Arquitetura do Projeto

```text
Dados de Telemetria
        ↓
Dataset CSV
        ↓
Processamento de Dados
        ↓
Treinamento do Modelo
        ↓
Modelo de Detecção de Falhas
        ↓
Predição Operacional
```

---

## Estrutura do Projeto

```text
industrial-failure-detection/
│
├── data/
│   └── telemetry.csv
│
├── models/
│   └── failure_detection_model.pkl
│
├── notebooks/
│
├── scripts/
│   ├── train_model.py
│   └── predict_failure.py
│
├── requirements.txt
│
└── README.md
```

---

## Modelo de Machine Learning

O projeto utiliza um modelo Random Forest Classifier para identificar padrões de risco operacional com base em:
- Temperatura
- Vibração
- Pressão

Classificação alvo:
- Normal
- Crítico

---

## Exemplo de Predição

Condição operacional crítica:

```python
{
    "temperatura": 115,
    "vibracao": 4.5,
    "pressao": 90
}
```

Resultado da previsão:

```text
ALERTA: Equipamento crítico!
```

---

## Próximas Evoluções

- Streaming de telemetria em tempo real
- Integração com AWS Glue
- Dashboards operacionais
- Deploy de API
- Detecção avançada de anomalias
- Integração com visão computacional

---

## Autor

Symon Costta

Analytics | IA Aplicada | Engenharia de Dados | AWS | Python | SQL