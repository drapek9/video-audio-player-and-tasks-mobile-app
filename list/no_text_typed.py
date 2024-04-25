from inputs import *
import list.helper as h

# functions using in adding_users.py

def no_text_function(the_class):
    the_class.ids.error_label.text = "Enter a text!"
    h.current_clock = Clock.schedule_interval(lambda dt: clock_func(dt, the_class), 2)

def clock_func(dt, the_class):
    cancel_clock(the_class)

def cancel_clock(the_class):
    h.current_clock.cancel()
    the_class.ids.error_label.text = ""
    h.current_clock = None