from inputs import *
from player.buttons_visual import clicked, unclicked
from player.actions import restart
import player.helper as h

# PlayerScreen using in main.py

Builder.load_file("player/mainplayerfile.kv")

class PlayerScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def action_press(self):
        clicked(self)
    def action_release(self):
        unclicked(self)
        print("goodbey")
    def restart_button(self):
        restart(self)
    def on_touch_move(self, touch):
        # print("hello")
        # if self.ids.buttons_image.source == "app_images/pause_clicked.png":
        #     print("baf")
        button_id = self.ids.button
        if (button_id.x > touch.pos[0] or touch.pos[0] > button_id.right) or \
            (button_id.y > touch.pos[1] or touch.pos[1] > button_id.top):
            if h.current_type == "pause":
                self.ids.buttons_image.source = "app_images/pause.png"
            else:
                self.ids.buttons_image.source = "app_images/play.png"