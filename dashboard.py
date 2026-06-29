import streamlit as st

from core.app_state import app_state
from core.router import render


def main() -> None:
    """
    Punto de entrada de DEV'S ALLIANCE.
    """

    st.set_page_config(
        page_title="DEV'S ALLIANCE",
        page_icon="💚",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    render(app_state.current_page)


if __name__ == "__main__":
    main()