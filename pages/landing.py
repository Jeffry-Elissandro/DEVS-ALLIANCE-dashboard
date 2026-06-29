"""
pages/landing.py
------------------------------------
Página de bienvenida de DEV'S ALLIANCE.
"""

from styles.landing import load_landing_styles

from components.background.gradients import render_gradient_background
from components.background.stars import render_star_background

from components.hero.hero import render_hero


def render() -> None:
    """
    Renderiza la página de bienvenida.
    """

    # Cargar estilos
    load_landing_styles()

    # Fondo
    render_gradient_background()
    render_star_background()

    # Hero principal
    render_hero()