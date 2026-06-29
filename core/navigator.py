from core.app_state import app_state


def go_to(page: str) -> None:
    """
    Cambia la página actual de la aplicación.
    """

    if page == app_state.current_page:
        return

    app_state.loading = True

    app_state.previous_page = app_state.current_page
    app_state.current_page = page

    app_state.first_visit = False
    app_state.loading = False


def back() -> None:
    """
    Regresa a la página anterior si existe.
    """

    if app_state.previous_page is None:
        return

    current = app_state.current_page

    app_state.current_page = app_state.previous_page
    app_state.previous_page = current


def reset_navigation() -> None:
    """
    Reinicia completamente el estado de navegación.
    """

    app_state.reset()