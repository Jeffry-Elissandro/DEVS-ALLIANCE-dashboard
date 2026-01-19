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
    },
    {
        "Nombre": "aru_25",
        "Rango": "Miembro",
        "ID": "38l9-o56hb",
        "Poder": 438611,
        "Nivel": 64,
        "Actividad": 10,
        "Daño": 5,
        "Puntos": 10,
        "Consistencia": 8
    },
    {
        "Nombre": "DLGPRO",
        "Rango": "Miembro",
        "ID": "1ak1-fm1pl",
        "Poder": 923148,
        "Nivel": 71,
        "Actividad": 10,
        "Daño": 4,
        "Puntos": 10,
        "Consistencia": 7
    },
    {
        "Nombre": "Arcos 16",
        "Rango": "Miembro",
        "ID": "3j75-94r2o",
        "Poder": 748226,
        "Nivel": 70,
        "Actividad": 10,
        "Daño": 4,
        "Puntos": 10,
        "Consistencia": 7
    },
    {
        "Nombre": "lucysaurio",
        "Rango": "Miembro",
        "ID": "4rrf-tsbt4",
        "Poder": 250450,
        "Nivel": 65,
        "Actividad": 10,
        "Daño": 5,
        "Puntos": 10,
        "Consistencia": 7
    },
    {
        "Nombre": "William_Afton_1983",
        "Rango": "Miembro",
        "ID": "3r1v-i03ks",
        "Poder": 946197,
        "Nivel": 70,
        "Actividad": 10,
        "Daño": 7,
        "Puntos": 10,
        "Consistencia": 8
    },
    {
        "Nombre": "SkibidiLopez",
        "Rango": "Miembro",
        "ID": "0ph6-5s5bh",
        "Poder": 1975525,
        "Nivel": 73,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    },
    {
        "Nombre": "Lady_Navier",
        "Rango": "Especialista",
        "ID": "50is-suxy9",
        "Poder": 575151,
        "Nivel": 64,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    },
    {
        "Nombre": "KSTKBMS23",
        "Rango": "Miembro",
        "ID": "3pni-nyf54",
        "Poder": 578309,
        "Nivel": 74,
        "Actividad": 10,
        "Daño": 4,
        "Puntos": 10,
        "Consistencia": 6
    },
    {
        "Nombre": "yo 456",
        "Rango": "Colider",
        "ID": "4jos-r67gh",
        "Poder": 636274,
        "Nivel": 76,
        "Actividad": 10,
        "Daño": 4,
        "Puntos": 10,
        "Consistencia": 7
    },
    {
        "Nombre": "mya",
        "Rango": "Miembro",
        "ID": "4yo3-cioo1",
        "Poder": 797375,
        "Nivel": 74,
        "Actividad": 10,
        "Daño": 5,
        "Puntos": 10,
        "Consistencia": 5
    },
    {
        "Nombre": "Arcabius",
        "Rango": "Especialista",
        "ID": "3nzc-bbblj",
        "Poder": 1771581,
        "Nivel": 77,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    },
    {
        "Nombre": "Lady.Moon",
        "Rango": "Miembro",
        "ID": "01e6-cjcu2",
        "Poder": 409685,
        "Nivel": 67,
        "Actividad": 10,
        "Daño": 3,
        "Puntos": 10,
        "Consistencia": 5
    },
    {
        "Nombre": "ROON2526",
        "Rango": "Miembro",
        "ID": "1d3k-mznw3",
        "Poder": 448386,
        "Nivel": 72,
        "Actividad": 10,
        "Daño": 9,
        "Puntos": 10,
        "Consistencia": 9
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
