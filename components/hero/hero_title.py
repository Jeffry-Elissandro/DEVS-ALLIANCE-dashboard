"""
components/hero/hero_title.py
"""

import streamlit as st


def render_title() -> None:

    st.markdown(
        """
        <div class="title-container">

            <h1>DEV'S ALLIANCE</h1>

            <p class="subtitle">
                Comunidad Oficial del Gremio
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )