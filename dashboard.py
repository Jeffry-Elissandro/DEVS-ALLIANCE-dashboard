import base64
import streamlit as st

from core.app_state import app_state
from core.router import render


def get_base64_image(path: str) -> str:
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()


def main() -> None:
    st.set_page_config(
        page_title="DEV'S ALLIANCE",
        page_icon="💚",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Convertir imagen a Base64
    img_base64 = get_base64_image("filia_study.png")

    # Mostrar imagen y descripción
    st.markdown(
    f"""
    <style>
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 90vh;
            text-align: center;
        }}

        .responsive-img {{
            width: 90%;
            max-width: 900px;
            height: auto;
        }}

        .description {{
            margin-top: 25px;
            font-size: clamp(16px, 2vw, 24px);
            color: #666;
            max-width: 900px;
            line-height: 1.6;
        }}

        @media (max-width: 768px) {{
            .responsive-img {{
                width: 100%;
            }}

            .description {{
                font-size: 16px;
                padding: 0 10px;
            }}
        }}
    </style>

    <div class="container">
        <img class="responsive-img"
             src="data:image/png;base64,{img_base64}">
        <div class="description">
            <b>En Desarrollo...</b><br>
            Página Web en mantenimiento.<br>
            Reestructuración completa del código fuente y nuevo servicio de hosting.<br>
            <b>(Update V10.62)</b>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

    render(app_state.current_page)


if __name__ == "__main__":
    main()