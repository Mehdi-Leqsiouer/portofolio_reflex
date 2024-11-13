"""The home page of the app."""

from portofolio_reflex.templates.template import template
from portofolio_reflex.components.test import create_portfolio_page

import reflex as rx


@template(route="/", title="Home", image="/reflex.png")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """

    return create_portfolio_page()
