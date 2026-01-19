#########################################################################################
# Title:Bunker budies
# Names(s): Brody, Nixon
# Class: CS 30
# Date:1/16/26
# Version: I don't know we forgot to count
#########################################################################################
"""
Our CS 30 fianl project, a game called bunker budies. This here just starts the game.
"""
#########################################################################################
# Impoorts and global variables ---------------------------------------------------------
import player as p 
import bunker2 as b 

# Functions -----------------------------------------------------------------------------
def game():
    p.playing()#playes house section
    b.bunker_menu()#playes bunker section


if __name__ == "__main__":
    game()