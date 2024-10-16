import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.views.Contact_me.contact import contact_page
from link_bio.views.projects.projects import projects_page


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                spacing="1px",
                align_items="center",
                justify="flex-start",
                padding_top="20px",
            )
        ),
        rx.center(
            footer(),
            margin_top="5px",
        ),
    )




# Crear la app
app = rx.App(style=styles.BASE_STYLE)

# Añadir las páginas
app.add_page(
    index, 
    title="Brayandev",
    description="Hi, I'm Brayan. Software Developer",
    image="",
    route="/")

app.add_page(
    contact_page,
    title="Contact me",
    image="/",
    route="/contact")

app.add_page(
    projects_page,
    title="Projects", 
    route="/projects")



# Ejecutar la app
app._compile()
