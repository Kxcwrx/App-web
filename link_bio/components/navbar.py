# Componentes con entidad

import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.text(
                "Brayan Zapata",
                height="40px",
                font_size="25px",
                font_weight="bold",
                font_family=styles.navbar_title_style,  # Aplicar la fuente Comfortaa
                margin_left="4px",
            ),
            spacing="11px",
        ),
        
        rx.spacer(min_width="20px"),

        rx.hstack(
            rx.link(
                rx.text("Home page", color="white", height="45px", font_size="25px", font_family=styles.navbar_title_style),  # Ajusta el tamaño para pantallas pequeñas
                href="/",
                _hover={
                    "background_color": Color.SECONDARY.value,
                    "color": "black",
                },
                title="Go to Home page"
            ),
            rx.link(
                rx.text("Projects", color="white", height="45px", font_size="25px", font_family=styles.navbar_title_style),  # Ajusta el tamaño para pantallas pequeñas
                href="/projects",
                _hover={
                    "background_color": Color.SECONDARY.value,
                    "color": "black",
                },
                title="View Projects"
            ),
            rx.link(
                rx.text("Contact me", color="white", height="45px", font_size="25px", font_family=styles.navbar_title_style),  # Ajusta el tamaño para pantallas pequeñas
                href="/contact",
                _hover={
                    "background_color": Color.SECONDARY.value,
                    "color": "black",
                },
                title="Contact me"
            ),
            spacing="16px",  # Ajusta el espaciado
        ),

        # Estilo general de la barra de navegación
        wrap="wrap",  # Permite que los elementos se ajusten en dispositivos pequeños
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%",
        align_items="center",
        _responsive={
            "base": {
                "flex_direction": "column",  # Cambia a columna en dispositivos pequeños
                "align_items": "flex-start",  # Alinea al inicio en dispositivos móviles
            },
            "md": {
                "flex_direction": "row",  # Cambia a fila en pantallas medianas y grandes
                "align_items": "center",
            }
        },
    )