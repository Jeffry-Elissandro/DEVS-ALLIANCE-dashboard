import pandas as pd
import plotly.express as px
import streamlit as st

# ============================
# CONFIGURACIÓN
# ============================
PESO_ACTIVIDAD = 0.30
PESO_DANO = 0.30
PESO_PUNTOS = 0.25
PESO_CONSISTENCIA = 0.15

# ============================
# DATOS DE LA ALIANZA
# (Edita aquí tus 30 jugadores)
# ============================
data = [
    {
        "Nombre": "CHESSDEV",
        "Rango": "Líder",
        "ID": "0gd5-r41k7",
        "Poder": 1002193,
        "Nivel": 78,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    },
    {
        "Nombre": "Chris",
        "Rango": "Especialista",
        "ID": "1l4y-eguc1",
        "Poder": 867520,
        "Nivel": 75,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    }
]

# ============================
# CÁLCULO DE RENDIMIENTO
# ============================
df = pd.DataFrame(data)

df["Score"] = (
    df["Actividad"] * PESO_ACTIVIDAD +
    df["Daño"] * PESO_DANO +
    df["Puntos"] * PESO_PUNTOS +
    df["Consistencia"] * PESO_CONSISTENCIA
) * 10  # Convertir a %

# Clasificación
def clasificar(score):
    if score >= 85:
        return "Elite"
    elif score >= 70:
        return "Sólido"
    elif score >= 50:
        return "Aceptable"
    else:
        return "Ineficiente"

df["Estado"] = df["Score"].apply(clasificar)

# ============================
# INTERFAZ
# ============================
st.set_page_config(page_title="DEV'S ALLIANCE", layout="wide")

st.title("🔥 DEV'S ALLIANCE – Sistema de Rendimiento")
st.write("Análisis de actividad, daño, puntos y consistencia")

# Filtro
estado_filtrado = st.multiselect(
    "Filtrar por estado:",
    ["Elite", "Sólido", "Aceptable", "Ineficiente"],
    default=["Elite", "Sólido", "Aceptable", "Ineficiente"]
)

df_filtrado = df[df["Estado"].isin(estado_filtrado)]

# ============================
# GRÁFICA INTERACTIVA
# ============================
fig = px.bar(
    df_filtrado,
    x="Nombre",
    y="Score",
    color="Estado",
    text="Score",
    hover_data=["Rango", "ID", "Poder", "Nivel", "Actividad", "Daño", "Puntos", "Consistencia"],
    title="Rendimiento de los miembros"
)

fig.update_layout(
    xaxis_tickangle=-45,
    yaxis_title="Rendimiento %",
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# ============================
# TABLA DE DATOS
# ============================
st.subheader("📊 Tabla completa de miembros")
st.dataframe(df_filtrado.sort_values("Score", ascending=False), use_container_width=True)

#python -m streamlit run dashboard.py
