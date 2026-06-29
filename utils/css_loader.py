"""
utils/css_loader.py
------------------------------------
Utilidades para cargar hojas de estilo CSS.
"""

from pathlib import Path

import streamlit as st


def load_css(css_file: str) -> None:
    """
    Carga un único archivo CSS.
    """

    path = Path(css_file)

    if not path.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo CSS: {css_file}"
        )

    with open(path, "r", encoding="utf-8") as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True,
        )


def load_css_files(*css_files: str) -> None:
    """
    Carga varios archivos CSS.

    Ejemplo:

    load_css_files(
        "styles/global.css",
        "styles/landing.css",
        "styles/cards.css",
    )
    """

    for css in css_files:
        load_css(css)