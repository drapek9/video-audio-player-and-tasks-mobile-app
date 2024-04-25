from inputs import *
from list.adding_users import add_user

# Screen for main.py

Builder.load_file("list/mainlistfile.kv")

class ListScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def add(self):
        add_user(self)
    