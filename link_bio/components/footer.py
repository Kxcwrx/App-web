import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src=""),
        rx.link(
            f"@2022-{datetime.date.today().year} BRAYANDEV V3.",
            href="",
            is_external=True,
            font_size=Size.MEDIUM.value,
            

        ),
        rx.text("BY BRAYAN ZAPATA V3. SOFTWARE DEVELOPMENT", font_size=Size.DEFAULT.value),
        padding_y="0px", 
        padding_x=Size.BIG.value, # Ajusta el `padding
        position="relative",
        margin_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value,
    )
    


    