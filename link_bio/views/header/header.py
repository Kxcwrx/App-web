import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size as Size
from link_bio.components.info_text import info_text as info_text
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color




def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="BrayanDev", 
                size="xl",
                padding="2px",
                src="", 
                color=TextColor.BODY.value,
                bg="white",
                border="4px",
                border_color="white"
                ),



            rx.vstack(

                rx.heading(
                    "Brayan Zapata", 
                    size="lg",
                    line_height="1.2",
                    color=TextColor.HEADER.value,
                ),
                rx.text(
                    "@Brayandev",
                    margin_top="0px !important",
                    line_height="1.2",
                    color=TextColor.BODY.value
                ),
                spacing="4px",
                align_items="start"
            ),
            spacing=Size.DEFAULT.value

        ),

        #rx.flex(
            #info_text("+13", "Años de experiencia")

        #),
        
        # Texto descriptivo en un nuevo elemento de vstack
        rx.text(
            """I am a junior software developer seeking opportunities 
            to grow as a backend developer and contribute to innovative projects. 
            I have experience with programming languages and frameworks such as Python, Reflex, and FastAPI, 
            as well as databases like SQL Server. Additionally, I am proficient with tools like Git and GitHub. 
            I am eager to keep learning and contribute in a dynamic and challenging environment.""",
            align_items="start",
            color=TextColor.BODY.value,
            font_size="18px"
        ),
        
        align_items="start",  # Centrar todo horizontalmente
        spacing=Size.BIG.value  # Espaciado entre los elementos de `vstack`
    )
