import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("My Currículum"),
        link_button(
            "Currículum", 
            "Visit my Currículum",
            "",
            "https://www.linkedin.com/in/brayan-zapata-17481130b/", 
        ),
        title("My Networks"),
        link_button(
            "LinkedIn", 
            "Visit my LinkedIn",
            "",
            "https://www.linkedin.com/in/brayan-zapata-17481130b/", 
        ),

        link_button(
            "Instagram", 
            "Visit my personal Instagram",
            "",  
            "https://www.instagram.com/", 
        ),

        link_button(
            "TikTok", 
            "Visit my personal TikTok",
            "", 
            "https://www.tiktok.com/@kxcwr", 
        ),
        width="100%",
        padding_top="1px",
    )