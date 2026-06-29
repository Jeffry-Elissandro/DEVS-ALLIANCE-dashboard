"""
components/hero/hero_logo.py
------------------------------------
Logo principal del Landing.
"""

import streamlit as st


def render_logo() -> None:

    st.markdown(
        """
        <div class="logo-container">

            <div class="logo-placeholder">

                LOGO

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )