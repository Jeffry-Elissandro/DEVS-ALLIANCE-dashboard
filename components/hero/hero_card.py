"""
components/hero/hero_card.py
------------------------------------
Contenedor principal de la Hero Section.
"""

import streamlit as st


def open_hero_card() -> None:
    """
    Abre la tarjeta principal.
    """

    st.markdown(
        """
        <main class="landing">

            <section class="hero-card">
        """,
        unsafe_allow_html=True,
    )


def close_hero_card() -> None:
    """
    Cierra la tarjeta principal.
    """

    st.markdown(
        """
            </section>

        </main>
        """,
        unsafe_allow_html=True,
    )