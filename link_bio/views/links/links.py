import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("My Currículum"),
        link_button(
            "Currículum", 
            "Download my Currículum",
            
            "https://www.dropbox.com/scl/fi/bqf78sw21u01kiipomjcu/Hoja-de-vida-Gerente-de-proyectos-Minimalista-Morado.pdf?rlkey=ru8f45m1p3pxwigoapg5z3oo7&st=bkvk55kw&dl=1", 
        ),
        title("My Networks"),
        link_button(
            "LinkedIn", 
            "Visit my LinkedIn",
            
            "https://www.linkedin.com/in/brayan-zapata-17481130b/", 
        ),
        link_button(
            "GitHub", 
            "Visit my GitHub",
            
            "https://github.com/Kxcwrx?tab=repositories", 
        ),

        link_button(
            "Instagram", 
            "Visit my personal Instagram",
            
            "https://www.instagram.com/", 
        ),

        link_button(
            "TikTok", 
            "Visit my personal TikTok",
            
            "https://www.tiktok.com/@kxcwr", 
        ),
        width="100%",
        padding_top="1px",
    )