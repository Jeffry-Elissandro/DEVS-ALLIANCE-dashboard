import pandas as pd
import plotly.express as px
import streamlit as st

if "mostrar_nota" not in st.session_state:
    st.session_state.mostrar_nota = True

# ============================
# CONFIGURACIÓN
# ============================
PESO_ACTIVIDAD = 0.30
PESO_DANO = 0.25
PESO_PUNTOS = 0.30
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
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    },
    {
        "Nombre": "DLGPRO", 
        "Rango": "Miembro",
        "ID": "1ak1-fm1pl",
        "Poder": 923148,
        "Nivel": 71,
        "Actividad": 10,
        "Daño": 6,
        "Puntos": 10,
        "Consistencia": 8
    },
    {
        "Nombre": "Arcos 16", 
        "Rango": "Miembro",
        "ID": "3j75-94r2o",
        "Poder": 748226,
        "Nivel": 70,
        "Actividad": 10,
        "Daño": 7,
        "Puntos": 10,
        "Consistencia": 8
    },
    {
        "Nombre": "lucysaurio", 
        "Rango": "Miembro",
        "ID": "4rrf-tsbt4",
        "Poder": 250450,
        "Nivel": 65,
        "Actividad": 10,
        "Daño": 8,
        "Puntos": 10,
        "Consistencia": 8
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
        "Consistencia": 9
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
        "Daño": 7,
        "Puntos": 10,
        "Consistencia": 8
    },
    {
        "Nombre": "yo 456", 
        "Rango": "Colider",
        "ID": "4jos-r67gh",
        "Poder": 636274,
        "Nivel": 76,
        "Actividad": 8,
        "Daño": 2,
        "Puntos": 8,
        "Consistencia": 4
    },
    {
        "Nombre": "mya", 
        "Rango": "Miembro",
        "ID": "4yo3-cioo1",
        "Poder": 797375,
        "Nivel": 74,
        "Actividad": 10,
        "Daño": 9,
        "Puntos": 9,
        "Consistencia": 9
    },
    {
        "Nombre": "Arcabius", 
        "Rango": "Especialista",
        "ID": "3nzc-bbblj",
        "Poder": 1771581,
        "Nivel": 77,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 8,
        "Consistencia": 9
    },
    {
        "Nombre": "Lady.Moon", 
        "Rango": "Miembro",
        "ID": "01e6-cjcu2",
        "Poder": 409685,
        "Nivel": 67,
        "Actividad": 10,
        "Daño": 3,
        "Puntos": 7,
        "Consistencia": 6
    },
    {
        "Nombre": "ROON2526", 
        "Rango": "Miembro",
        "ID": "1d3k-mznw3",
        "Poder": 448386,
        "Nivel": 72,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    },
    {
        "Nombre": "Experience^w^", 
        "Rango": "Miembro",
        "ID": "12u8-9x3w1",
        "Poder": 2263655,
        "Nivel": 78,
        "Actividad": 10,
        "Daño": 5,
        "Puntos": 6,
        "Consistencia": 7
    },
    {
        "Nombre": "hellsing AG", 
        "Rango": "Miembro",
        "ID": "0q9y-mxd7g",
        "Poder": 451700,
        "Nivel": 75,
        "Actividad": 10,
        "Daño": 5,
        "Puntos": 6,
        "Consistencia": 6
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
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    },
    {
        "Nombre": "Ander_Wedd_45", 
        "Rango": "Miembro",
        "ID": "0316-9bwz0",
        "Poder": 2769159,
        "Nivel": 73,
        "Actividad": 10,
        "Daño": 9,
        "Puntos": 10,
        "Consistencia": 9
    },
    {
        "Nombre": "sofiii12", 
        "Rango": "Miembro",
        "ID": "4e75-mx46l",
        "Poder": 633945,
        "Nivel": 74,
        "Actividad": 10,
        "Daño": 4,
        "Puntos": 8,
        "Consistencia": 6
    },
    {
        "Nombre": "pijuynic3127", 
        "Rango": "Miembro",
        "ID": "4ybn-mnv3x",
        "Poder": 703109,
        "Nivel": 69,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 7,
        "Consistencia": 7
    },
    {
        "Nombre": "exterminador de bts", 
        "Rango": "Especialista",
        "ID": "46rw-ef8ec",
        "Poder": 910234,
        "Nivel": 73,
        "Actividad": 10,
        "Daño": 7,
        "Puntos": 5,
        "Consistencia": 7
    },
    {
        "Nombre": "Benja", 
        "Rango": "Miembro",
        "ID": "0qph-cbpiv",
        "Poder": 1810380,
        "Nivel": 80,
        "Actividad": 10,
        "Daño": 5,
        "Puntos": 7,
        "Consistencia": 7
    },
    {
        "Nombre": "Elizabeth c.v13", 
        "Rango": "Miembro",
        "ID": "4d6g-cqz8y",
        "Poder": 641011,
        "Nivel": 72,
        "Actividad": 4,
        "Daño": 0,
        "Puntos": 2,
        "Consistencia": 4
    },
    {
        "Nombre": "Pxneda", 
        "Rango": "Miembro",
        "ID": "3uxe-dhcdm",
        "Poder": 626123,
        "Nivel": 74,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    },
    {
        "Nombre": "black lagoon69", 
        "Rango": "Miembro",
        "ID": "4iu7-dxzm0",
        "Poder": 1745060,
        "Nivel": 75,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 9,
        "Consistencia": 10
    },
    {
        "Nombre": "Artuxx<D", 
        "Rango": "Miembro",
        "ID": "16ln-8xkeg",
        "Poder": 553274,
        "Nivel": 72,
        "Actividad": 10,
        "Daño": 3,
        "Puntos": 8,
        "Consistencia": 4
    },
    {
        "Nombre": "Yander758", 
        "Rango": "Miembro",
        "ID": "044e-oopz4",
        "Poder": 311505,
        "Nivel": 68,
        "Actividad": 5,
        "Daño": 2,
        "Puntos": 3,
        "Consistencia": 3
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

st.write("Análisis de actividad, daño, puntos y consistencia")










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














#Para el mensaje de agradecimiento rango oro

import base64

def img_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()
import streamlit.components.v1 as components



img_banner = img_to_base64("Gremios_Rango_14k.png")




components.html(
    f"""
    <div style="
        background: linear-gradient(145deg, rgba(255,215,0,0.12), rgba(255,75,75,0.10));
        border-radius: 22px;
        padding: 26px;
        box-shadow: 0 0 35px rgba(255, 200, 75, 0.55);
        margin: 30px auto 35px auto;
        max-width: 1100px;
        font-family: Arial, sans-serif;
    ">

        <div style="text-align:center;">
            <img src="data:image/png;base64,{img_banner}" style="
                max-width: 100%;
                border-radius: 18px;
                box-shadow: 0 0 25px rgba(255, 215, 0, 0.65);
                margin-bottom: 22px;
            ">
        </div>

        <h2 style="text-align:center; color:#ffd700;">
            💎 A un paso de Diamante
        </h2>

        <p style="
            text-align:center;
            color:#f0f0f0;
            font-size:17px;
            max-width:900px;
            margin:0 auto;
            line-height:1.7;
        ">
            Esta semana estuvimos <strong>muy cerca de alcanzar el rango Diamante (16,000 puntos)</strong>,
            quedándonos en <strong>Oro con 14,000</strong>.
            <br><br>
            El potencial está ahí. Con constancia y trabajo en equipo,
            <strong>Diamante es totalmente alcanzable</strong>.
        </p>

    </div>
    """,
    height=950
)






# ============================
# PROGRESO HACIA DIAMANTE
# ============================

puntaje_actual = 13940   # Oro actual
puntaje_meta = 16000     # Diamante

porcentaje = int((puntaje_actual / puntaje_meta) * 100)


import streamlit.components.v1 as components



import base64

def img_to_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


diamante_img = img_to_base64("Gremio_Diamante_Logotipo.png")






components.html(
    f"""
    <div style="
        max-width: 1000px;
        margin: 30px auto 40px auto;
        padding: 26px 22px 28px 22px;
        border-radius: 22px;
        background: rgba(255, 0, 156, 0.08);
        box-shadow: 0 0 40px rgba(255, 0, 156, 0.5);
        font-family: Arial, sans-serif;
        text-align: center;
    ">

        <!-- IMAGEN DIAMANTE -->
        <img src="data:image/png;base64,{diamante_img}"
     style="
        width: 120px;
        max-width: 40vw;
        margin-bottom: 14px;
        filter: drop-shadow(0 0 18px rgba(255, 0, 156, 0.95));
     " />


        <h1 style="
            color: rgba(255, 0, 156, 0.94);
            margin-bottom: 12px;
        ">
            Progreso hacia Diamante
        </h1>

        <p style="
            color: #dddddd;
            font-size: 15px;
            margin-bottom: 18px;
        ">
            {puntaje_actual:,} / {puntaje_meta:,} puntos alcanzados
        </p>

        <!-- BARRA -->
        <div style="
            width: 100%;
            height: 22px;
            background: rgba(255,255,255,0.08);
            border-radius: 14px;
            overflow: hidden;
            box-shadow: inset 0 0 6px rgba(0,0,0,0.6);
        ">
            <div style="
                width: {porcentaje}%;
                height: 100%;
                background: linear-gradient(
                    90deg,
                    rgba(255, 0, 156, 0.85),
                    rgba(255, 120, 220, 1)
                );
                box-shadow:
                    0 0 18px rgba(255, 0, 156, 0.95),
                    inset 0 0 6px rgba(255,255,255,0.35);
                transition: width 0.8s ease;
            ">
            </div>
        </div>

        <p style="
            color: #f0f0f0;
            margin-top: 12px;
            font-size: 14px;
        ">
            {porcentaje}% completado — cada aporte nos acerca más
        </p>

    </div>
    """,
    height=320
)










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






#Resumen ejeutivo


st.subheader("🛠️ Resumen Ejecutivo de la Alianza")

st.markdown("""
<style>
.kpi-card {
    background: linear-gradient(
        145deg,
        rgba(255, 75, 75, 0.12),
        rgba(120, 40, 40, 0.06)
    );
    border-radius: 16px;
    padding: 14px 12px;
    text-align: center;
    box-shadow: 0 8px 18px rgba(255, 75, 75, 0.4);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    min-height: 110px;
}

@media (hover: hover) {
    .kpi-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 35px rgba(255, 75, 75, 0.6);
    }
}

.kpi-title {
    font-size: 14px;
    color: #ffb3b3;
    margin-bottom: 8px;
}

.kpi-value {
    font-size: 30px;
    font-weight: 700;
    color: #ffffff;
}
            
/* Hover solo desktop */
@media (hover: hover) {
    .kpi-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 14px 28px rgba(255, 75, 75, 0.55);
    }
}

/* Mobile: separación vertical clara */
@media (max-width: 768px) {
    .kpi-card {
        margin-bottom: 16px;          /* 🧠 aire entre tarjetas */
    }
}
</style>
""", unsafe_allow_html=True)



c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">👥 Miembros evaluados</div>
        <div class="kpi-value">{total_miembros}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🔖 Promedio general</div>
        <div class="kpi-value">{promedio_general}%</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🏆 TOP actuales</div>
        <div class="kpi-value">{top_count}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">⚠️ En riesgo</div>
        <div class="kpi-value">{riesgo_count}</div>
    </div>
    """, unsafe_allow_html=True)



st.caption(
    "Este resumen refleja el estado actual del rendimiento de la alianza "
    "y se actualiza conforme cambian los datos."
)







# st.divider() Sirve para dejar espacios






#Para objetivo semanal


st.markdown("---")

st.subheader("🎯 Objetivo Semanal de la Alianza")

import streamlit.components.v1 as components

components.html(
    """
    <div style="
        background: linear-gradient(145deg, rgba(255,75,75,0.12), rgba(120,40,40,0.06));
        border-radius: 18px;
        padding: 22px 26px;
        box-shadow: 0 10px 30px rgba(255,75,75,0.35);
        max-width: 1000px;
        margin: 20px auto 30px auto;
        font-family: sans-serif;
    ">
        <h3 style="color:#ff4b4b; margin-bottom:10px;">
            📌 Meta clara
        </h3>
        <p style="color:#dddddd; font-size:16px;">
            Alcanzar los 16k de puntos para el <strong>rango diamante</strong> 
            de gremios esta semana.
        </p>

        <h3 style="color:#ff4b4b; margin-top:18px; margin-bottom:10px;">
            🔥 Enfoque principal
        </h3>
        <p style="color:#dddddd; font-size:16px;">
            Priorizar <strong>operaciones de gremio</strong> y mantener
            actividad en el evento.
        </p>

        <h3 style="color:#ff4b4b; margin-top:18px; margin-bottom:10px;">
            🏅 Recomendación
        </h3>
        <p style="color:#dddddd; font-size:16px;">
            Realiza las operaciones constantemente, aprocechando que se
            reinicia cada 24 horas.
        </p>
    </div>
    """,
    height=380
)




st.caption(
    "Este objetivo se actualiza semanalmente y sirve como referencia colectiva, "
    "no como sanción individual."
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
    title="Rendimiento de los miembros - Semana 2 de Gremios 19/25 Enero 2026",
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


st.info("➡️ En móvil, observa en horizontal la gráfica")


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







#Para el mensaje de invitación a solucionar errores

st.markdown(
    """
    <div style="
        background: rgba(255, 75, 75, 0.08);
        border-left: 5px solid #ff4b4b;
        border-radius: 14px;
        padding: 18px 22px;
        margin: 25px auto 10px auto;
        max-width: 900px;
    ">
        <p style="
            margin: 0;
            color: #f2f2f2;
            font-size: 16px;
            line-height: 1.6;
        ">
            💬 <strong>¿Notas algo extraño en tu puntuación?</strong><br>
            Si consideras que tu puntuación presenta algún error o no refleja correctamente tu actividad, 
            puedes dejar un comentario más abajo. Lo revisaré personalmente y, si corresponde, se corregirá. 
            Este sistema es una referencia interna y siempre está abierto a cambios justos.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


st.caption("El objetivo del ranking es mejorar como alianza, no señalar errores individuales.")






#Para justificar el rendimiento de cada miembro


st.markdown("---")

st.markdown("""
<h3 style="text-align:center; color:#ff4b4b; margin-bottom:10px;">
🔎 ¿Cómo se evalúa el rendimiento?
</h3>

<p style="
text-align:center;
color:#cccccc;
max-width:900px;
margin: 0 auto 30px auto;
font-size:15px;
line-height:1.6;
">
El sistema de rendimiento evalúa a cada integrante considerando múltiples factores.
El objetivo no es castigar, sino <b>identificar fortalezas, detectar áreas de mejora</b>
y mantener el crecimiento de la alianza.
</p>

<div style="
display: flex;
flex-wrap: wrap;
justify-content: center;
gap: 20px;
">

<!-- FACTORES -->
<div style="
flex: 1;
min-width: 260px;
max-width: 360px;
background: rgba(255,255,255,0.03);
border-radius: 16px;
padding: 20px;
box-shadow: 0 0 20px rgba(255,75,75,0.25);
">
<h4 style="color:#ff7b7b; margin-bottom:10px;">⚙️ Factores evaluados</h4>
<ul style="color:#dddddd; font-size:14px; line-height:1.6;">
<li><b>Actividad:</b> Participación constante.</li>
<li><b>Daño:</b> Aporte real en combates.</li>
<li><b>Puntos:</b> Resultado acumulado.</li>
<li><b>Consistencia:</b> Rendimiento estable semana a semana.</li>
</ul>
</div>

<!-- ESTADOS -->
<div style="
flex: 1;
min-width: 260px;
max-width: 360px;
background: rgba(255,255,255,0.03);
border-radius: 16px;
padding: 20px;
box-shadow: 0 0 20px rgba(255,75,75,0.25);
">
<h4 style="color:#ff7b7b; margin-bottom:10px;">🏷️ Estados de rendimiento</h4>
<ul style="color:#dddddd; font-size:14px; line-height:1.6;">
<li><b>TOP:</b> Rendimiento sobresaliente y constante.</li>
<li><b>Elite / Sólido:</b> Buen desempeño general.</li>
<li><b>Aceptable:</b> Cumple, pero puede mejorar.</li>
<li><b>Ineficiente:</b> Bajo impacto o poca actividad.</li>
</ul>
</div>

<!-- MENSAJE -->
<div style="
flex: 1;
min-width: 260px;
max-width: 360px;
background: rgba(255,255,255,0.03);
border-radius: 16px;
padding: 20px;
box-shadow: 0 0 20px rgba(255,75,75,0.25);
">
<h4 style="color:#ff7b7b; margin-bottom:10px;">🏆 Mensaje importante</h4>
<p style="color:#dddddd; font-size:14px; line-height:1.6;">
El estado asignado <b>no es permanente</b>.
Todos los miembros pueden mejorar su posición
aumentando su participación, daño y consistencia.
</p>
</div>

</div>
""", unsafe_allow_html=True)








st.divider()


# ============================
# TABLA DE DATOS
# ============================
st.subheader("📊 Tabla completa de miembros - ACTUALIZADA!🏆")
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
    st.image("carta_fukua.png", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card-container'>", unsafe_allow_html=True)
    st.image("carta_painwheel.png", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)










#Voz humana antes que numeros


st.divider()

st.markdown(
    """
<div style="
    margin: 40px auto 50px auto;
    max-width: 900px;
    padding: 30px 28px;
    border-radius: 20px;
    background: linear-gradient(
        145deg,
        rgba(127, 179, 200, 0.12),
        rgba(90, 130, 150, 0.06)
    );
    box-shadow:
        0 0 28px rgba(127, 179, 200, 0.35),
        inset 0 0 0 1px rgba(127, 179, 200, 0.25);
    text-align: center;
">

<h2 style="color:#9fd3e8; margin-bottom:16px;">
🤍 Un mensaje para quienes han sido parte
</h2>

<p style="color:#e0e0e0; font-size:17px; line-height:1.7; margin-bottom:14px;">
Cada persona que pasó por esta alianza dejó algo.
A veces fue apoyo, a veces constancia, a veces simplemente estar ahí.
Algunos siguen caminando con nosotros, otros tomaron su propio rumbo,
pero <strong>ningún paso fue en vano</strong>.
</p>

<p style="color:#d0d0d0; font-size:15px; line-height:1.6; margin-bottom:14px;">
Tomar decisiones no siempre es fácil.
Hay momentos en los que toca pensar en el grupo,
aunque eso duela más de lo que se nota desde fuera.
Eso no borra lo vivido, ni el esfuerzo, ni el tiempo compartido.
</p>

<p style="color:#b8b8b8; font-size:14px; line-height:1.6;">
Si hoy sigues aquí, gracias por quedarte.
Si ya no estás, gracias por haber estado.
Este espacio existe porque hubo personas que lo hicieron posible,
aunque hoy no todas sigan presentes.
</p>

</div>
""",
    unsafe_allow_html=True
)







#Para mostrar tabla de MIEMBROS!


st.markdown(f"""
<style>
.dev-card {{
  background:linear-gradient(
    180deg,
    rgba(15,23,42,0.9),
    rgba(2,6,23,0.9)
  );
  border-radius:14px;
  padding:8px;
  cursor:pointer;
  border:1px solid rgba(212,177,95,0.25);
  transition:0.3s ease;
}}

.dev-card img {{
  width:100%;
  border-radius:10px;
  display:block;
}}

.dev-card span {{
  display:block;
  margin-top:6px;
  font-size:12px;
  color:#e5f3ff;
  letter-spacing:0.5px;
}}

.dev-card:hover {{
  transform:translateY(-6px) scale(1.06);
  box-shadow:
    0 0 12px rgba(212,177,95,0.35),
    0 0 25px rgba(212,177,95,0.15);
  border-color:#d4b15f;
}}
</style>
""", unsafe_allow_html=True)










import streamlit as st
import base64

def img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img1 = img_base64("1.png")
img2 = img_base64("2.png")
img3 = img_base64("3.png")
img4 = img_base64("4.png")
img5 = img_base64("5.png")
img6 = img_base64("6.png")
img7 = img_base64("7.png")
img8 = img_base64("8.png")
img9 = img_base64("9.png")
img10 = img_base64("10.png")
img11 = img_base64("11.png")
img12 = img_base64("12.png")
img13 = img_base64("13.png")
img14 = img_base64("14.png")
img15 = img_base64("15.png")
img16 = img_base64("16.png")
img17 = img_base64("17.png")
img18 = img_base64("18.png")
img19 = img_base64("19.png")
img20 = img_base64("20.png")
img21 = img_base64("21.png")
img22 = img_base64("22.png")
img23 = img_base64("23.png")
img24 = img_base64("24.png")
img25 = img_base64("25.png")
img26 = img_base64("26.png")
img27 = img_base64("27.png")
img28 = img_base64("28.png")
img29 = img_base64("29.png")
img30 = img_base64("30.png")

st.markdown(f"""
<style>
.dev-card{{
  background:#292929e6; /* Fondo de las cartas */
  border-radius:12px;
  padding:8px;
  transition:0.25s;
  cursor:pointer;
}}
.dev-card img{{
  width:100%;
  border-radius:10px;
  display:block;
}}
.dev-card span{{
  display:block;
  margin-top:6px;
  font-size:12px;
  color:#e5f3ff;
}}
.dev-card:hover{{
  transform:translateY(-4px) scale(1.04);
  box-shadow:0 0 15px rgba(212,175,55,0.6);
  border-color:#D4AF37;
}}
</style>

<div style="
max-width:1100px;
margin:40px auto;
padding:28px;
background:linear-gradient(180deg,#0b0f1a,#020617);
border-radius:18px;
box-shadow:
  0 0 35px rgba(0,0,0,0.6),
  inset 0 0 40px rgba(212,177,95,0.05);
text-align:center;
">

<h2 style="
color:#f5e6b8;
margin-bottom:6px;
font-size:26px;
letter-spacing:1px;
">
💜 Miembros Actuales — Alianza DEVS
</h2>

<p style="
color:#9fb3c8;
font-size:14px;
margin-bottom:22px;
">
Cada rostro aquí representa compromiso, constancia y equipo.
</p>

<div style="
display:grid;
grid-template-columns:repeat(auto-fill,minmax(90px,1fr));
gap:14px;
">

<div class="dev-card">
  <img src="data:image/png;base64,{img26}">
  <span>CHESSDEV</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img25}">
  <span>»Chris«</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img27}">
  <span>Lady_Navier</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img30}">
  <span>brinda con queso</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img29}">
  <span>aru_25</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img28}">
  <span>DLGPRO</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img19}">
  <span>black lagoon69</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img23}">
  <span>SkibidiLopez</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img24}">
  <span>Artuxx<D</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img22}">
  <span>lucysaurio</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img21}">
  <span>William_Afton_1983</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img18}">
  <span>Pxneda</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img20}">
  <span>RIXTUN</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img16}">
  <span>"mya"</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img17}">
  <span>Arcos 16</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img14}">
  <span>Experience^w^</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img7}">
  <span>KSTKBMS23</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img15}">
  <span>Lady.Moon</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img12}">
  <span>sofiii12</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img13}">
  <span>ROON2526</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img11}">
  <span>Ander_Wedd_45</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img6}">
  <span>exterminador de bts</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img10}">
  <span>hellsing AG</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img9}">
  <span>Benja</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img8}">
  <span>Bonilla Elias</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img5}">
  <span>pijuynic3127</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img4}">
  <span>Athenacatevv</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img1}">
  <span>yo 456</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img2}">
  <span>FRANCIS798</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img3}">
  <span>Oliver's</span>
</div>




</div>
</div>
""", unsafe_allow_html=True)










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

st.markdown("### 🌟 Opiniones de los miembros")

try:
    with open("comentarios.txt", "r", encoding="utf-8") as f:
        st.text(f.read())
except FileNotFoundError:
    st.info("Aún no hay comentarios.")




st.divider() 



#Para EasterEgg

import base64

def load_gif(path):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/gif;base64,{data}"



gif_src = load_gif("secreto.gif")

st.markdown(f"""
<div style="text-align:center; margin-top:30px;">
    <img src="{gif_src}" width="180">
    <p style="color:#777; font-size:12px; margin-top:8px;">
        ¡Gracias por ver!
    </p>
</div>
""", unsafe_allow_html=True)








#python -m streamlit run dashboard.py
