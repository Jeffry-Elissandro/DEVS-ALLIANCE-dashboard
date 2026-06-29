import streamlit as st

from components.hero.hero_title import render_title


def render() -> None:
    """
    Renderiza la Hero completa.
    """

    html = f"""
    <div class="hero-card">

        {render_title()}

    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True,
    )