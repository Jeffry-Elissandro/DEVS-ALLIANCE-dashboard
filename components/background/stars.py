"""
components/background/stars.py
----------------------------------
Renderiza el contenedor de estrellas.
"""

import streamlit as st


def render_star_background() -> None:
    """
    Inserta el contenedor donde se mostrarán
    las estrellas animadas.
    """

    stars_html = ""

    # Cantidad de estrellas inicial
    for i in range(120):

        stars_html += '<div class="star"></div>'

    st.markdown(
        f"""
        <div id="star-container">

            {stars_html}

        </div>
        """,
        unsafe_allow_html=True,
    )