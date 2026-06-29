import streamlit as st


def open_hero_card() -> None:
    st.markdown(
        """
        <div class="hero-card">
        """,
        unsafe_allow_html=True,
    )


def close_hero_card() -> None:
    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True,
    )