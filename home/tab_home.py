from inputs import *
from home.video_player import video_end, play_pause_video

# functions for main.py when we enter or leave HomeScreen

def entry_home(our_class):
        our_class.home_screen.my_clock = Clock.schedule_interval(lambda dt: video_end(dt, our_class), 0.1)
def leave_home(our_class):
    our_class.home_screen.my_clock.cancel()
    our_class.home_screen.ids.my_video.state = "play"
    play_pause_video(our_class.home_screen)