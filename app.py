import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AeroPredict", layout="wide")
st.title("🔧 AeroPredict – Predicción Inteligente de Mantenimiento Aéreo")

# Introducción
st.markdown("""
### ¿Qué es AeroPredict?
AeroPredict es una solución basada en IA que permite predecir fallos y necesidades de mantenimiento antes de que ocurran, reduciendo costes y mejorando la disponibilidad de la flota.

Esta demo muestra cómo se ingieren datos, se procesan con modelos predictivos, y se entregan alertas e informes útiles para técnicos de mantenimiento.
""")

# Simulación de Ingreso de Datos
st.header("📥 Datos de Entrada del Sistema")
data = {
    'ID Avión': ['A320-ES123'],
    'Horas de vuelo': [14320],
    'Ciclos de despegue': [7250],
    'Temp. promedio motor (°C)': [635],
    'Vibración eje (Hz)': [42.1],
    'Último mantenimiento (días)': [89]
}
df = pd.DataFrame(data)
st.dataframe(df)

# IA Predictiva
st.header("🧠 Módulo de IA Predictiva")
st.markdown("""
El sistema utiliza modelos de supervivencia y detección de anomalías para anticipar:
- Tiempo restante hasta fallo (TRTF)
- Probabilidad de fallo crítico en 30 días
- Recomendación de intervención
""")

# Simulación de salida del modelo
predict_result = {
    'Prob. fallo crítico en 30 días (%)': [18.4],
    'Tiempo estimado hasta fallo (días)': [41],
    'Recomendación': ['Inspección preventiva del compresor del motor']
}
st.table(pd.DataFrame(predict_result))

# Dashboard de KPIs de Salud
st.header("📊 Estado del Componente Crítico")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("🔥 Temp. motor", "635°C", "+5%")
kpi2.metric("🔧 Vibración eje", "42.1 Hz", "+12%")
kpi3.metric("🕒 Último mantenimiento", "89 días", "↑")

# Footer
st.markdown("""
---
Demo desarrollada con [Streamlit](https://streamlit.io/) | Repositorio: [GitHub - AeroPredict](https://github.com/tuusuario/aeropredict-demo)
""")
