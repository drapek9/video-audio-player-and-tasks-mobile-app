from inputs import *
import player.helper as h

# functions using in button_visual.py

music = SoundLoader.load(h.song_address)
h.music_length = music.length
def play():
    music.seek(h.music_pos)
    music.play()
def pause():
    h.music_pos = music.get_pos()
    music.stop()
def restart(the_class):
    h.music_pos = 0
    music.stop()
    h.current_type = "pause"
    the_class.ids.buttons_image.source = "app_images/pause.png"