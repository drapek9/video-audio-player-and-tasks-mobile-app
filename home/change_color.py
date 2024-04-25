from inputs import *
from home.helper import colors

# function for changing color in mainhome.py class

def change_color_def(home_class):
    previous_color = home_class.ids.title.color
    the_color = previous_color
    while the_color == previous_color:
        the_color = random.choice(colors)
    home_class.ids.title.color = the_color
    if the_color == "yellow":
        home_class.ids.title.md_bg_color = "black"
    else:
        home_class.ids.title.md_bg_color = "white"