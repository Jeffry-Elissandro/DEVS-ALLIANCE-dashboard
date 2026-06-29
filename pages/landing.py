"""
pages/landing.py
------------------------------------
Página de bienvenida de DEV'S ALLIANCE.
"""

from utils.css_loader import load_css_files

from components.background.gradients import render_gradient_background
from components.background.stars import render_star_background

from components.hero.hero import render


def render_page() -> None:
    """
    Renderiza la Landing.
    """

    load_css_files(
        "styles/global.css",
        "styles/landing.css",
        "styles/landing_components.css",
        "styles/landing_animations.css",
    )

    render_gradient_background()

    render_star_background()

    render()