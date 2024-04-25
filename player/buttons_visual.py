import player.helper as h
from player.actions import play, pause

# functions using in mainplayer.py

def clicked(the_class):
    if h.current_type == "pause":
        the_class.ids.buttons_image.source = "app_images/pause_clicked.png"
    else:
        the_class.ids.buttons_image.source = "app_images/play_clicked.png"

def unclicked(the_class):
    if h.current_type == "pause":
        h.current_type = "play"
        the_class.ids.buttons_image.source = "app_images/play.png"
        play()
    else:
        h.current_type = "pause"
        the_class.ids.buttons_image.source = "app_images/pause.png"
        pause()