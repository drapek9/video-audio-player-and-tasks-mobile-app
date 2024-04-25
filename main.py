from kivymd.app import MDApp
from kivy.lang import Builder
from home.mainhome import *
from home.tab_home import entry_home, leave_home
from list.tab_list import entry_list, leave_list
from player.tab_player import entry_player, leave_player
from list.mainlist import *
from player.mainplayer import *

class MyApp(MDApp):
    title = "NOMSI"
    def build(self):
        self.kvfile = Builder.load_file("mainfile.kv")
        self.home_screen = HomeScreen()
        self.list_screen = ListScreen()
        self.player_screen = PlayerScreen()
        self.kvfile.ids.home_id.add_widget(self.home_screen)
        self.kvfile.ids.list_id.add_widget(self.list_screen)
        self.kvfile.ids.player_id.add_widget(self.player_screen)
        return self.kvfile
    def enter_tab(self, the_tab):
        if the_tab == "home":
            entry_home(self)
        elif the_tab == "list":
            entry_list(self)
        elif the_tab == "player":
            entry_player(self)
    def leave_tab(self, the_tab):
        if the_tab == "home":
            leave_home(self)
        elif the_tab == "list":
            leave_list(self)
        elif the_tab == "player":
            leave_player(self)
if __name__ == "__main__":
    MyApp().run()