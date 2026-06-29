# core/router.py

from config import routes

from pages import (
    landing,
    dashboard,
    home,
    legacy,
    rules,
    progress,
    season,
    statistics,
    strategy,
    community,
    gallery,
    comments,
    contact,
    media,
)

ROUTES = {
    routes.LANDING: landing.render_page,
    routes.DASHBOARD: dashboard.render,
    routes.HOME: home.render,
    routes.LEGACY: legacy.render,
    routes.RULES: rules.render,
    routes.PROGRESS: progress.render,
    routes.SEASON: season.render,
    routes.STATISTICS: statistics.render,
    routes.STRATEGY: strategy.render,
    routes.COMMUNITY: community.render,
    routes.GALLERY: gallery.render,
    routes.COMMENTS: comments.render,
    routes.CONTACT: contact.render,
    routes.MEDIA: media.render,
}


def get_page(page: str):
    """
    Devuelve la función render() asociada a una ruta.
    """
    return ROUTES.get(page)


def render(page: str) -> None:
    """
    Renderiza la página solicitada.
    """
    page_function = get_page(page)

    if page_function is None:
        raise ValueError(f"Ruta desconocida: {page}")

    page_function()