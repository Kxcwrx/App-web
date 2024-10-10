import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

#Constants
MAX_WIDTH = "600px"

#Sizes

class Size(Enum):
    ZERO = "0px !important" 
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    LARGE = "1.5em"

#Styles 

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
       
        "paddings": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "Color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value,
        }

    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
        
    }
}

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    font_family=Font.TITLE.value,  


)

button_body_style = dict(
    font_family=Font.DEFAULT.value,  
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value

)

title_style = dict(
        font_family=Font.TITLE.value,  
        size="lg",
        width="100%",
        padding_top=Size.DEFAULT.value,
        color=TextColor.HEADER.value
)

navbar_title_style = dict(
    font_family=Font.LOGO.value,  


)