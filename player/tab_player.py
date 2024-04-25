from player.buttons_visual import unclicked
import player.helper as h

# functions when we enter or leave PlayerScreen

def entry_player(my_class): # nothing yet
    pass
def leave_player(my_class):
    h.current_type = "play"
    unclicked(my_class.player_screen)