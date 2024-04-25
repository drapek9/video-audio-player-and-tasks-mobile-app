from inputs import *
from list.no_text_typed import no_text_function, cancel_clock

# functions for adding using in mainlist.py

def add_user(the_class):
    input_text = the_class.ids.field.text
    the_class.ids.field.text = ""
    if input_text != "" and control_only_space(input_text):
        try:
            cancel_clock(the_class)
        except:
            pass
        label = MDLabel(text=f"- {input_text}", size_hint_y=None, height=dp(20), halign="left", theme_text_color = "Custom", text_color = (1, 1, 1, 1))
        the_class.ids.grid.add_widget(label)
    else:
        no_text_function(the_class)

def control_only_space(text):
    for character in text:
        if character != " ":
            return True
    return False