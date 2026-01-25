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

st.title("💎 DEV'S ALLIANCE – Sistema de Rendimiento")
if st.session_state.mostrar_nota:
    st.warning(
        "📢 NOTA IMPORTANTE:\n\n"
    "Este sistema evalúa el rendimiento de cada integrante en base a actividad, "
    "daño, puntos y consistencia.\n"
    "Los rangos se actualizan periódicamente y sirven como referencia interna "
    "para la gestión de la alianza. \n"
    "También puedes interactuar con la gráfica con las herramientas disponibles a la  "
    "derecha, o bien, descargar el PNG de la gráfica para más comodidad - CHESS"
    )
    if st.button("Entendido"):
        st.session_state.mostrar_nota = False

st.write("Análisis de actividad, daño, puntos y consistencia")





#Sistema KPIs

total_miembros = len(df)

promedio_general = round(df["Score"].mean(), 1)

top_count = len(df[df["Estado"] == "TOP"])

riesgo_count = len(df[df["Estado"] == "Ineficiente"])

st.divider()




st.markdown("""
<style>
/* Estilo visual para KPIs */
div[data-testid="metric-container"] {
    background: linear-gradient(
        145deg,
        rgba(255, 75, 75, 0.08),
        rgba(120, 40, 40, 0.04)
    );
    border-radius: 16px;
    padding: 18px 14px;
    box-shadow:
        0 8px 20px rgba(255, 75, 75, 0.35),
        inset 0 0 0 1px rgba(255, 75, 75, 0.25);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

/* Micro realce solo en desktop */
@media (hover: hover) {
    div[data-testid="metric-container"]:hover {
        transform: translateY(-3px);
        box-shadow:
            0 14px 30px rgba(255, 75, 75, 0.55),
            inset 0 0 0 1px rgba(255, 75, 75, 0.35);
    }
}
</style>
""", unsafe_allow_html=True)





st.markdown("<div class='kpi-animate'>", unsafe_allow_html=True)




st.subheader("🛠️ Resumen Ejecutivo de la Alianza")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(
        label="👥 Miembros evaluados",
        value=total_miembros
    )

with kpi2:
    st.metric(
        label="🔖 Promedio general",
        value=f"{promedio_general} %"
    )

with kpi3:
    st.metric(
        label="🏆 TOP actuales",
        value=top_count
    )

with kpi4:
    st.metric(
        label="⚠️ En riesgo",
        value=riesgo_count
    )


st.markdown("<div class='kpi-animate'>", unsafe_allow_html=True)


st.caption(
    "Este resumen refleja el estado actual del rendimiento de la alianza "
    "y se actualiza conforme cambian los datos."
)




st.divider()




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

fig_mobile = px.bar(
    df_filtrado.sort_values("Score"),
    x="Score",
    y="Nombre",
    color="Estado",
    color_discrete_map=color_map,
    orientation="h",
    text="Score",
    hover_data=[
        "Estado", "Rango", "ID", "Nivel", "Poder",
        "Actividad", "Daño", "Puntos", "Consistencia"
    ],
    title="Rendimiento de los miembros (Vista Mobile)",
    height=max(600, len(df_filtrado) * 35)
)

fig_mobile.update_traces(texttemplate="%{text}%", textposition="outside")
fig_mobile.update_layout(
    xaxis_title="Rendimiento %",
    yaxis_title="",
    margin=dict(l=120, r=40, t=80, b=40)
)

# Selector de vista
modo_mobile = st.checkbox("📱 Modo Mobile - vista optimizada (En Desarrollo)", value=False)


st.info("📱 En móvil, observa en horizontal la gráfica")


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

# ============================
# CONFIGURACIÓN DE PLOTLY
# ============================
plotly_config = {
    "scrollZoom": False,        # ❌ desactiva zoom con scroll / touch
    "displayModeBar": True,
    "displaylogo": False,
    "modeBarButtonsToRemove": [
        "zoom2d",
        "select2d",
        "lasso2d",
        "zoomIn2d",
        "zoomOut2d",
        "autoScale2d",
        "resetScale2d"
    ]
}

fig.update_layout(dragmode="pan")

