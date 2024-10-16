import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.styles import Size as Size


def link_button(title: str, body: str, url: str, ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value,
                    bg="white",
                    border="4px",
                    border_color="white",
                ),
                rx.vstack(
                    rx.text(
                        title, font_size="20px", 
                        color=TextColor.HEADER.value,
                    ),
                    rx.text(
                        body, font_size="14px", 
                        color=TextColor.BODY.value
                    ),

                    align_items="start",
                    spacing=Size.ZERO.value,
                    margin=Size.SMALL.value,
                ),
                align="center",
                width="100%",
                
                
            )
        ),
        is_external=True,
        width="100%",
        href=url,
        text_decoration="none",
    )