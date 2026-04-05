import pandas as pd
import plotly.express as px
import streamlit as st

if "mostrar_nota" not in st.session_state: #DOKI THEME PATH: C:\Users\CompuFire\Desktop\Equipo de imágenes\Black Dahlia para VSCode.png
    st.session_state.mostrar_nota = True


import streamlit as st

WEB_TESTING = False

def show_testing_badge():
    st.markdown("""
    <style>
    .web-testing-badge{
        position:fixed;
        top:12px;
        left:18px;
        background:linear-gradient(135deg,#3a3a3a,#1f1f1f);
        color:#eaeaea;
        font-size:12px;
        font-weight:700;
        padding:6px 12px;
        border-radius:6px;
        z-index:999999;
        letter-spacing:1px;
        font-family:monospace;
        border:1px solid rgba(255,255,255,0.15);
        box-shadow:0 2px 8px rgba(0,0,0,0.35);
    }
    </style>

    <div class="web-testing-badge">
        WEB TESTING
    </div>
    """, unsafe_allow_html=True)

if WEB_TESTING:
    show_testing_badge()





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
    {"Nombre":"CHESSDEV","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Líder", "ID": "0gd5-r41k7", "Nivel": 80, "Poder": 1336707},
    {"Nombre":"Lady_Navier","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Especialista", "ID": "50is-suxy9", "Nivel": 68, "Poder": 000},
    {"Nombre":"MRchochox","Actividad":10,"Daño":3,"Puntos":10,"Consistencia":7, "Rango": "Colíder", "ID": "0000-00000", "Nivel": 61, "Poder": 000},
    {"Nombre":"Kileo0217","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 79, "Poder": 000},
    {"Nombre":"Rukawa_Noceda","Actividad":10,"Daño":1,"Puntos":10,"Consistencia":6, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 65, "Poder": 000},
    {"Nombre":"CoinXY","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 80, "Poder": 000},
    {"Nombre":"BAKI","Actividad":10,"Daño":4,"Puntos":10,"Consistencia":7, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 75, "Poder": 000},
    {"Nombre":"Aesick4u","Actividad":10,"Daño":1,"Puntos":10,"Consistencia":6, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 78, "Poder": 000},
    {"Nombre":"jfglhg","Actividad":10,"Daño":3,"Puntos":10,"Consistencia":7, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 80, "Poder": 000},
    {"Nombre":"xXDrive_shXx","Actividad":10,"Daño":2,"Puntos":10,"Consistencia":7, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 78, "Poder": 000},
    {"Nombre":"eduguti","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 80, "Poder": 000},
    {"Nombre":"œ oooooo","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 74, "Poder": 000},
    {"Nombre":"black lagoon69","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 77, "Poder": 000},
    {"Nombre":"onediax","Actividad":10,"Daño":3,"Puntos":10,"Consistencia":7, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 79, "Poder": 000},
    {"Nombre":"batgirl","Actividad":10,"Daño":1,"Puntos":10,"Consistencia":6, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 77, "Poder": 000},
    {"Nombre":"shrek embaraz@d0","Actividad":10,"Daño":8,"Puntos":10,"Consistencia":9, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 71, "Poder": 000},
    {"Nombre":"PABLOX3","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 80, "Poder": 000},
    {"Nombre":"ArtuxxD","Actividad":10,"Daño":3,"Puntos":10,"Consistencia":7, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 74, "Poder": 000},
    {"Nombre":"oscuro","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 73, "Poder": 000},
    {"Nombre":"LESLIE'M","Actividad":10,"Daño":3,"Puntos":10,"Consistencia":7, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 65, "Poder": 000},
    {"Nombre":"void_13","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 80, "Poder": 000},
    {"Nombre":"aru_25","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 73, "Poder": 000},
    {"Nombre":"GxJxGxSx","Actividad":10,"Daño":3,"Puntos":10,"Consistencia":7, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 73, "Poder": 000},
    {"Nombre":"exe2029l","Actividad":10,"Daño":10,"Puntos":10,"Consistencia":10, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 76, "Poder": 000},
    {"Nombre":"UnrealNat","Actividad":10,"Daño":6,"Puntos":10,"Consistencia":9, "Rango": "Miembro", "ID": "0000-00000", "Nivel": 75, "Poder": 000}
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

st.title("💎 DEV'S ALLIANCE – WEB OFICIAL")

st.write("Análisis de actividad, daño, puntos y consistencia")










if st.session_state.mostrar_nota:
    st.warning(
        "📢 NOTA IMPORTANTE:\n\n"
    "Este sistema evalúa el rendimiento de cada integrante en base a actividad, "
    "daño, puntos y consistencia.\n"
    "Los rangos se actualizan periódicamente y sirven como referencia interna "
    "para la gestión de la alianza. Todas las noticias o avisos serán "
     "informados por aquí. Ante dudas no temas en preguntar - CHESSDEV \n" 
    )
    if st.button("Entendido"):
        st.session_state.mostrar_nota = False








st.divider()






# ==============================
# 24 MESSAGES!!
# ==============================


import streamlit.components.v1 as components
import base64

def load_gif(path):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/gif;base64,{data}"



gif_update = load_gif("no_update.gif")

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

      .contenedor h4 {{
        font-size: 24px;
        color: #ffffff;
        text-shadow: 0 0 1px rgba(255,255,255,0.9),
                     0 0 1px rgba(200,200,200,0.7);
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
        .contenedor h4 {{
          font-size: 24px;
        }}
      }}
    </style>

    <div class="contenedor">
      <img src="data:image/gif;base64,{gif_update}" alt="gif update"
             width="250" height="250" />
    </div>
    """,
    height=700
)



















st.divider()



# =========================
# FUKUA'S BIRTHDAY !!!
# =========================


import streamlit as st
import base64
import streamlit.components.v1 as components

# =========================
# CONFIGURACIÓN BASE
# =========================
st.set_page_config(page_title="Fukua Birthday", layout="wide")

# =========================
# CARGAR IMAGEN LOCAL
# =========================
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_fukua = get_base64("Maries_birthday.png")

# =========================
# HTML COMPLETO (TODO JUNTO)
# =========================
html_code = f"""
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">

<style>
@keyframes fukua-glow {{
  0% {{
    text-shadow: 
      0 0 6px rgba(255,255,255,0.7),
      0 0 14px rgba(192,192,192,0.6),
      0 0 28px rgba(255,255,255,0.5);
  }}
  100% {{
    text-shadow: 
      0 0 10px rgba(255,255,255,0.9),
      0 0 20px rgba(192,192,192,0.8),
      0 0 40px rgba(255,255,255,0.7);
  }}
}}

/* CONTENEDOR */
.fukua-container {{
    background: linear-gradient(135deg, #0f122f, #2a317d);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    max-width: 900px;
    margin: auto;
}}

/* TÍTULO */
.fukua-title {{
  font-family: 'Dancing Script', cursive;
  font-size: 58px;
  font-weight: 800;
  letter-spacing: 2px;
  color: #f0f0f0;
  text-transform: uppercase;
  animation: fukua-glow 1.5s ease-in-out infinite alternate;
}}

.fukua-title:hover {{
  color:#ffffff;
  text-shadow:
    0 0 12px rgba(255,255,255,1),
    0 0 24px rgba(192,192,192,0.9),
    0 0 48px rgba(255,255,255,0.8);
  transform: scale(1.05);
  transition: all 0.3s ease;
}}

/* SUBTÍTULO */
.fukua-subtitle {{
    font-size: 22px;
    color: #caffca;
    margin-bottom: 30px;
}}

/* IMAGEN */
.fukua-img {{
    width: 350px;
    max-width: 90%;
    height: auto;
    border-radius: 15px;
}}

/* DESCRIPCIÓN */
.fukua-desc {{
    margin-top: 25px;
    font-size: 18px;
    color: #eaffea;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}}

/* =========================
   📱 RESPONSIVE (MOBILE)
   ========================= */
@media (max-width: 788px) {{

  .fukua-container {{
      padding: 25px;
      border-radius: 15px;
  }}

  .fukua-title {{
      font-size: 50px;
      font-weight: 800;
      letter-spacing: 2px;
      color: #f0f0f0;
      text-transform: uppercase;
      animation: fukua-glow 1.5s ease-in-out infinite alternate;
  }}

  .fukua-subtitle {{
      font-size: 18px;
  }}

  .fukua-desc {{
      font-size: 15px;
      padding: 0 10px;
  }}

  .fukua-img {{
      width: 280px;
  }}
}}

</style>

<div class="fukua-container">

    <div style="margin:35px auto 20px; text-align:center;">
        <h1 class="fukua-title">Marie's Birthday</h1>
    </div>
    
    <div class="fukua-subtitle">Celebrando a la Skullgirl de Nuevo Meridiano 💙</div>

    <img class="fukua-img" src="data:image/png;base64,{img_fukua}">

    <div class="fukua-desc">
        <strong>¡Hoy es el cumpleaños de Marie!</strong>
        <br><br>
        En honor al alma torturada favorita de todos, la administración otorga este espacio para rendir 
        homenaje a uno de nuestros personajes más queridos en la comunidad.
        <br><br>
        Además, recuerda ir a la sección OFERTAS DIARIAS de la TIENDA para reclamar tu regalo <strong>GRATIS</strong>, 
        que incluye movimientos de Marie, puntos de habilidad, repescas y una reliquia!! Hora de ordenar...
    </div>

</div>
"""

# =========================
# RENDER HTML CORRECTAMENTE
# =========================
components.html(html_code, height=830, scrolling=False)










st.divider()


# ==============================
# DESTACADOS DE TEMPORADA
# ==============================


# VERSIÓN COLECTIVA 5 MIEMBROS (SIN JERARQUÍA)

import streamlit as st
import base64

def img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

miembros_destacados = [
    {"img": "8.png", "score": "5.147B - 740 points", "name": "œ oooooo"},
    {"img": "7.png", "score": "4.366B - 760 points", "name": "void_13"},
    {"img": "1.png", "score": "1.348B - 830 points", "name": "CHESSDEV"},
    {"img": "2.png", "score": "1.241B - 810 points", "name": "Lady_Navier"},
    {"img": "3.png", "score": "720M - 810 points", "name": "CoinXY"},
]

for miembro in miembros_destacados:
    miembro["img_b64"] = img_base64(miembro["img"])

members_html = "".join(
    f"""
    <div class="member">
      <img src="data:image/png;base64,{m['img_b64']}">
      <div class="score">{m['score']}</div>
      <div class="name">{m['name']}</div>
    </div>
    """ for m in miembros_destacados
)

gif_chibi = img_base64("Filia_mini_celebrate.gif")

html_code = f"""
<style>

.destacados-card {{
  max-width:900px;
  margin:60px auto;
  padding:40px 20px;
  background: radial-gradient(circle at top, #1a102d, #050505 80%);
  border-radius:20px;
  border:2px solid rgba(124,58,237,0.3);
  box-shadow:0 0 40px rgba(124,58,237,0.3);
  text-align:center;
}}

.destacados-title {{
  font-size:34px;
  font-weight:bold;
  margin-bottom:10px;
  color:#c084fc;
  letter-spacing:2px;
}}

.destacados-sub {{
  font-size:14px;
  color:#a78bfa;
  margin-bottom:30px;
  opacity:0.8;
}}

.grid {{
  display:flex;
  justify-content:center;
  flex-wrap:wrap;
  gap:30px;
}}

.member {{
  text-align:center;
  transition:0.3s ease;
}}

.member img {{
  width:110px;
  height:110px;
  border-radius:50%;
  object-fit:cover;
  border:3px solid #a78bfa;
  box-shadow:0 0 20px rgba(167,139,250,0.5);
  margin-bottom:10px;
  transition:0.3s ease;
}}

.member:hover img {{
  transform:scale(1.08);
  box-shadow:0 0 30px rgba(167,139,250,0.8);
}}

.score {{
  font-size:14px;
  font-weight:bold;
  color:#e9d5ff;
}}

.name {{
  font-size:13px;
  color:#d8b4fe;
}}

</style>

<div class="destacados-card">
  <h3 class="destacados-title">💜 Miembros Destacados</h3>
  <div class="destacados-sub">Reconocimiento colectivo al rendimiento de la temporada</div>
  <div class="grid">
    {members_html}
  </div>
  <div style="margin-top:30px; text-align:center;">
    <img src="data:image/gif;base64,{gif_chibi}" 
         style="width:85%; max-width:300px; height:auto; border-radius:12px; opacity:0.95;">
  </div>
</div>
"""

st.components.v1.html(html_code, height=1080, scrolling=False)
















st.divider()


# ==============================
# REGLAS DE RENDIMIENTO Y LIMPIEZA
# ==============================

import streamlit as st
import base64

# ==============================
# FUNCIÓN BASE64
# ==============================
def img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_regla = img_base64("guild_rules.png")  # Cambia el nombre si deseas

# ==============================
# BLOQUE CSS
# ==============================
st.markdown("""
<style>
.regla-box {
    max-width:1100px;
    margin:40px auto;
    padding:30px;
    border-radius:18px;
    background: linear-gradient(180deg, #0f172a, #020617);
    box-shadow: 0 0 35px rgba(34,197,94,0.25);
    display:flex;
    align-items:center;
    gap:30px;
}
.regla-box:hover {
    transform: scale(1.01);
    transition: 0.3s;
    box-shadow: 0 0 45px rgba(34,197,94,0.35);
}
.regla-img img {
    max-width:100%;
    border-radius:16px;
    box-shadow: 0 0 25px rgba(255,255,255,0.15);
}
.regla-text h2 {
    color:#86efac;
    font-size:26px;
    margin-bottom:12px;
}
.regla-text p {
    color:#e5e7eb;
    font-size:15px;
    line-height:1.6;
}
.regla-highlight {
    color:#4ade80;
    font-weight:bold;
}
.regla-warning {
    color:#facc15;
    font-weight:bold;
}
@media (max-width: 768px) {
    .regla-box {
        flex-direction:column;
        text-align:center;
    }
}
</style>
""", unsafe_allow_html=True)

# ==============================
# BLOQUE HTML
# ==============================
st.markdown(f"""
<div class="regla-box">
    <div class="regla-img" style="flex:1;">
        <img src="data:image/png;base64,{img_regla}">
    </div>
    <div class="regla-text" style="flex:2;">
        <h2>DEVS - REGLA</h2>
        <p>Para mantener el equilibrio y asegurar el crecimiento de la alianza, se realiza una 
        <span class="regla-warning">LIMPIEZA semanal cada sábado por la noche</span>.</p>
        <p>El objetivo es claro y accesible: cada miembro debe alcanzar al menos 
        <span class="regla-highlight">500 puntos semanales</span>.</p>
        <p>Esta meta puede lograrse fácilmente completando actividades diarias, sin necesidad de exigencias extremas.</p>
        <p>Quienes cumplan o superen este valor continúan formando parte del equipo. En caso contrario, se dará oportunidad a nuevos miembros que puedan aportar al progreso del gremio.</p>
        <p>Esta medida no busca excluir, sino 
        <span class="regla-highlight">mantener un entorno activo, justo y comprometido para todos</span>, ya que la recompensa es para el que verdaderamente se esfuerza y aporta.</p>
    </div>
</div>
""", unsafe_allow_html=True)


st.divider()










import streamlit as st
import base64

# Convertir imagen a base64
with open("TOP_97.png", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")
top_img = f"data:image/png;base64,{data}"

# ==============================
# RÉCORD HISTÓRICO - TOP 97
# ==============================

st.markdown(f"""
<style>
  .responsive-img {{
    width: 100%;
    max-width: 500px;
    border-radius: 16px;
    box-shadow: 0 0 25px rgba(250,204,21,0.6);
  }}

  @media (max-width: 768px) {{
    .responsive-img {{
      max-width: 300px; /* tamaño más pequeño en móviles */
    }}
  }}
</style>

<div style="
  max-width:950px;
  margin:40px auto;
  padding:20px;
  background:transparent;
  border-radius:20px;
  font-family:'Segoe UI',sans-serif;
  text-align:center;
">

  <h2 class="record-title">¡RÉCORD HISTÓRICO ALCANZADO!</h2>

  <p style="
    color:#e5e7eb;
    font-size:18px;
    line-height:1.7;
    margin-bottom:22px;
  ">
    Oficialmente ahora somos parte de los <strong style="color:#fde68a;">TOP 100 gremios a nivel global</strong>,
    alcanzando el puesto <strong style="color:#fde68a;">97</strong>.
  </p>

  <!-- Imagen responsiva -->
  <div style="text-align:center; margin:30px 0;">
    <img src="{top_img}" alt="TOP 97" class="responsive-img" />
  </div>

  <p style="
    color:#cbd5e1;
    font-size:16px;
    line-height:1.6;
    margin-bottom:16px;
  ">
    Para algunos puede parecer muy alejado, pero quienes llevamos tiempo en esta alianza
    sabemos lo que realmente significa. En nuestros inicios, el objetivo parecía lejano;
    nuestro mejor puesto en ese entonces fue alrededor del <strong>TOP 5800</strong>.
  </p>

  <p style="
    color:#cbd5e1;
    font-size:16px;
    line-height:1.6;
    margin-bottom:16px;
  ">
    Hoy demostramos que el crecimiento constante, la constancia y el trabajo en equipo
    pueden llevarnos mucho más lejos de lo que imaginábamos.
    Este logro no pertenece a una sola persona, pertenece a toda la alianza.
  </p>

  <p style="
    color:#fde68a;
    font-weight:600;
    font-size:18px;
    margin-top:22px;
    text-shadow:0 0 12px rgba(250,204,21,0.6);
  ">
    Este no es el final — Gracias
  </p>

</div>
""", unsafe_allow_html=True)











st.divider()













#Para el mensaje de agradecimiento rango oro









# ============================
# PROGRESO HACIA DIAMANTE
# ============================

puntaje_actual = 16420   # Oro actual
puntaje_meta = 16000     # Diamante

porcentaje = int((puntaje_actual / puntaje_meta) * 100)


import streamlit.components.v1 as components




import base64

def img_to_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


diamante_img = img_to_base64("Gremio_Diamante_Logotipo.png")




file_path = "test_gif.gif" #Para el gif
with open(file_path, "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data).decode("utf-8")




components.html(
    f"""
       <style>
    @keyframes pulseGlow {{
      0% {{
        transform: scale(1);
        filter: drop-shadow(0 0 10px rgba(255, 0, 156, 0.6));
      }}
      50% {{
        transform: scale(1.06);
        filter: drop-shadow(0 0 35px rgba(255, 0, 156, 1));
      }}
      100% {{
        transform: scale(1);
        filter: drop-shadow(0 0 10px rgba(255, 0, 156, 0.6));
      }}
    }}
    </style>
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
        border-radius: 50%;
        animation: pulseGlow 2.5s ease-in-out infinite;
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
            {porcentaje}% completado — cada aporte fue de gran ayuda
        </p>

                <!-- GIF -->
        <img src="data:image/gif;base64,{encoded}" alt="gif animado"
             width="250" height="250" />

        <div style="text-align:center;">
      <strong style="color:#ffffff;">¡Gracias!</strong><br><strong style="color:#fff;">Logramos Llegar a Rango Diamante esta Temporada</strong>
    </div>


    </div>
    """,
    height=735
)




#-159, 44, -13
#cristian_673_yt
#licuadodechocolate
#yoremoik
#Wsixww

#nini_Taekjoo
#marylalaloca2.0



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
    <style>
        .panel {
            max-width: 1000px;
            margin: 30px auto;
            padding: 30px;
            border-radius: 14px;
            background: linear-gradient(160deg, #0f0f0f, #1a1a1a);
            border: 1px solid rgba(255, 75, 75, 0.4);
            box-shadow: 0 0 40px rgba(255, 75, 75, 0.25);
            font-family: 'Segoe UI', sans-serif;
            color: #e6e6e6;
        }

        .header {
            font-size: 22px;
            font-weight: bold;
            color: #ff4b4b;
            margin-bottom: 5px;
            letter-spacing: 1px;
        }

        .divider {
            height: 2px;
            background: linear-gradient(to right, transparent, #ff4b4b, transparent);
            margin: 15px 0 25px 0;
        }

        .section {
            margin-bottom: 25px;
        }

        .title {
            font-size: 16px;
            font-weight: bold;
            color: #ff4b4b;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .text {
            font-size: 15px;
            line-height: 1.6;
            color: #cccccc;
        }

        .highlight {
            color: #ffffff;
            font-weight: bold;
        }

        .warning {
            margin-top: 20px;
            padding: 12px;
            border-left: 4px solid #ff4b4b;
            background: rgba(255, 75, 75, 0.08);
            font-size: 14px;
        }

        .footer {
            margin-top: 25px;
            text-align: right;
            font-size: 13px;
            color: #888;
            letter-spacing: 1px;
        }
    </style>

    <div class="panel">

        <div class="header">COMUNICADO OFICIAL</div>
        <div class="divider"></div>

        <div class="section">
            <div class="title">META ACTUAL</div>
            <div class="text">
                Recuperar el rendimiento del gremio y consolidarnos nuevamente entre los mejores.
                El objetivo inmediato es superar nuestra posición actual en el 
                <span class="highlight">TOP 150</span>. 
                Este resultado depende directamente del cumplimiento de las normas establecidas.
            </div>
        </div>

        <div class="section">
            <div class="title">ENFOQUE</div>
            <div class="text">
                Las reglas <span class="highlight">NO son opcionales</span>. Son la base del orden interno. 
                Cualquier desacuerdo puede expresarse con respeto, pero el incumplimiento constante
                llevará a medidas más estrictas. 
                La permanencia en el gremio está sujeta al respeto de estas normas.
            </div>
        </div>

        <div class="section">
            <div class="title">DIRECTIVA</div>
            <div class="text">
                Cumplir las reglas no es complicado. Lo que se espera es compromiso y responsabilidad. 
                La administración no puede atender conflictos individuales constantes. 
                Se requiere paciencia, disciplina y cooperación colectiva.
            </div>
        </div>

        <div class="warning">
            El incumplimiento reiterado resultará en la expulsión del gremio como última medida.
        </div>

        <div class="footer">
            FIN DEL COMUNICADO
        </div>

    </div>
    """,
    height=855
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
    title="RENDIMIENTOS 📌 | Semana NO.12 | 23/29 Marzo ",
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







#========================================================================
#SCORE Y DAÑO DE ALIANZA
#========================================================================


st.set_page_config(page_title="DEV'S ALLIANCE", layout="wide")

import base64
import streamlit as st
import streamlit.components.v1 as components

with open("Recomendado_Imagen.gif", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")

imagen = f"data:image/gif;base64,{data}"


components.html(f"""
<div style="
    max-width: 900px;
    margin: 35px auto;
    padding: 28px;
    border-radius: 14px;
    background: linear-gradient(160deg, #050505, #111111);
    border: 1px solid rgba(255,75,75,0.4);
    box-shadow: 0 0 35px rgba(255,75,75,0.25);
    font-family: 'Segoe UI', sans-serif;
">

    <div style="
        text-align:center;
        color:#ff4b4b;
        font-size:24px;
        font-weight:bold;
        letter-spacing:2px;
    ">
        CONDICIÓN DE PARTICIPACIÓN
    </div>

    <div style="
        text-align:center;
        color:#aaaaaa;
        font-size:14px;
        margin-bottom:20px;
    ">
        Parámetros activos para mantenerse dentro del gremio
    </div>

    <div style="
        height:2px;
        background: linear-gradient(to right, transparent, #ff4b4b, transparent);
        margin: 15px 0 25px 0;
    "></div>

    <div style="text-align:center; margin:20px 0;">
        <img src="{imagen}" style="
            max-width:100%;
            border-radius:10px;
            box-shadow:0 0 20px rgba(255,75,75,0.4);
        ">
    </div>

    <div style="
        display:flex;
        justify-content:space-around;
        margin-top:25px;
        text-align:center;
    ">

        <div style="
            padding:15px;
            border-radius:10px;
            background: rgba(255,75,75,0.08);
            border: 1px solid rgba(255,75,75,0.3);
            width:40%;
        ">
            <div style="font-size:22px; font-weight:bold; color:#ffffff;">
                500
            </div>
            <div style="font-size:13px; color:#bbbbbb;">
                PUNTOS SEMANALES (BASE REQUERIDA)
            </div>
        </div>

        <div style="
            padding:15px;
            border-radius:10px;
            background: rgba(255,75,75,0.05);
            border: 1px solid rgba(255,75,75,0.2);
            width:40%;
        ">
            <div style="font-size:22px; font-weight:bold; color:#ffffff;">
                200M
            </div>
            <div style="font-size:13px; color:#999999;">
                DAÑO (OPCIONAL, NO CAUSA EXPULSIÓN)
            </div>
        </div>

    </div>

    <div style="
        margin-top:25px;
        padding:14px;
        border-left:4px solid #ff4b4b;
        background: rgba(255,75,75,0.1);
        color:#dddddd;
        font-size:14px;
        line-height:1.5;
    ">
        Mantener un mínimo de <strong>500 puntos semanales</strong> forma parte de los parámetros activos del gremio.
        <br><br>
        La falta de cumplimiento de forma continua podrá derivar en la rotación del miembro.
        <br><br>
        El daño total es únicamente una métrica de rendimiento y no condiciona la permanencia (osea opcional pe).
    </div>

    <div style="
        margin-top:20px;
        text-align:right;
        font-size:12px;
        color:#777;
        letter-spacing:1px;
    ">
        ESTADO: ACTIVO
    </div>

</div>
""", height=950)

















st.divider()


# ============================
# TABLA DE DATOS
# ============================
st.subheader("Tabla completa de miembros 🎯")
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
            Tenemos de vuelta al jefe más molesto y desafiante de todos, 
            debido a sus modificadores. Estos son complejos y requieren 
            técnicas específicas para destacar en daño. ¿Te interesa saber más? 
            Si no conoces estas técnicas puedes ver los siguientes videos 
            por distintos creadores (con respectivos créditos) para practicar, buena suerte!!!
            Video creado por: <strong>AlannAx</strong> 💚
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
                    src="https://www.youtube.com/embed/EsdLZ80r1cE"
                    title="YouTube video player"
                    frameborder="0"
                    allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen
                    style="border-radius:12px;"
                ></iframe>
            </div>
        </div>

        <p style="
            color:#cccccc;
            max-width:800px;
            margin:0 auto 30px auto;
            font-size:16px;
            line-height:1.6;
        ">
            ¿Quieres más Variedad de equipos? 
            Video creado por: <strong>Deny17S</strong> 🖤
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
                    src="https://www.youtube.com/embed/VGm-StKu0Kk"
                    title="YouTube video player"
                    frameborder="0"
                    allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen
                    style="border-radius:12px;"
                ></iframe>
            </div>
        </div>

        <p style="
            color:#cccccc;
            max-width:800px;
            margin:0 auto 30px auto;
            font-size:16px;
            line-height:1.6;
        ">
            ¿Recuerdas esta loca jugada? Te recuerdo que ya ha sido parcheado, pero 
            fue divertido mientras duró.
            Video creado por: <strong>RodirKW</strong> 🤍
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
                    src="https://www.youtube.com/embed/tVqGYTvZyn8"
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
    height=2330
)





st.divider()



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














# ==============================
# CARTAS CON SUBTÍTULOS ARRIBA
# ==============================

import streamlit as st

st.markdown("""
<style>
.card-container {
    border: 2px solid rgba(150, 80, 255, 0.9); /* borde morado */
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 0 14px rgba(150, 80, 255, 0.6);
    transition: transform 0.3s ease, box-shadow 0.3s ease, color 0.3s ease, background 0.3s ease;
    background: rgba(17, 24, 39, 0.85); /* fondo oscuro */
    padding: 0;
    text-align: center;
}

/* Hover SOLO desktop */
@media (hover: hover) {
    .card-container:hover {
        transform: translateY(-6px) scale(1.05);
        border: 2px solid #fff; /* borde blanco */
        box-shadow: 0 0 35px rgba(255, 255, 255, 0.95);
    }
}

/* Hover y active (para mobile) */
.card-container:hover,
.card-container:active {
    transform: scale(1.02);
    border: 2px solid #fff; /* borde blanco */
    box-shadow: 0 0 35px rgba(255, 255, 255, 0.95);
}

/* Carta central */
.card-main {
    box-shadow: 0 0 35px rgba(255, 77, 240, 0.5);
}

/* Título arriba */
.card-caption {
    font-size: 17px;
    font-weight: 700;
    color: #fa15c8; /* amarillo dorado */
    background: rgba(0,0,0,0.7); /* franja oscura semitransparente */
    padding: 10px;
    text-align: center;
    text-shadow: 0 2px 6px rgba(0,0,0,0.9);
    letter-spacing: 0.5px;
    transition: all 0.3s ease;
    margin: 0;
}

.card-container:hover .card-caption,
.card-container:active .card-caption {
    background: rgba(0, 0, 0, 1); /* fondo negro */
    color: #fff; /* texto blanco */
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.2, 1])

with col1:
    st.markdown("<div class='card-container'><div class='card-caption'>ATACANTE</div>", unsafe_allow_html=True)
    st.image("carta_fukua.png", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card-container card-main'><div class='card-caption'>ATACANTE</div>", unsafe_allow_html=True)
    st.image("carta_annie_marcada.png", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card-container'><div class='card-caption'>ATACANTE</div>", unsafe_allow_html=True)
    st.image("carta_beowulf.png", use_container_width=True)
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
img25 = img_base64("Imagen_para_testeos.png")
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
  <span>Lady_Navier</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img3}">
  <span>CoinXY</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img4}">
  <span>MRchochox</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img5}">
  <span>aru_25</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img6}">
  <span>angel vados</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img7}">
  <span>void_13</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img8}">
  <span>œ oooooo</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img9}">
  <span>BAKI</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img10}">
  <span>UnrealNat</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img11}">
  <span>oscuro</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img12}">
  <span>m4tth3w_kn</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img13}">
  <span>Emmy</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img14}">
  <span>black lagoon69</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img15}">
  <span>SansanoPerfecto</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img16}">
  <span>shrek embaraz@d0</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img17}">
  <span>ArtuxxD</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img18}">
  <span>Aesick4u</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img19}">
  <span>KilLeo0217</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img20}">
  <span>eduguti</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img21}">
  <span>PABLOX3</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img22}">
  <span>lanera_8043</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img23}">
  <span>GxJxGxSx</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img24}"> 
  <span>Coldsoul9223</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img25}">
  <span>DISPONIBLE</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img26}">
  <span>Sir Lag</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img27}"> 
  <span>batgirl</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img28}"> 
  <span>DeMauku</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img29}">
  <span>nini_Taekjoo</span>
</div>

<div class="dev-card">
  <img src="data:image/png;base64,{img30}">
  <span>Rukawa_Noceda</span>
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



#xd













import streamlit.components.v1 as components



def img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- Imagen del nuevo miembro ---


# Lista de nuevos miembros (nombre + imagen)
nuevos_miembros = [

    {"nombre": "DeMauku", "imagen": "28.png"},
    {"nombre": "nini_Taekjoo", "imagen": "29.png"},
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








st.divider()











# ==============================
# Título de Carrusel
# ==============================

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

/* SOLO afecta al título con clase .my-title */
.my-title {
  font-family: 'Orbitron', sans-serif;
  font-size:42px;
  font-weight:800;
  letter-spacing:2px;
  color:#f0f0f0;
  text-transform:uppercase;
  animation: glow 1.5s ease-in-out infinite alternate;
}

.my-title:hover {
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
  <h1 class="my-title">FAN-ARTS SEMANALES</h1>
</div>
""", unsafe_allow_html=True)







# ==============================
# CARRUSEL / EXPERIMENTAL / TEST
# ==============================

import streamlit as st
import base64

st.set_page_config(layout="wide")

# ==============================
# FUNCION BASE64
# ==============================
def img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ==============================
# IMAGENES
# ==============================
img1 = img_base64("fn_cerebella.png")
img2 = img_base64("fn_peacock.png")
img3 = img_base64("fn_fortune.png")
img4 = img_base64("fn_double.png")
img5 = img_base64("fn_filia.png")
img6 = img_base64("fn_parasoul.png")
img7 = img_base64("fn_valentine.png")
img8 = img_base64("fn_squigly.png")
img9 = img_base64("fn_bigband.png")
img10 = img_base64("fn_painwheel.png")
img11 = img_base64("fn_beowulf.png")
img12 = img_base64("fn_eliza.png")
img13 = img_base64("fn_robo_fortune.png")
img14 = img_base64("fn_dahlia.png")
img15 = img_base64("fn_umbrella.png")
img16 = img_base64("fn_fukua.png")
img17 = img_base64("fn_annie.png")
img18 = img_base64("fn_marie.png")

# ==============================
# CSS (CORREGIDO)
# ==============================
css = """
<style>
.slider {
    width: 100%;
    overflow: hidden;
    position: relative;
    padding: 30px 0;
}

.slide-track {
    display: flex;
    width: max-content;
    animation: scroll 80s linear infinite;
}

.slide {
    flex: 0 0 320px;
    margin: 0 15px;
    background: #1e1e1e;
    border-radius: 15px;
    padding: 15px;
    text-align: center;
    color: white;
    transition: transform 0.3s ease;
}

.slide:hover {
    transform: scale(1.05);
}

/* 🔥 IMAGEN CUADRADA SIN RECORTE */
.slide img {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: contain;
    background: #111;
    border-radius: 10px;
    cursor: pointer;
}

.title {
    font-weight: bold;
    margin-top: 10px;
    font-size: 16px;
}

.desc {
    font-size: 14px;
    opacity: 0.8;
}

/* ANIMACIÓN */
@keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}

/* ================= MODAL ================= */

.modal {
    display: none;
    position: fixed;
    z-index: 9999;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.85);
    backdrop-filter: blur(6px);
}

.modal-content {
    background: #1e1e1e;
    margin: 5% auto;
    padding: 20px;
    width: 60%;
    max-width: 800px;
    border-radius: 15px;
    color: white;
    text-align: center;
    position: relative;
}

.modal-content img {
    width: 100%;
    max-height: 500px;
    object-fit: contain;
    background: #111;
    border-radius: 10px;
}

.modal-title {
    font-size: 22px;
    font-weight: bold;
    margin-top: 15px;
}

.modal-desc {
    margin-top: 10px;
    font-size: 15px;
    opacity: 0.9;
}

.close {
    position: absolute;
    top: 10px;
    right: 15px;
    font-size: 28px;
    cursor: pointer;
}
</style>
"""

# ==============================
# HTML (MISMA ESTRUCTURA + onclick)
# ==============================
html = (
'<div class="slider">'
'  <div class="slide-track">'

f'    <div class="slide"><img src="data:image/png;base64,{img1}" onclick="openModal(data:image/png;base64,{img1}, CEREBELLA")><div class="title">CEREBELLA</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img2}" onclick="openModal(data:image/png;base64,{img2}, PEACOCK"><div class="title">PEACOCK</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img3}" onclick="openModal(data:image/png;base64,{img3}, NADIA (MS.) FORTUNE"><div class="title">NADIA "MS." FORTUNE</div><div class="desc">クミ 𓂃 ✒️ ωω𝗑𝗌𝗄𝗂 、zZz (wwxski)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img4}" onclick="openModal(data:image/png;base64,{img4}, DOUBLE"><div class="title">DOUBLE</div><div class="desc">Isabel (isabelgarciasofia3)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img5}" onclick="openModal(data:image/png;base64,{img5}, FILIA"><div class="title">FILIA</div><div class="desc">Santiago Hermosillo (santihermosillo)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img6}" onclick="openModal(data:image/png;base64,{img6}, PARASOUL"><div class="title">PARASOUL</div><div class="desc">Blaine Valentine (BlaineSilverlock)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img7}" onclick="openModal(data:image/png;base64,{img7}, VALENTINE"><div class="title">VALENTINE</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img8}" onclick="openModal(data:image/png;base64,{img8}, SQUIGLY"><div class="title">SQUIGLY</div><div class="desc">VIRUs (G0dnix)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img9}" onclick="openModal(data:image/png;base64,{img9}, BIGBAND"><div class="title">BIGBAND</div><div class="desc">Jake (Stagbeetlex)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img10}" onclick="openModal(data:image/png;base64,{img10}, PAINWHEEL"><div class="title">PAINWHEEL</div><div class="desc">YORUICHI (kiihan4)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img11}" onclick="openModal(data:image/png;base64,{img11}, BEOWULF"><div class="title">BEOWULF</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img12}" onclick="openModal(data:image/png;base64,{img12}, ELIZA"><div class="title">ELIZA</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img13}" onclick="openModal(data:image/png;base64,{img13}, ROBO FORTUNE"><div class="title">ROBO FORTUNE</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img14}" onclick="openModal(data:image/png;base64,{img14}, DAHLIA"><div class="title">DAHLIA</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img15}" onclick="openModal(data:image/png;base64,{img15}, UMBRELLA"><div class="title">UMBRELLA</div><div class="desc">Nezuko Kamado (leslieestradahernandez639)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img16}" onclick="openModal(data:image/png;base64,{img16}, FUKUA"><div class="title">FUKUA</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img17}" onclick="openModal(data:image/png;base64,{img17}, ANNIE"><div class="title">ANNIE</div><div class="desc">luz25 Casasola (luzariadnacasasola)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img18}" onclick="openModal(data:image/png;base64,{img18}, MARIE"><div class="title">MARIE</div><div class="desc">Neko_Niki (CanyaKrash)</div></div>'


f'    <div class="slide"><img src="data:image/png;base64,{img1}" onclick="openModal(data:image/png;base64,{img1}, CEREBELLA")><div class="title">CEREBELLA</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img2}" onclick="openModal(data:image/png;base64,{img2}, PEACOCK"><div class="title">PEACOCK</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img3}" onclick="openModal(data:image/png;base64,{img3}, NADIA (MS.) FORTUNE"><div class="title">NADIA "MS." FORTUNE</div><div class="desc">クミ 𓂃 ✒️ ωω𝗑𝗌𝗄𝗂 、zZz (wwxski)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img4}" onclick="openModal(data:image/png;base64,{img4}, DOUBLE"><div class="title">DOUBLE</div><div class="desc">Isabel (isabelgarciasofia3)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img5}" onclick="openModal(data:image/png;base64,{img5}, FILIA"><div class="title">FILIA</div><div class="desc">Santiago Hermosillo (santihermosillo)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img6}" onclick="openModal(data:image/png;base64,{img6}, PARASOUL"><div class="title">PARASOUL</div><div class="desc">Blaine Valentine (BlaineSilverlock)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img7}" onclick="openModal(data:image/png;base64,{img7}, VALENTINE"><div class="title">VALENTINE</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img8}" onclick="openModal(data:image/png;base64,{img8}, SQUIGLY"><div class="title">SQUIGLY</div><div class="desc">VIRUs (G0dnix)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img9}" onclick="openModal(data:image/png;base64,{img9}, BIGBAND"><div class="title">BIGBAND</div><div class="desc">Jake (Stagbeetlex)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img10}" onclick="openModal(data:image/png;base64,{img10}, PAINWHEEL"><div class="title">PAINWHEEL</div><div class="desc">YORUICHI (kiihan4)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img11}" onclick="openModal(data:image/png;base64,{img11}, BEOWULF"><div class="title">BEOWULF</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img12}" onclick="openModal(data:image/png;base64,{img12}, ELIZA"><div class="title">ELIZA</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img13}" onclick="openModal(data:image/png;base64,{img13}, ROBO FORTUNE"><div class="title">ROBO FORTUNE</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img14}" onclick="openModal(data:image/png;base64,{img14}, DAHLIA"><div class="title">DAHLIA</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img15}" onclick="openModal(data:image/png;base64,{img15}, UMBRELLA"><div class="title">UMBRELLA</div><div class="desc">Nezuko Kamado (leslieestradahernandez639)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img16}" onclick="openModal(data:image/png;base64,{img16}, FUKUA"><div class="title">FUKUA</div><div class="desc"></div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img17}" onclick="openModal(data:image/png;base64,{img17}, ANNIE"><div class="title">ANNIE</div><div class="desc">luz25 Casasola (luzariadnacasasola)</div></div>'
f'    <div class="slide"><img src="data:image/png;base64,{img18}" onclick="openModal(data:image/png;base64,{img18}, MARIE"><div class="title">MARIE</div><div class="desc">Neko_Niki (CanyaKrash)</div></div>'

'  </div>'
'</div>'
)

# ==============================
# MODAL + SCRIPT (ANTES DEL RENDER)
# ==============================
html += """
<div id="myModal" class="modal">
  <div class="modal-content">
    <span class="close" onclick="closeModal()">&times;</span>
    <img id="modal-img">
    <div id="modal-title" class="modal-title"></div>
    <div id="modal-desc" class="modal-desc"></div>
  </div>
</div>

<script>
function openModal(img, title, desc) {
    document.getElementById("myModal").style.display = "block";
    document.getElementById("modal-img").src = img;
    document.getElementById("modal-title").innerText = title;
    document.getElementById("modal-desc").innerText = desc;
}

function closeModal() {
    document.getElementById("myModal").style.display = "none";
}

window.onclick = function(event) {
    const modal = document.getElementById("myModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
</script>
"""

# ==============================
# RENDER FINAL
# ==============================
st.markdown(css + html, unsafe_allow_html=True)




st.divider() 























# ==============================
# MEME DEL DÍA
# ==============================


import base64
import streamlit as st

# 🔢 Cambia SOLO este nombre cada día
nombre_imagen = "skull_meme_30.png"

try:
    with open(nombre_imagen, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode("utf-8")

    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(88,28,135,0.25), rgba(168,85,247,0.15));
        padding:22px;
        border-radius:18px;
        margin:35px 0 60px 0; /* 👈 espacio extra debajo */
        border: 1px solid rgba(168,85,247,0.35);
        box-shadow: 0 4px 22px rgba(168,85,247,0.25);
        text-align:center;
    ">
    
    <h3 style="
        color:#f5f3ff;
        margin:10px 0 16px 0; /* 👈 menos espacio arriba/abajo */
        letter-spacing:0.6px;
        font-family: 'Trebuchet MS', sans-serif;
        font-size:22px;
    ">
        Skullmomazo del día 💀
    </h3>
    """, unsafe_allow_html=True)

    # Imagen centrada
    st.markdown(f"""
        <div style="display:flex; justify-content:center;">
            <img src="data:image/png;base64,{img_base64}"
                 style="
                    max-width:600px;
                    width:100%;
                    max-height:500px;
                    object-fit:contain;
                    border-radius:14px;
                    box-shadow:0 0 20px rgba(0,0,0,0.45);
                 ">
        </div>
    """, unsafe_allow_html=True)

    # Descripción centrada
    st.markdown("""
        <p style="
            color:#ddd6fe;
            font-size:15px;
            margin-top:18px;
            text-align:center;
            font-style:italic;
        ">
            Fortune Presents
        </p>

    </div>
    """, unsafe_allow_html=True)

except FileNotFoundError:
    st.info("No se encontró el meme de hoy.")



















#Para establecer ciclo horario
# ==============================
# ESTABLECER CICLO DE TEMPORADA
# ==============================

from datetime import datetime, timedelta

def obtener_inicio_temporada():
    ahora = datetime.now()

    # Lunes = 0
    dias_desde_lunes = ahora.weekday()

    ultimo_lunes = ahora - timedelta(days=dias_desde_lunes)

    # Ajustamos a lunes 12:00
    inicio_temporada = ultimo_lunes.replace(
        hour=12,
        minute=0,
        second=0,
        microsecond=0
    )

    # Si aún no llega el lunes 12:00 de esta semana
    if ahora < inicio_temporada:
        inicio_temporada -= timedelta(days=7)

    return inicio_temporada









# ==============================
# LIMPIEZA AUTOMÁTICA POR TEMPORADA
# ==============================

def limpiar_por_temporada():
    try:
        with open("comentarios.txt", "r", encoding="utf-8") as f:
            contenido = f.read()

        # Unificar delimitadores
        contenido = contenido.replace("===\n", "§§§")
        bloques = contenido.split("§§§")

        inicio_temporada = obtener_inicio_temporada()
        inicio_siguiente = inicio_temporada + timedelta(days=7)

        bloques_validos = []

        for bloque in bloques:
            bloque = bloque.strip()
            if not bloque:
                continue

            if "Fecha:" in bloque:
                lineas = bloque.split("\n")
                fecha_texto = ""

                for linea in lineas:
                    if linea.startswith("Fecha:"):
                        fecha_texto = linea.replace("Fecha:", "").strip()

                if fecha_texto:
                    try:
                        fecha_comentario = datetime.strptime(
                            fecha_texto,
                            "%Y-%m-%d %H:%M:%S"
                        )
                    except:
                        continue

                    # Validar si pertenece a la temporada actual
                    if inicio_temporada <= fecha_comentario < inicio_siguiente:
                        bloques_validos.append(bloque + "\n===\n")

        # Reescribir archivo solo con temporada actual
        with open("comentarios.txt", "w", encoding="utf-8") as f:
            for bloque in bloques_validos:
                f.write(bloque)

    except FileNotFoundError:
        pass




inicio = obtener_inicio_temporada()
fin = inicio + timedelta(days=7)

st.caption(
    f"🗓 Temporada activa: "
    f"{inicio.strftime('%d %b %H:%M')} - "
    f"{fin.strftime('%d %b %H:%M')}"
)





#Para Comentarios

import streamlit as st
import base64
from datetime import datetime

st.markdown("---")
st.subheader("💬 Comentarios de la Alianza")

nombre = st.text_input("Tu nombre o Nick")
comentario = st.text_area("Escribe tu comentario")
imagen = st.file_uploader("Adjuntar imagen (opcional)", type=["png", "jpg", "jpeg"])

if st.button("Enviar comentario"):
    if nombre and comentario:
        
        img_base64 = ""
        if imagen is not None:
            img_bytes = imagen.read()
            img_base64 = base64.b64encode(img_bytes).decode("utf-8")

        with open("comentarios.txt", "a", encoding="utf-8") as f:
            f.write(f"Nombre:{nombre}\n")
            f.write(f"Mensaje:{comentario}\n")
            f.write(f"Imagen:{img_base64}\n")
            f.write(f"Fecha:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("===\n")

        st.success("¡Comentario enviado!")
    else:
        st.warning("Completa Nombre y Mensaje")

st.divider()


#Para mostrar los comentarios

st.subheader("🌟 Opiniones de los Miembros")

try:
    with open("comentarios.txt", "r", encoding="utf-8") as f:
        contenido = f.read()

    # Unificamos delimitadores
    contenido = contenido.replace("===\n", "§§§")
    contenido = contenido.replace("---\n", "§§§")

    bloques = contenido.split("§§§")

    for bloque in reversed(bloques):
        bloque = bloque.strip()
        if not bloque:
            continue

        nombre = ""
        mensaje = ""
        img_data = ""

        # Detectar formato nuevo
        if "Nombre:" in bloque and "Mensaje:" in bloque:
            lineas = bloque.split("\n")
            for linea in lineas:
                if linea.startswith("Nombre:"):
                    nombre = linea.replace("Nombre:", "").strip()
                elif linea.startswith("Mensaje:"):
                    mensaje = linea.replace("Mensaje:", "").strip()
                elif linea.startswith("Imagen:"):
                    img_data = linea.replace("Imagen:", "").strip()

        # Detectar formato antiguo
        elif ":" in bloque:
            partes = bloque.split(":", 1)
            nombre = partes[0].strip()
            mensaje = partes[1].strip()

        # Renderizado
        st.markdown(f"""
        <div style="
            background: rgba(99,102,241,0.08);
            padding:18px;
            border-radius:14px;
            margin-bottom:16px;
            box-shadow:0 0 18px rgba(99,102,241,0.25);
        ">
            <strong style="color:#a5b4fc; font-size:15px;">{nombre}</strong>
            <p style="color:#e5e7eb; margin:8px 0 12px 0;">{mensaje}</p>
        """, unsafe_allow_html=True)

        # Imagen ampliable
        if img_data:
            st.markdown(f"""
            <details>
                <summary style="cursor:pointer; color:#c4b5fd;">
                    📎 Ver imagen adjunta
                </summary>
                <br>
                <img src="data:image/png;base64,{img_data}"
                     style="
                        max-width:400px;
                        width:100%;
                        border-radius:12px;
                        box-shadow:0 0 20px rgba(255,255,255,0.3);
                     ">
            </details>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

except FileNotFoundError:
    st.info("Aún no hay comentarios.")










#Para Limpieza Manual

st.divider()

admin_pass = st.text_input("Clave admin", type="password")

if admin_pass == "CHESSCOM":
    st.success("Acceso concedido")
    
    if st.button("🗑️ Borrar chat completamente"):
        open("comentarios.txt", "w").close()
        st.success("Chat eliminado correctamente.")



st.divider()








# ==============================
# CONTACTO PRIVADO CON EL ADMIN
# ==============================

import streamlit as st

st.markdown("""
<style>
/* Tarjeta principal */
.contact-card {
    background: #111827; /* fondo oscuro */
    padding: 32px 24px;
    border-radius: 18px;
    margin: 40px auto 60px auto;
    border: 1px solid rgba(147,197,253,0.25); /* azul tenue */
    box-shadow: 0 6px 20px rgba(0,0,0,0.45);
    text-align: center;
    max-width: 600px;
}

/* Título */
.contact-card h3 {
    color: #93c5fd; /* azul claro */
    font-size: 22px;
    margin-bottom: 16px;
    font-weight: 600;
}

/* Texto */
.contact-card p {
    color: #d1d5db;
    font-size: 15px;
    margin-bottom: 28px;
    line-height: 1.6;
}

/* Contenedor de botones */
.contact-buttons {
    display: flex;
    flex-direction: column;
    gap: 14px;
}

/* Botón base */
.contact-buttons a {
    display: block;
    padding: 12px 20px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: 600;
    border: 2px solid #60a5fa; /* azul */
    color: #60a5fa;
    transition: all 0.3s ease;
}

/* Hover */
.contact-buttons a:hover {
    background: #60a5fa;
    color: #111827;
}
</style>

<div class="contact-card">
    <h3>🔐 Contacto Privado con CHESSDEV</h3>
    <p>
        ¿Deseas hablar directamente conmigo?<br>
        Puedes contarme lo que quieras con confianza, respeto tu opinión 💚
    </p>
    <div class="contact-buttons">
        <a href="https://wa.me/50248320737" target="_blank">CHESSDEV CONTACT</a>
        <a href="https://www.youtube.com/channel/UC3E1IMA4c6-U-_atZOomvPw" target="_blank">CHESSDEV CHANNEL</a>
    </div>
</div>
""", unsafe_allow_html=True)





st.divider()









# ==============================
# MIS ÚLTIMAS NOVEDADES
# ==============================

import streamlit as st

st.markdown("""
    <style>
    /* Encapsulamos TODO dentro de #ultimo-video-section */
    #ultimo-video-section {
        padding: 60px 20px;
        text-align: center;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
        margin-top: 80px;
        position: relative;
        z-index: 1;
        animation: fadeInUp 1.2s ease-out;
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0); }
    }

/* NEW badge */
#ultimo-video-section .new-badge {
    position: absolute;
    top: 20px;
    right: 20px;
    background: #ff2b2b;
    color: white;
    font-weight: bold;
    padding: 8px 14px;
    border-radius: 20px;
    font-size: 0.9rem;
    letter-spacing: 1px;
    box-shadow: 0 0 15px rgba(255, 43, 43, 0.8);
    animation: pulseNew 1.5s infinite ease-in-out;
}

@keyframes pulseNew {
    0% { transform: scale(1); box-shadow: 0 0 10px rgba(255, 43, 43, 0.6); }
    50% { transform: scale(1.1); box-shadow: 0 0 25px rgba(255, 43, 43, 1); }
    100% { transform: scale(1); box-shadow: 0 0 10px rgba(255, 43, 43, 0.6); }
}
            
    /* Partículas SOLO dentro de esta sección */
    #ultimo-video-section .particlesB {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: 0;
        overflow: hidden;
        pointer-events: none;
    }
    #ultimo-video-section .particleB {
        position: absolute;
        background: rgba(0,255,163,0.8);
        border-radius: 50%;
        animation: float 15s infinite ease-in-out;
    }
    @keyframes float {
        0% { transform: translateY(0) translateX(0); opacity: 1; }
        25% { transform: translateY(-60px) translateX(30px); opacity: 0.7; }
        50% { transform: translateY(-30px) translateX(-30px); opacity: 0.5; }
        75% { transform: translateY(40px) translateX(20px); opacity: 0.8; }
        100% { transform: translateY(0) translateX(0); opacity: 1; }
    }

    /* Título encapsulado */
    #ultimo-video-section .ultimo-video-title {
        font-size: 2.8rem;
        font-weight: bold;
        margin-bottom: 10px;
        color: #ffffff;
        text-shadow: 0 0 15px #00ffa3, 0 0 30px #00c3ff;
        animation: greenGlow 2s infinite alternate;
        transition: transform 0.3s ease;
    }
    @keyframes greenGlow {
        from { text-shadow: 0 0 15px #00ffa3; }
        to { text-shadow: 0 0 30px #00c3ff; }
    }
    #ultimo-video-section .ultimo-video-title:hover {
        transform: scale(1.08);
    }

    /* Línea decorativa encapsulada */
    #ultimo-video-section .ultimo-video-line {
        width: 100px;
        height: 4px;
        background: linear-gradient(90deg, #00ffa3, #00c3ff);
        margin: 0 auto 20px auto;
        border-radius: 2px;
        box-shadow: 0 0 15px rgba(0,255,163,0.8);
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scaleX(1); opacity: 1; }
        50% { transform: scaleX(1.3); opacity: 0.6; }
        100% { transform: scaleX(1); opacity: 1; }
    }

    /* Video encapsulado */
    #ultimo-video-section .ultimo-video-box {
        max-width: 800px;
        margin: 0 auto;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 0 25px rgba(0,255,163,0.6);
        transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    #ultimo-video-section .ultimo-video-box:hover {
        transform: scale(1.03);
        box-shadow: 0 0 50px rgba(0,255,163,1);
    }

    #ultimo-video-section iframe {
        width: 100%;
        height: 450px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Sección encapsulada con partículas
st.markdown("""
<div id="ultimo-video-section">
  <div class="new-badge">NEW</div>
  <h2 class="ultimo-video-title">
      Mi <span>Último Video</span>
  </h2>
  <div class="ultimo-video-line"></div>
  <p style="font-size:1.2rem; margin-bottom:40px;">
      Aquí te comparto mi más reciente novedad en el canal.
  </p>
  <div class="ultimo-video-box">
      <iframe src="https://www.youtube.com/embed/6cmAFt-dnBI" 
              title="YouTube video player" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen>
      </iframe>
  </div>
</div>
""", unsafe_allow_html=True)



st.divider()











#===========================================
# LAST VERSION / ALL MUSIC OST
#===========================================

#Para ambientar la web (bloque opcional)

import streamlit as st
import streamlit.components.v1 as components
import base64

def load_audio_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        return base64.b64encode(data).decode()

# 🔊 Cargar audios locales
audio_tipe = load_audio_base64("tipe_beat_web.mp3")
audio_rnb = load_audio_base64("tipe_beat_web R&B Remix.mp3")
audio_rnb2 = load_audio_base64("tipe_beat_web R&B 2 Remix.mp3")
audio_rock = load_audio_base64("tipe_beat_web Rock Remix.mp3")
audio_trap = load_audio_base64("tipe_beat_web Trap Remix.mp3")
audio_drill = load_audio_base64("tipe_beat_web Drill Remix.mp3")
audio_techno = load_audio_base64("tipe_beat_web Techno Remix.mp3")

st.markdown("## 🌿 Ambiente")

with st.expander("🎧 Música ambiental (opcional)", expanded=False):
    st.caption("Activa el sonido si deseas una experiencia más inmersiva. Elige tu versión favorita:")

    components.html(f"""
    <style>
    .music-buttons {{
        display: flex;
        justify-content: center;
        gap: 18px;
        margin: 25px 0;
        flex-wrap: wrap;
    }}
    .music-buttons button {{
        padding: 14px 26px;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        cursor: pointer;
        color: white;
        font-size: 16px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .music-buttons button:hover {{
        transform: scale(1.08);
        box-shadow: 0 0 20px rgba(255,255,255,0.7);
    }}
    .btn-tipe {{ background: linear-gradient(135deg,#7c3aed,#a78bfa); }}
    .btn-rnb {{ background: linear-gradient(135deg,#ec4899,#f472b6); }}
    .btn-rnb2 {{ background: linear-gradient(135deg, #03a9f4, #3498db); }}
    .btn-rock {{ background: linear-gradient(135deg,#ef4444,#f87171); }}
    .btn-trap {{ background: linear-gradient(135deg,#22c55e,#4ade80); }}
    .btn-lofi {{ background: linear-gradient(135deg,#06b6d4,#60a5fa); }}
    .btn-drill {{ background: linear-gradient(135deg, #ffd700, #f5e647); }}
    .btn-techno {{ background: linear-gradient(135deg, #75002D, #ad0341); }}
    </style>

    <div class="music-buttons">
        <button class="btn-tipe" onclick="playMusic('{audio_tipe}')">Tipe beat</button>
        <button class="btn-rnb" onclick="playMusic('{audio_rnb}')">R&B</button>
        <button class="btn-rnb2" onclick="playMusic('{audio_rnb2}')">R&B 2</button>
        <button class="btn-rock" onclick="playMusic('{audio_rock}')">Rock</button>
        <button class="btn-trap" onclick="playMusic('{audio_trap}')">Trap</button>
        <button class="btn-drill" onclick="playMusic('{audio_drill}')">Drill</button>
        <button class="btn-techno" onclick="playMusic('{audio_techno}')">Techno</button>
    </div>

    <audio id="bg-music" controls loop style="width:100%; margin-top:15px; filter: invert(1) hue-rotate(180deg) brightness(0.9) contrast(0.9);"></audio>

    <script>
    function playMusic(base64Audio) {{
        var player = document.getElementById('bg-music');
        player.src = "data:audio/mp3;base64," + base64Audio;
        player.loop = true;
        player.play();
    }}
    </script>
    """, height=300)


st.divider()







# ==============================
# THANKS YOU »alex«
# ==============================


import streamlit as st
import base64

def img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

img_colider = img_base64("Thanks_colider.png")

html_code = f"""
<style>
.tribute-card {{
  max-width:950px;
  margin:60px auto;
  padding:60px 40px 80px;
  background:linear-gradient(180deg,#0a0c12,#111827 60%,#05070b);
  border-radius:30px;
  border:1px solid rgba(255,215,0,0.25);
  box-shadow:0 0 80px rgba(255,215,0,0.15), inset 0 0 60px rgba(255,215,0,0.08);
  text-align:center;
  position:relative;
  overflow:hidden;
}}
.tribute-title {{
  font-size:34px;
  color:#fff;
  margin-bottom:30px;
  letter-spacing:2px;
  font-weight:bold;
  text-shadow:0 0 25px rgba(0, 0, 0, 0.8);
}}
.tribute-text {{
  font-size:16px;
  color:#d1d5db;
  line-height:1.8;
  margin-bottom:20px;
  max-width:950px;
  margin-left:auto;
  margin-right:auto;
  word-wrap: break-word;
  overflow-wrap: break-word;
}}
.colider-avatar {{
  width:140px;
  height:140px;
  border-radius:50%;
  object-fit:cover;
  border:4px solid #ffd700;
  box-shadow:0 0 35px rgba(255,215,0,0.7),0 0 70px rgba(255,215,0,0.3);
  display:block;
  margin:40px auto -70px auto;
  position:relative;
  z-index:10;
  background:#000;
}}

/* Estilo para el SVG del pedestal, ajustado a tamaño y posición */
.pedestal-container {{
  margin-top: -20px; /* ajusta si quieres más espacio */
  display: flex;
  justify-content: center;
  align-items: flex-end;
}}

.pedestal-svg {{
  width: 220px;
  height: 250px;
}}

/* Opcional: efectos en el SVG */
.pedestal-svg polygon {{
  stroke: #d3a410;
  stroke-width: 2;
  fill: #414750;
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
}}
</style>

<div class="tribute-card">
  <div class="tribute-title">Homenaje a »alex«</div>
  <div class="tribute-text" style="margin-top:30px; padding:0 20px; color:#d1d5db; font-size:16px; line-height:1.6;">
  <p>
    Hoy queremos expresar nuestro más sincero agradecimiento por todo el tiempo,
    esfuerzo y dedicación que brindaste a este gremio. Tu presencia marcó una etapa
    importante que siempre será recordada.
    Gracias por cada momento, cada decisión y cada esfuerzo dedicado a este gremio.
    Tu impacto permanecerá con nosotros.
  </p>
  <p>
    Comprendemos tu decisión. Sabemos que hay momentos donde la vida exige prioridad,
    y elegir ese camino demuestra responsabilidad y fortaleza.
    Entendemos tu decisión y la respetamos profundamente. Hay momentos donde la vida
    exige prioridad, y eso también es parte del camino.
  </p>
  <p>
    Esto no es una despedida definitiva. Este gremio siempre será tu hogar.
    Cuando decidas volver, serás recibido con el mismo respeto y aprecio.
    Este nunca será un adiós. Siempre tendrás un lugar aquí.
    Cuando decidas volver, serás bienvenido.
  </p>
</div>
  <img src="data:image/png;base64,{img_colider}" class="colider-avatar">
  <!-- Contenedor del pedestal con SVG -->
  <div class="pedestal-container">
    <svg class="pedestal-svg" xmlns="http://www.w3.org/2000/svg" height="250" width="220" viewBox="0 0 200 200">
      <g style="order: -1;">
        <polygon transform="rotate(45 100 100)" stroke-width="1" stroke="#d3a410" fill="none" points="70,70 148,50 130,130 50,150" id="bounce"></polygon>
        <polygon transform="rotate(45 100 100)" stroke-width="1" stroke="#d3a410" fill="none" points="70,70 148,50 130,130 50,150" id="bounce2"></polygon>
        <polygon transform="rotate(45 100 100)" stroke-width="2" stroke="" fill="#414750" points="70,70 150,50 130,130 50,150"></polygon>
        <polygon stroke-width="2" stroke="" fill="url(#gradiente)" points="100,70 150,100 100,130 50,100"></polygon>
        <defs>
          <linearGradient y2="100%" x2="10%" y1="0%" x1="0%" id="gradiente">
            <stop style="stop-color: #1e2026;stop-opacity:1" offset="20%"></stop>
            <stop style="stop-color:#414750;stop-opacity:1" offset="60%"></stop>
          </linearGradient>
        </defs>
        <polygon transform="translate(20, 31)" stroke-width="2" stroke="" fill="#b7870f" points="80,50 80,75 80,99 40,75"></polygon>
        <polygon transform="translate(20, 31)" stroke-width="2" stroke="" fill="url(#gradiente2)" points="40,-40 80,-40 80,99 40,75"></polygon>
        <defs>
          <linearGradient y2="100%" x2="0%" y1="-17%" x1="10%" id="gradiente2">
            <stop style="stop-color: #d3a51000;stop-opacity:1" offset="20%"></stop>
            <stop style="stop-color:#d3a51054;stop-opacity:1" offset="100%"></stop>
          </linearGradient>
        </defs>
        <polygon transform="rotate(180 100 100) translate(20, 20)" stroke-width="2" stroke="" fill="#d3a410" points="80,50 80,75 80,99 40,75"></polygon>
        <polygon transform="rotate(0 100 100) translate(60, 20)" stroke-width="2" stroke="" fill="url(#gradiente3)" points="40,-40 80,-40 80,85 40,110.2"></polygon>
        <defs>
          <linearGradient y2="100%" x2="10%" y1="0%" x1="0%" id="gradiente3">
            <stop style="stop-color: #d3a51000;stop-opacity:1" offset="20%"></stop>
            <stop style="stop-color:#d3a51054;stop-opacity:1" offset="100%"></stop>
          </linearGradient>
        </defs>
        <polygon transform="rotate(45 100 100) translate(80, 95)" stroke-width="2" stroke="" fill="#ffe4a1" points="5,0 5,5 0,5 0,0" id="particles"></polygon>
        <polygon transform="rotate(45 100 100) translate(80, 55)" stroke-width="2" stroke="" fill="#ccb069" points="6,0 6,6 0,6 0,0" id="particles"></polygon>
        <polygon transform="rotate(45 100 100) translate(70, 80)" stroke-width="2" stroke="" fill="#fff" points="2,0 2,2 0,2 0,0" id="particles"></polygon>
        <polygon stroke-width="2" stroke="" fill="#292d34" points="29.5,99.8 100,142 100,172 29.5,130"></polygon>
        <polygon transform="translate(50, 92)" stroke-width="2" stroke="" fill="#1f2127" points="50,50 120.5,8 120.5,35 50,80"></polygon>
      </g>
    </svg>
  </div>
</div>
"""

st.components.v1.html(html_code, height=1600)








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











# ==============================
# NOTAS
# ==============================


#Para dejar divisiones notables (incluye una línea y una hitbox lineal) se usa la función st.divider()

#Para cambiar las URL de enlaces externos (YouTube) se usa la función embed y cambiar el código final de base 64

#Para agregar imágenes se cargan localmente con la función import base 64 y asegurar la extensión

#Para códigos erroneos o de constante error se encapsula todo el código para que funcione y lea la instrucción crrectamente

#Para cuando se repita constantemente el código, se debe dar un prompt indicando que se debe "encapsular"
#todo el código para no confundir las instrucciones con texto plano, por uso de diversos lenguajes.

#Un posible indicador de que el código funciona es que la estructura del bloque lleve varias llaves, 
#señal de que el código leerá las instrucciones de forma más precisa

#En ciertas ocasiones el código puede confundir las notas "#"" con instrucciones, por lo que se pueden remover para renderizar.

#Cuando la página no logre cargar correctamente los videos o URLs externas se debe recargar o borrar Cookies.

#Cuando no haya compatibilidad con Mobile (sistema UX/UI) se debe dar un prompt indicando que solo necesita "reestructuración de compatibilidad"

#Cuando la línea de código no muestra la imagen previa, se debe revisar si tiene la extensión correcra, si existe en el código,
#si el formato asignado es correcto o si la línea de código es incorrecta.

#Si el código no logra renderizar el código puede deberse a que falta una librería o instrucción para mostrar
#como funciones pertenecientes al hosting Streamlit

#Si se desconocen las dimensiones de elementos se puede indicar la instrucción en el prompt para otorgar un código
#con limitaciones, tanto para PC como para Mobile

#Si las dimensiones otorgadas no son las correctas, pero si cuenta con el diseño y funcionalidad, se puede intentar
#encontrar una versión correcta de tamaño, modificando la hitbox con Height para altura y Weidht para ancho.
#(Usualmente se usa más Height para dejar espacio vertical, por si el apartado visual no alcanza)

#Si las imágenes no cuentan con la extensión correcta se pueden usar las herramientas externas de IA para
#cambiar el formato o propiedades (Esta instrucción es muy intuitiva)

#Cuando Se usan archivos grandes/pesados se debe esperar tiempo adicional para actualizar, debido a que son
#archivos que pasan por proceso de conversión a base 64 para renderizar.

#Para secciones que sean demasiado grandes, se debe reducir el tamaño de las dimensiones para evitar 
#que cree un scroll interno, ya que afecta principalmente a la versión Mobile.

#Cuando la página cargue







#FUEGO
#Parasoul - La protegida 📌
#Peacock - Réplica 

#AIRE
#BigBand - Bemol 📌
#Double - Monjerias 📌

#AGUA
#Beowulf - Cold Stones 📌
#Double - Bruja del mar 📌
#

#LUZ
#Dahlia - Trituradora de almas 📌
#Dahlia - Pistolera de oro 📌
#Robo Fortune - M-I4U 📌
#

#OSCURIDAD
#Filia - Descabellada 📌
#Squigly - Pánico Escénico 📌



#python -m streamlit run dashboard.py
