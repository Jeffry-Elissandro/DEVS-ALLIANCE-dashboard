"""
components/background/gradients.py
----------------------------------
Renderiza el fondo degradado de la Landing.
"""

import streamlit as st


def render_gradient_background() -> None:
    """
    Inserta el contenedor principal del fondo.

    El diseño visual se controla completamente
    desde landing.css.
    """

    st.markdown(
        """
        <div class="landing-background"></div>
        """,
        unsafe_allow_html=True,
    )