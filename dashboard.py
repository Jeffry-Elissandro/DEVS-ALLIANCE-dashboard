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
        "Poder": 1266707,
        "Nivel": 79,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    },
    {
        "Nombre": "»alex«", 
        "Rango": "Colíder",
        "ID": "1l4y-eguc1",
        "Poder": 958033,
        "Nivel": 77,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    },
    {
        "Nombre": "Lady_Navier", 
        "Rango": "Especialista",
        "ID": "50is-suxy9",
        "Poder": 705004,
        "Nivel": 66,
        "Actividad": 10,
        "Daño": 10,
        "Puntos": 10,
        "Consistencia": 10
    },
    {
        "Nombre": "TwerlenK", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 77,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "MRchochox", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 52,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "EARTHLINGO", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 68,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "Adrexolm", 
        "Rango": "Especialista",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 79,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "DLGPRO", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 72,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "xXDrive_shXx", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 76,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "viejamiada", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 74,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "KSTKBMS23", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 77,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "jfglhg", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 79,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "William_Afton_1983", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 72,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "Blood Skull RD", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 77,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "KilLeo0217", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 78,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "Experience^w^", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 79,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "ArtuxxD", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 73,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "Skullgirls14203520", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 62,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "Oliver's", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 75,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "Ander_Weed_45", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 75,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "Arcos16", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 71,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "black lagoon69", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 76,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "STANLEY GOAT", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 69,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "NERE OTAKO", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 66,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "Bonilla Elias", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 80,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "defuncion", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 73,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "exterminador de bts", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 74,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "CoinXY", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 79,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },
    {
        "Nombre": "rottqned", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 74,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
    },{
        "Nombre": "Tik_lmao", 
        "Rango": "Miembro",
        "ID": "0000-00000",
        "Poder": 000,
        "Nivel": 67,
        "Actividad": 6,
        "Daño": 6,
        "Puntos": 6,
        "Consistencia": 6
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
    "para la gestión de la alianza. Todas las noticias o avisos serán "
     "informados por aquí. Ante dudas no temas en preguntar - CHESS \n" 
    )
    if st.button("Entendido"):
        st.session_state.mostrar_nota = False






#14 de Febrero




import streamlit as st

st.set_page_config(layout="wide")

css = """
<style>
#embedim--heart{
  position:fixed;
  left:0;top:0;bottom:0;
  width:100vw;height:100vh;
  overflow:hidden;
  z-index:9999999;
  pointer-events:none
}
.heart { position: relative; }
.heart:before, .heart:after {
  position: absolute; content: "";
  left: 18px; top: 0; width: 18px; height: 30px;
  background: #CC2022;
  border-radius: 30px 30px 0 0;
  transform: rotate(-45deg);
  transform-origin: 0 100%;
}
.heart:after {
  left: 0;
  transform: rotate(45deg);
  transform-origin: 100% 100%;
}
@keyframes moveclouds {0% { top: 702px; } 100% { top: -702px; } }
@keyframes sideWays {0% { margin-left:0px; } 100% { margin-left:50px; } }
.x { position: absolute; top: 0; }
.x:nth-child(2){ left: 5%; transform: scale(0.6); opacity: 0.6; animation: moveclouds 15s linear infinite, sideWays 5s ease-in-out infinite alternate; }
.x:nth-child(3){ left: 25%; transform: scale(0.5); opacity: 0.5; animation: moveclouds 25s linear infinite, sideWays 5s ease-in-out infinite alternate; }
.x:nth-child(4){ left: 40%; transform: scale(0.8); opacity: 0.8; animation: moveclouds 20s linear infinite, sideWays 5s ease-in-out infinite alternate; }
.x:nth-child(5){ left: 55%; transform: scale(0.9); opacity: 0.9; animation: moveclouds 18s linear infinite, sideWays 5s ease-in-out infinite alternate; }
.x:nth-child(6){ left: 60%; transform: scale(0.3); opacity: 0.3; animation: moveclouds 12s linear infinite, sideWays 5s ease-in-out infinite alternate; }
.x:nth-child(7){ left: 72%; transform: scale(0.5); opacity: 0.6; animation: moveclouds 15s linear infinite, sideWays 5s ease-in-out infinite alternate; }
.x:nth-child(8){ left: 88%; transform: scale(0.4); opacity: 0.2; animation: moveclouds 10s linear infinite, sideWays 5s ease-in-out infinite alternate; }
.x:nth-child(9){ left: 90%; transform: scale(0.2); opacity: 0.4; animation: moveclouds 12s linear infinite, sideWays 5s ease-in-out infinite alternate; }
</style>
"""

