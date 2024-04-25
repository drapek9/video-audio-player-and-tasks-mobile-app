from inputs import *
from home.change_color import change_color_def
from home.video_player import play_pause_video, restart_video, video_end

# Screen for main.py

Builder.load_file("home/mainhomefile.kv")
class HomeScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def ch_c(self): # i want to change color
        change_color_def(self)
    def v_f(self): # i want to play or pause video
        play_pause_video(self)
    def v_r(self): # i want to restart video and stop it
        restart_video(self)