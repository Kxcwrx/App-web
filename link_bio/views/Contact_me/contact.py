import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def contact_card(title: str, description: str, contact_info: str, button_text: str, button_link: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(  # Placeholder for the icon
                width="50px",
                height="50px",
                margin_bottom="10px"
            ),
            rx.text(title, font_size="28px", font_weight="bold", text_align="center"),
            rx.text(description, font_size="18px", text_align="center", color=TextColor.BODY.value),
            rx.text(contact_info, text_align="center", font_size="19px", margin_bottom="10px"),
            rx.link(
                rx.button(
                    button_text,
                    background_color=Color.SECONDARY.value,
                    color="white",
                    _hover={"background_color": "darkblue"},
                    border_radius="0px",
                    padding="10px 20px"
                ),
                href=button_link,
                target="_blank"
            ),
            spacing="10px",
            align_items="center"
        ),
        border="1px solid #ccc",
        border_radius="10px",
        padding="20px",
        width=["90%", "400px"],  # Responsive width: 90% on smaller screens, 400px on larger screens
        height="auto",
        box_shadow="lg",
        _hover={"box_shadow": "xl"},
    )

def contact_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.text("Contact me", font_size="35px", font_weight="bold", margin="20px auto", text_align="center"),
        rx.text(
            "Please contact me through any of the links below.", 
            text_align="center",
            font_size="22px",
            margin="10px auto",
            color=TextColor.BODY.value
        ),
        rx.box(
            rx.hstack(
                contact_card(
                    "Whatsapp",
                    "Contact me by WhatsApp.",
                    "+57 321-668-1554",
                    "Send Whatsapp",
                    "https://wa.me/573216681554"
                ),
                contact_card(
                    "E-mail",
                    "Contact me by email.",
                    "Brayanfha4@gmail.com",
                    "Send E-mail",
                    "mailto:Brayanfha4@gmail.com"
                ),
                spacing="30px",
                justify="center",
                margin_top="50px",
            ),
            display="flex",
            flex_direction="row",  # Default to horizontal
            align_items="center",
            justify_content="center",
            width="100%",
            _media_query={
                "(max-width: 768px)": {
                    "flex_direction": "column"  # Change to vertical on smaller screens
                }
            },
        ),
        rx.box(
            rx.center(
                footer(),
            ),
            margin_top="50px",
        ),
        width="100%",
    )