html = """
<div id="embedim--heart">
  <div class="x"><div class="heart"></div></div>
  <div class="x"><div class="heart"></div></div>
  <div class="x"><div class="heart"></div></div>
  <div class="x"><div class="heart"></div></div>
  <div class="x"><div class="heart"></div></div>
  <div class="x"><div class="heart"></div></div>
  <div class="x"><div class="heart"></div></div>
  <div class="x"><div class="heart"></div></div>
  <div class="x"><div class="heart"></div></div>
</div>
"""

st.markdown(css + html, unsafe_allow_html=True)


























#Para ambientar la web (bloque opcional)

st.markdown("## 🌿 Ambiente")

with st.expander("🎧 Música ambiental (opcional)", expanded=False):
    st.caption(
        "Activa el sonido si deseas una experiencia más inmersiva. "
    )

    st.audio(
        "tipe_beat_web.mp3",
        format="audio/mp3",
        loop=True
    )










# CARAJO DENUEVO ENFERMO >:O


import streamlit as st
import base64

def img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

sick_img = img_base64("sick_admin.png")

# Inyectar CSS
st.markdown("""
<style>
.sick-note {
    max-width: 1000px;
    margin: 50px auto;
    padding: 28px;
    background: linear-gradient(
        180deg,
        rgba(99, 102, 241, 0.08),
        rgba(168, 85, 247, 0.06)
    );
    border-radius: 18px;
    box-shadow: 0 0 30px rgba(99, 102, 241, 0.25);
    display: grid;
    grid-template-columns: 1fr 260px;
    gap: 26px;
    align-items: center;
}
.sick-note img {
    width: 100%;
    border-radius: 14px;
    filter: drop-shadow(0 0 12px rgba(99, 102, 241, 0.35));
}
.sick-title {
    color: #e5e7eb;
    font-size: 26px;
    margin-bottom: 12px;
}
.sick-text {
    color: #cbd5f7;
    font-size: 16px;
    line-height: 1.7;
    margin-bottom: 14px;
}
.sick-footer {
    color: #a5b4fc;
    font-size: 14px;
}
@media (max-width: 768px) {
    .sick-note {
        grid-template-columns: 1fr;
        text-align: center;
    }
}
</style>
""", unsafe_allow_html=True)

# Renderizar HTML
st.markdown(f"""
<div class="sick-note">
  <div>
    <div class="sick-title">¡Saludos gente! 😅</div>
    <div class="sick-text">
      En estos días no me encuentro al 100% de salud, por lo que estaré
      tomándome un pequeño tiempo para recuperarme con calma.
      <br><br>
      Mientras tanto, <strong>nuestro Colíder queda a cargo</strong> para
      asegurar que todo siga funcionando como debe.
    </div>
    <div class="sick-text">
      Seguiré presente en la medida de lo posible, aportando y tratando de
      mantener la web actualizada.  
      Esto es solo una pausa, no una ausencia.
    </div>
    <div class="sick-footer">
      Gracias por la comprensión, el apoyo y la buena vibra 💜  
      Nos seguimos cuidando como equipo.
    </div>
  </div>
  <div>
    <img src="data:image/png;base64,{sick_img}">
  </div>
</div>
""", unsafe_allow_html=True)














# AGRADECIMIENTO A NAVIER


import streamlit as st
import base64

# Función para convertir imagen a base64
def img_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")

# Imagen del nuevo Colíder
img_colider = img_base64("3.png")

