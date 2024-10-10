import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar



"""
def project_card(title: str, description: str, link: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(title, font_size="20px", font_weight="bold"),
            rx.text(description, text_align="center"),
            rx.button("Ir", on_click=lambda: rx.redirect(link), background_color="blue", color="white"),
            spacing="10px",
            align_items="center"
        ),
        border="1px solid #ccc",
        border_radius="10px",
        padding="20px",
        width="300px",
        height="200px",
        box_shadow="lg",
        _hover={"box_shadow": "xl"},
    )

"""


def projects_page() -> rx.Component:
    return rx.box(
        navbar(),


        rx.center(
            rx.text("My Projects", font_size="30px", font_weight="bold", margin="20px auto"),
            margin_top="20px"
        ),




        rx.box(
            rx.center(
                footer(),
                style={"position": "absolute", "bottom": "0", "width": "100%", "text_align": "center", "padding": "10px"},
            )
            
        ),
    )