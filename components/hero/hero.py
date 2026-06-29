from components.hero.hero_card import (
    open_hero_card,
    close_hero_card,
)

from components.hero.hero_logo import render_logo
from components.hero.hero_title import render_title
from components.hero.hero_quote import render_quote
from components.hero.hero_info import render_info
from components.hero.hero_button import render_start_button


def render_hero() -> None:
    """
    Renderiza la Hero Section completa.
    """

    open_hero_card()

    render_logo()

    render_title()

    render_quote()

    render_info()

    render_start_button()

    close_hero_card()