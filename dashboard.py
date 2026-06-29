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
        <div style="text-align:center; margin-bottom:20px;">
            <img src="data:image/png;base64,{img_base64}" width="180">
            <p style="font-size:18px; color:#666;">
                <b>En Desarrollo...</b> Página Web en mantenimiento. 
                Reestructuración completa del código fuente y nuevo servicio de hosting. 
                <b>(Update V10.62)</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render(app_state.current_page)


if __name__ == "__main__":
    main()