# Tarjeta de felicitación estilo rango superior
st.markdown(
    f"""
    <style>
    .colider-card {{
      max-width:700px;
      margin:60px auto;
      padding:40px 30px;
      background:linear-gradient(180deg,#0f0f0f,#1a1a1a 70%,#0f0f0f);
      border-radius:18px;
      border:2px solid rgba(180,180,180,0.35);
      box-shadow:
        0 0 40px rgba(120,120,120,0.45),
        inset 0 0 25px rgba(180,180,180,0.15);
      text-align:center;
      transition:0.4s ease;
    }}

    @media (hover:hover) {{
      .colider-card:hover {{
        transform:scale(1.02);
        box-shadow:
          0 0 65px rgba(200,200,200,0.65),
          inset 0 0 35px rgba(180,180,180,0.25);
      }}
    }}

    .colider-avatar {{
      width:140px;
      height:140px;
      border-radius:50%;
      object-fit:cover;
      border:4px solid #9ca3af;
      box-shadow:0 0 30px rgba(200,200,200,0.8);
      margin-bottom:20px;
    }}

    .colider-title {{
      font-size:28px;
      color:#f3f4f6;
      margin:0;
      letter-spacing:2px;
      font-weight:bold;
      text-shadow:0 0 15px rgba(180,180,180,0.9);
    }}

    .colider-text {{
      margin-top:18px;
      font-size:16px;
      color:#d1d5db;
      line-height:1.8;
    }}

    .colider-rank {{
      margin-top:22px;
      font-size:14px;
      color:#9ca3af;
      letter-spacing:1.5px;
      font-weight:bold;
      text-transform:uppercase;
    }}
    </style>

    <div class="colider-card">
      <img src="data:image/png;base64,{img_colider}" class="colider-avatar">
      <h3 class="colider-title">Destacado de la semana</h3>
      <p class="colider-text">
        Este puesto es realmente exclusivo.
        Fuiste el único miembro capaz de conseguir <strong>Todos los Puntos </strong>
        de gremio. ¡Tu ayuda nos llevo a completar el Diamante!
        <br><br>
        Un sincero agradecimiento por siempre seguir superándote, 
        incluso hasta superar límites.
      </p>
      <div class="colider-rank">
        Felicitaciones — Eres el miembro más comprometido
      </div>
    </div>
    """,
    unsafe_allow_html=True
)
















#Para Promocionar el nuevo JEFE MS.FORTUNE


import streamlit.components.v1 as components
import base64

def img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

misterio_img = img_base64("Critty_Kitty.png")

components.html(
    f"""
    <style>
      .contenedor {{
        max-width: 1000px;
        margin: 40px auto;
        padding: 18px;
        background: linear-gradient(180deg, #0f0f0f, #1c1c1c);
        border-radius: 22px;
        border: 2px solid rgba(180,180,180,0.55);
        box-shadow: 0 0 25px rgba(120,120,120,0.45),
                    inset 0 0 18px rgba(80,80,80,0.35);
        text-align: center;
      }}

      .contenedor h2 {{
        font-size: 32px;
        color: #ffffff;
        text-shadow: 0 0 12px rgba(255,255,255,0.9),
                     0 0 24px rgba(200,200,200,0.7);
        margin-bottom: 20px;
      }}

      .contenedor img {{
        width: 50%;   /* por defecto en PC */
        height: auto;
        border-radius: 12px;
        box-shadow: 0 0 25px rgba(255,255,255,0.15);
      }}

      /* En pantallas pequeñas (mobile) */
      @media (max-width: 768px) {{
        .contenedor img {{
          width: 100%;  /* ocupa todo el ancho en mobile */
        }}
        .contenedor h2 {{
          font-size: 24px;
        }}
      }}
    </style>

    <div class="contenedor">
      <h2>16 DE FEBRERO</h2>
      <img src="data:image/png;base64,{misterio_img}" />
    </div>
    """,
    height=900
)














#Para el mensaje de agradecimiento rango oro









# ============================
# PROGRESO HACIA DIAMANTE
# ============================

puntaje_actual = 12820   # Oro actual
puntaje_meta = 16000     # Diamante

porcentaje = int((puntaje_actual / puntaje_meta) * 100)


import streamlit.components.v1 as components









import base64

def img_to_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


diamante_img = img_to_base64("Gremio_Diamante_Logotipo.png")




