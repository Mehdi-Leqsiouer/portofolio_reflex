"""Styles for the app."""

import reflex as rx

border_radius = "0.375rem"
box_shadow = "0px 0px 0px 1px rgba(84, 82, 95, 0.14)"
border = f"1px solid {rx.color('accent', 12)}"
text_color = rx.color("gray", 11)
accent_text_color = rx.color("accent", 10)
accent_color = rx.color("accent", 1)
hover_accent_color = {"_hover": {"color": accent_text_color}}
hover_accent_bg = {"_hover": {"background_color": accent_color}}
content_width_vw = "90vw"
sidebar_width = "20em"


template_page_style = {"padding_top": "1em", "padding_x": ["auto", "1em"], "flex": "1"}

template_content_style = {
    "align_items": "flex-start",
    "box_shadow": box_shadow,
    "border_radius": border_radius,
    "padding": "1em",
    "margin_bottom": "1em",
}

link_style = {
    "color": accent_text_color,
    "text_decoration": "none",
    **hover_accent_color,
}

overlapping_button_style = {
    "background_color": "white",
    "border": border,
    "border_radius": border_radius,
}

base_style = {
    rx.menu.trigger: {
        **overlapping_button_style,
    },
    rx.menu.item: hover_accent_bg,
}

markdown_style = {
    "code": lambda text: rx.code(text, color=accent_text_color, bg=accent_color),
    "a": lambda text, **props: rx.link(
        text,
        **props,
        font_weight="bold",
        color=accent_text_color,
        text_decoration="underline",
        text_decoration_color=accent_text_color,
        _hover={
            "color": accent_color,
            "text_decoration": "underline",
            "text_decoration_color": accent_color,
        },
    ),
}

H1_FONT_SIZE = ["2.2em", "2.4em", "2.5em"]
H2_FONT_SIZE = "1.5em"
H3_FONT_SIZE = "1.35em"
H4_FONT_SIZE = "1.15em"

font_weights = {
    "bold": "800",
    "heading": "700",
    "subheading": "600",
    "section": "600",
}