fig.update_traces(texttemplate="%{text}%", textposition="outside")

fig.update_layout(
    dragmode="pan",            # ✅ PAN por defecto
    xaxis_tickangle=-45,
    yaxis_title="Rendimiento %",
    height=600,
    margin=dict(l=40, r=40, t=80, b=150)
)


st.plotly_chart(
    fig,
    use_container_width=False,
    key="grafica_rendimiento",
    config=plotly_config
)



st.markdown(
    """
    </div>
    """,
    unsafe_allow_html=True
)



st.divider()


# ============================
# TABLA DE DATOS
# ============================
st.subheader("📊 Tabla completa de miembros")
st.dataframe(df_filtrado.sort_values("Score", ascending=False), use_container_width=True)


#Video Promocional DEVS
#<!-- URL embed solo funciona dentro de iframe -->


import streamlit as st
import streamlit.components.v1 as components

st.markdown("---")

components.html(
    """
    <div style="text-align:center;">

        <h1 style="color:#ff4b4b; margin-bottom:20px;">
            🎬 EQUIPO PARA JEFE DE INMORTALES
        </h1>

        <p style="
            color:#cccccc;
            max-width:800px;
            margin:0 auto 20px auto;
            font-size:28px;
            line-height:1.6;
        ">
            ¡Saludos Gente!
        </p>

        <p style="
            color:#cccccc;
            max-width:800px;
            margin:0 auto 30px auto;
            font-size:16px;
            line-height:1.6;
        ">
            ¿Tienes problemas para hacer más daño al Jefe de Inmortales?
            No te preocupes... te mostraré el equipo ideal para que logres
            hacer más daño y puedas superarte esta temporada de Gremios.
        </p>

        <div style="
            display:flex;
            justify-content:center;
            margin-bottom:40px;
        ">
            <div style="
                border:4px solid #ff4b4b;
                border-radius:16px;
                padding:10px;
                max-width:900px;
                width:100%;
                box-shadow:0 0 20px rgba(255,75,75,0.6);
            ">
                <iframe
                    width="100%"
                    height="500"
                    src="https://www.youtube.com/embed/XwXHEG6iJbE?rel=0&autoplay=0"
                    title="YouTube video player"
                    frameborder="0"
                    allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen
                    style="border-radius:12px;"
                ></iframe>
            </div>
        </div>

    </div>
    """,
    height=800
)



#Para mostrar las cartas

st.markdown("""
<style>
.card-container {
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 0 14px rgba(150, 80, 255, 0.6);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* IMPORTANTE */
.card-container img {
    display: block;
}

/* Hover SOLO desktop */
@media (hover: hover) {
    .card-container:hover {
        transform: translateY(-6px) scale(1.05);
        box-shadow: 0 0 35px rgba(255, 75, 75, 0.95);
    }
}

/* Carta central */
.card-main {
    box-shadow: 0 0 30px rgba(255, 75, 75, 0.9);
}
</style>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 1.2, 1])

with col1:
    st.markdown("<div class='card-container'>", unsafe_allow_html=True)
    st.image("carta_annie.png", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card-container card-main'>", unsafe_allow_html=True)
    st.image("carta_peacock.png", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card-container'>", unsafe_allow_html=True)
    st.image("carta_painwheel.png", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)









#Para Comentarios

st.markdown("---")
st.subheader("💬 Comentarios de la Alianza")

nombre = st.text_input("Tu nombre o Nick")
comentario = st.text_area("Escribe tu comentario")

if st.button("Enviar comentario"):
    if nombre and comentario:
        with open("comentarios.txt", "a", encoding="utf-8") as f:
            f.write(f"{nombre}: {comentario}\n---\n")
        st.success("¡Comentario enviado!")
    else:
        st.warning("Completa todos los campos")

st.divider()

#Para mostrar los comentarios

st.markdown("### 🗨️ Opiniones de los miembros")

try:
    with open("comentarios.txt", "r", encoding="utf-8") as f:
        st.text(f.read())
except FileNotFoundError:
    st.info("Aún no hay comentarios.")


#python -m streamlit run dashboard.py