file_path = "Skull_characteres.gif" #Para el gif
with open(file_path, "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data).decode("utf-8")




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
            {porcentaje}% completado — cada aporte será de gran ayuda
        </p>

                <!-- GIF -->
        <img src="data:image/gif;base64,{encoded}" alt="gif animado"
             width="250" height="250" />

    </div>
    """,
    height=735
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
            Seguir mejorando los puntos de gremio para suber, actualmente nuestro <strong>TOP 280</strong> 
            .
        </p>

        <h3 style="color:#ff4b4b; margin-top:18px; margin-bottom:10px;">
            🔥 Enfoque principal
        </h3>
        <p style="color:#dddddd; font-size:16px;">
            Mantenernos estables con las <strong>operaciones de gremio</strong> y llegar a 
            diamante u oro.
        </p>

        <h3 style="color:#ff4b4b; margin-top:18px; margin-bottom:10px;">
            🏅 Recomendación
        </h3>
        <p style="color:#dddddd; font-size:16px;">
            Realizar las operaciones constantemente, aprocechando que se
            reinician cada 24 horas.
        </p>
    </div>
    """,
    height=400
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
    title="Rendimiento de los miembros - ⚠️SE ACTUALIZARÁ AL FINALIZAR LA SEMANA",
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








#Para explicar el Promedio A Superar para mantenerse a flote en la alianza



import streamlit as st




st.set_page_config(page_title="Score Recomendado Alianza", layout="wide")

import base64
with open("Recomendado_Imagen.gif", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")
Recomendado_Imagen = f"data:image/gif;base64,{data}"



# Configuración global de la página
st.set_page_config(
    page_title="Score Recomendado Alianza",
    layout="wide"   # 👈 Esto activa Wide mode por defecto
)

st.markdown(f"""
<div style="
  max-width:900px;
  margin:35px auto;
  padding:22px 26px;
  background:linear-gradient(180deg,#0f172a,#020617);
  border-radius:16px;
  box-shadow:0 0 25px rgba(99,102,241,0.25);
  border:1px solid rgba(99,102,241,0.35);
">

  <h2 style="
    text-align:center;
    color:#ffffff;
    font-size:26px;
    letter-spacing:1.5px;
    margin-bottom:10px;
    text-shadow:0 0 12px rgba(99,102,241,0.6);
  ">
    🏆 Score Recomendado de la Alianza
  </h2>

  <p style="
    text-align:center;
    color:#9fb3c8;
    font-size:15px;
    margin-bottom:18px;
  ">
    Este es el <strong style="color:#e5f3ff;">promedio sugerido</strong> que todo miembro debería alcanzar semanalmente para mantener a la Alianza en lo más alto.
    No es una exigencia, sino una meta motivadora que refleja el compromiso colectivo.
  </p>

  <!-- Imagen/GIF en Base64 -->
  <div style="text-align:center; margin:20px 0;">
    <img src="{Recomendado_Imagen}" alt="Imagen" style="max-width:100%; border-radius:12px; box-shadow:0 0 15px rgba(99,102,241,0.5);" />
  </div>
            
  <div style="
    display:flex;
    justify-content:space-around;
    margin-top:20px;
    font-size:16px;
    color:#cbd5f1;
  ">
    <div style="text-align:center;">
      <strong style="color:#ffffff;">500</strong><br>Medallas / semana
    </div>
    <div style="text-align:center;">
      <strong style="color:#ffffff;">200,000,000</strong><br>Daño total
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

















st.divider()


# ============================
# TABLA DE DATOS
# ============================
st.subheader("📊 Tabla completa de miembros - ACTUALIZACIÓN PRONTO ⚙️")
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
            No llegó el nuevo jefe de inmortales <strong>Critty Kitty</strong> esta semana.
            Sin embargo, pueden seguir con el equipo contra Marie que, igualmente, tiene muchas ventajas.
            Además, ahora que ya no tiene el modificador, es recomendado llevarla con Fukua y Annie.
            Una alternativa muy conocida es <strong>Robo Fortune - Terrrminator</strong>.
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
                    src="https://www.youtube.com/embed/XwXHEG6iJbE"
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
    height=1020
)









#Para el Título Equipo de la Semana

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">

<style>
@keyframes glow {
  0% {
    text-shadow: 
      0 0 6px rgba(255,255,255,0.7),
      0 0 14px rgba(192,192,192,0.6),
      0 0 28px rgba(255,255,255,0.5);
  }
  100% {
    text-shadow: 
      0 0 10px rgba(255,255,255,0.9),
      0 0 20px rgba(192,192,192,0.8),
      0 0 40px rgba(255,255,255,0.7);
  }
}

/* SOLO afecta al título con clase .special-title */
.special-title {
  font-family: 'Orbitron', sans-serif;
  font-size:42px;
  font-weight:800;
  letter-spacing:2px;
  color:#f0f0f0;
  text-transform:uppercase;
  animation: glow 1.5s ease-in-out infinite alternate;
}

.special-title:hover {
  color:#ffffff;
  text-shadow:
    0 0 12px rgba(255,255,255,1),
    0 0 24px rgba(192,192,192,0.9),
    0 0 48px rgba(255,255,255,0.8);
  transform: scale(1.05);
  transition: all 0.3s ease;
}
</style>

<div style="margin:35px auto 20px; text-align:center;">
  <h1 class="special-title">Equipo de la Semana</h1>
</div>
""", unsafe_allow_html=True)














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
  <img src="data:image/png;base64,{img1}">
  <span>CHESSDEV</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img2}">
  <span>»alex«</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img3}">
  <span>Lady_Navier</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img4}">
  <span>TwerlenK</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img5}">
  <span>rottqned</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img6}">
  <span>CoinXY</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img7}">
  <span>exterminador de bts</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img8}">
  <span>defuncion</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img9}">
  <span>Bonilla Elias</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img10}">
  <span>NERE OTAKO</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img11}">
  <span>STANLEY GOAT</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img12}">
  <span>black lagoon69</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img13}">
  <span>Arcos 16</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img14}">
  <span>Ander_Weed_45</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img15}">
  <span>Oliver's</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img16}">
  <span>Skullgirls14203520</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img17}">
  <span>ArtuxxD</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img18}">
  <span>Experience^w^</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img19}">
  <span>KilLeo0217</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img20}">
  <span>Blood Skull RD</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img21}">
  <span>William_Afton_1983</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img22}">
  <span>jfglhg</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img23}">
  <span>KSTKBMS23</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img24}">
  <span>viejamiada</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img25}">
  <span>xXDrive_shXx</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img26}">
  <span>DLGPRO</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img27}">
  <span>Adrexolm</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img28}">
  <span>E A R T H L I N G O</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img29}">
  <span>MRchochox</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img30}">
  <span>Tik_lmao</span>
