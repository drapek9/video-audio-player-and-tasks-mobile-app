# play, restart functions for mainhome.py
# end function for tab_home.py

def play_pause_video(our_class):
    the_state = our_class.ids.my_video.state
    if the_state == "play":
        our_class.ids.my_video.state = "pause"
        our_class.ids.play_button.text = "play"
    else:
        our_class.ids.my_video.state = "play"
        our_class.ids.play_button.text = "pause"
def restart_video(our_class):
    our_class.ids.my_video.seek(0)
    our_class.ids.my_video.state = "play"
    play_pause_video(our_class)
def video_end(dt, our_class):
    if our_class.home_screen.ids.my_video.position >= our_class.home_screen.ids.my_video.duration - 0.3:
        restart_video(our_class.home_screen)
    