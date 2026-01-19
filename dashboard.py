import pandas as pd
import plotly.express as px
import streamlit as st

if "mostrar_nota" not in st.session_state:
    st.session_state.mostrar_nota = True

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
        "Actividad": 8,
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
        "Actividad": 8,
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
        "Actividad": 6,
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
        "Actividad": 6,
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
        "Actividad": 7,
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
        "Actividad": 6,
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
        "Actividad": 9,
        "Daño": 9,
        "Puntos": 10,
        "Consistencia": 9
    },
    {
        "Nombre": "Experience^w^",
        "Rango": "Miembro",
        "ID": "12u8-9x3w1",
        "Poder": 2263655,
        "Nivel": 78,
        "Actividad": 9,
        "Daño": 10,
        "Puntos": 9,
        "Consistencia": 9
    },
    {
        "Nombre": "hellsing AG",
        "Rango": "Miembro",
        "ID": "0q9y-mxd7g",
        "Poder": 451700,
        "Nivel": 75,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 9,
        "Consistencia": 10
    },
    {
        "Nombre": "eusebio uwu",
        "Rango": "Miembro",
        "ID": "4ekl-amdrf",
        "Poder": 868769,
        "Nivel": 74,
        "Actividad": 6,
        "Daño": 4,
        "Puntos": 9,
        "Consistencia": 7
    },
    {
        "Nombre": "Bonilla Elias",
        "Rango": "Miembro",
        "ID": "3q6s-dssmd",
        "Poder": 3498663,
        "Nivel": 80,
        "Actividad": 9,
        "Daño": 10,
        "Puntos": 9,
        "Consistencia": 9
    },
    {
        "Nombre": "Ander_Wedd_45",
        "Rango": "Miembro",
        "ID": "0316-9bwz0",
        "Poder": 2769159,
        "Nivel": 73,
        "Actividad": 8,
        "Daño": 10,
        "Puntos": 8,
        "Consistencia": 9
    },
    {
        "Nombre": "sofiii12",
        "Rango": "Miembro",
        "ID": "4e75-mx46l",
        "Poder": 633945,
        "Nivel": 74,
        "Actividad": 6,
        "Daño": 3,
        "Puntos": 8,
        "Consistencia": 6
    },
    {
        "Nombre": "pijuynic3127",
        "Rango": "Miembro",
        "ID": "4ybn-mnv3x",
        "Poder": 703109,
        "Nivel": 69,
        "Actividad": 7,
        "Daño": 10,
        "Puntos": 7,
        "Consistencia": 8
    },
    {
        "Nombre": "exterminador de bts",
        "Rango": "Especialista",
        "ID": "46rw-ef8ec",
        "Poder": 910234,
        "Nivel": 73,
        "Actividad": 6,
        "Daño": 5,
        "Puntos": 6,
        "Consistencia": 7
    },
    {
        "Nombre": "AlexBBV",
        "Rango": "Miembro",
        "ID": "3j6t-ckkfp",
        "Poder": 916755,
        "Nivel": 75,
        "Actividad": 6,
        "Daño": 4,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "Benja",
        "Rango": "Miembro",
        "ID": "0qph-cbpiv",
        "Poder": 1810380,
        "Nivel": 80,
        "Actividad": 5,
        "Daño": 8,
        "Puntos": 6,
        "Consistencia": 8
    },
    {
        "Nombre": "unu880",
        "Rango": "Miembro",
        "ID": "0pf7-i1l5w",
        "Poder": 638219,
        "Nivel": 64,
        "Actividad": 5,
        "Daño": 2,
        "Puntos": 6,
        "Consistencia": 5
    },
    {
        "Nombre": "karma_ichikawa",
        "Rango": "Miembro",
        "ID": "4j53-gd6c5",
        "Poder": 753905,
        "Nivel": 74,
        "Actividad": 4,
        "Daño": 3,
        "Puntos": 5,
        "Consistencia": 5
    },
    {
        "Nombre": "Elizabeth c.v13",
        "Rango": "Especialista",
        "ID": "4d6g-cqz8y",
        "Poder": 641011,
        "Nivel": 72,
        "Actividad": 4,
        "Daño": 2,
        "Puntos": 4,
        "Consistencia": 4
    },
    {
        "Nombre": "Sapulinga01",
        "Rango": "Miembro",
        "ID": "33ou-fej3y",
        "Poder": 663553,
        "Nivel": 75,
        "Actividad": 4,
        "Daño": 6,
        "Puntos": 1,
        "Consistencia": 3
    },
    {
        "Nombre": "Aquio",
        "Rango": "Especialista",
        "ID": "0jj3-2yyeu",
        "Poder": 1186568,
        "Nivel": 73,
        "Actividad": 0,
        "Daño": 0,
        "Puntos": 0,
        "Consistencia": 1
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
    if score == 100:
        return "TOP"
    elif score >= 85:
        return "Elite"
    elif score >= 70:
        return "Sólido"
    elif score >= 50:
        return "Aceptable"
    else:
        return "Ineficiente"


df["Estado"] = df["Score"].apply(clasificar)

orden_estados = ["TOP", "Elite", "Sólido", "Aceptable", "Ineficiente"]

df["Estado"] = pd.Categorical(
    df["Estado"],
    categories=orden_estados,
    ordered=True
)

df = df.sort_values(by=["Estado", "Score"], ascending=[True, False])

color_map = {
    "TOP": "#ffff26",          # amarillo
    "Elite": "#1349dd",        # azul
    "Sólido": "#0ff10f",       # verde
    "Aceptable": "#e67e22",    # naranja
    "Ineficiente": "#e74c3c"   # rojo oscuro
}


# ============================
# INTERFAZ
# ============================
st.set_page_config(page_title="DEV'S ALLIANCE", layout="wide")

st.title("🔥 DEV'S ALLIANCE – Sistema de Rendimiento")
if st.session_state.mostrar_nota:
    st.warning(
        "📢 NOTA IMPORTANTE:\n\n"
    "Este sistema evalúa el rendimiento de cada integrante en base a actividad, "
    "daño, puntos y consistencia.\n"
    "Los rangos se actualizan periódicamente y sirven como referencia interna "
    "para la gestión de la alianza. \n"
    "Si estas en Mobile miralo horizontal. Además puedes resetear con el botón a la derecha "
    "o bien, descargar el PNG para más comodidad - CHESS"
    )
    if st.button("Entendido"):
        st.session_state.mostrar_nota = False

st.write("Análisis de actividad, daño, puntos y consistencia")


# Filtro
estado_filtrado = st.multiselect(
    "Filtrar por estado:",
    orden_estados,
    default=orden_estados
)

df_filtrado = df[df["Estado"].isin(estado_filtrado)]

# Ancho dinámico según cantidad de jugadores visibles
ancho_grafica = max(1200, len(df_filtrado) * 120)



# ============================
# GRÁFICA INTERACTIVA
# ============================
fig = px.bar(
    df_filtrado,
    x="Nombre",
    y="Score",
    color="Estado",
    color_discrete_map=color_map,
    text="Score",
    hover_data={
        "Estado": True,
        "Rango": True,
        "ID": True,
        "Nivel": True,
        "Poder": True,
        "Actividad": True,
        "Daño": True,
        "Puntos": True,
        "Consistencia": True,
        "Score": False
    },
    title="Rendimiento de los miembros - Semana de Gremios 12/18 Enero 2026",
    width=ancho_grafica
)

st.info("📱 En móviles, desliza horizontalmente la gráfica para ver todos los miembros")


fig.update_traces(texttemplate="%{text}%", textposition="outside")

fig.update_layout(
    xaxis_tickangle=-45,
    yaxis_title="Rendimiento %",
    height=600,
    margin=dict(l=40, r=40, t=80, b=150),
    xaxis=dict(
        tickfont=dict(size=12),
        automargin=True
    )
)

st.markdown(
    """
    <div style="overflow-x: auto; width: 100%;">
    """,
    unsafe_allow_html=True
)

st.plotly_chart(fig, use_container_width=False)

st.markdown(
    """
    </div>
    """,
    unsafe_allow_html=True
)


st.plotly_chart(fig, use_container_width=False)


# ============================
# TABLA DE DATOS
# ============================
st.subheader("📊 Tabla completa de miembros")
st.dataframe(df_filtrado.sort_values("Score", ascending=False), use_container_width=True)

#python -m streamlit run dashboard.py