</div>




</div>
</div>
""", unsafe_allow_html=True)





# C H A N G E S ! ! !


# Eliminated FRANCIS CHANGE TO tomohu
# Eliminated "mya" CHANGE TO SAUL GOODMAN
# Eliminated GOODMAN CHANGE TO SAUL E A R T H L I N G O

#Change yo 456 Colider to Especialist
#Change »chris« Especialist to Colider
#07/02/2026 18:45

















import streamlit.components.v1 as components



def img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- Imagen del nuevo miembro ---


# Lista de nuevos miembros (nombre + imagen)
nuevos_miembros = [
    {"nombre": "Adrexolm", "imagen": "27.png"},
    {"nombre": "Blood Skull RD", "imagen": "20.png"},
    {"nombre": "KilLeo0217", "imagen": "19.png"},
    {"nombre": "Skullgirls1420352", "imagen": "16.png"},
    {"nombre": "STANLEY GOAT", "imagen": "11.png"},
    {"nombre": "NERE OTAKO", "imagen": "10.png"},
    {"nombre": "defuncion", "imagen": "8.png"},
    {"nombre": "jfglhg", "imagen": "22.png"},
    {"nombre": "MRchochox", "imagen": "29.png"},
    {"nombre": "Tik_lmao", "imagen": "30.png"},
    {"nombre": "CoinXY", "imagen": "6.png"},
]



components.html(
    """
    <h2 style="
      text-align:center;
      font-size:28px;
      color:#ffffff;
      text-shadow:0 0 12px rgba(255,255,255,0.9),
                   0 0 24px rgba(255,255,255,0.7);
      margin-bottom:24px;
    ">
      Incorporaciones
    </h2>
    """,
    height=80
)



for miembro in nuevos_miembros:
    img_new = img_base64(miembro["imagen"])
    components.html(
        f"""
        <div style="
          max-width:800px;
          margin:20px auto;
          padding:22px;
          background:linear-gradient(180deg,#020617,#0f172a);
          border-radius:18px;
          border:2px solid rgba(168,85,247,0.55);
          box-shadow:
            0 0 25px rgba(168,85,247,0.45),
            inset 0 0 18px rgba(99,102,241,0.25);
          display:flex;
          align-items:center;
          gap:22px;
        ">

          <!-- Avatar -->
          <img src="data:image/png;base64,{img_new}" style="
            width:96px;
            height:96px;
            border-radius:50%;
            object-fit:cover;
            border:3px solid #a855f7;
            box-shadow:0 0 18px rgba(168,85,247,0.9);
          ">

          <!-- Texto -->
          <div>
            <h3 style="
              margin:0;
              font-size:22px;
              color:#ffffff;
              letter-spacing:1px;
              text-shadow:0 0 10px rgba(168,85,247,0.8);
            ">
              ✨ Bienvenido, <span style="color:#d8b4fe;">{miembro["nombre"]}</span>
            </h3>

            <p style="
              margin-top:6px;
              font-size:14px;
              color:#c7d2fe;
              line-height:1.6;
            ">Nos alegra tenerte en la alianza.</p>
          </div>

        </div>
        """,
        height=250
    )










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
