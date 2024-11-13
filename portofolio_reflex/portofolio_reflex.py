"""Welcome to Reflex!."""

from portofolio_reflex import styles

# Import all the pages.
from portofolio_reflex.pages.index import page

import reflex as rx

# Create the app.
app = rx.App(style=styles.base_style)
