# Zork 2 main program
# Joseph Prater, Chelsea Mitchener
# 10/07/2022
"""
THIS IS THE MAIN
PROGRAM FOR ZORK 2
"""
# from js import document
# from pyodide import create_proxy

# import player_input as pinput
import zork_functions as fun
import zork_objects as obj

# intro statment
print(fun.intro())

# get input to create player
def create_player():
    try:
        progress = 0
        print("What is your name?")
        input(progress)

    except EOFError:
        return

create_player()

# -----------------------------------------------------------------------------------------
# chels: If I can get create_proxy() to work and my logic in player_input.py is right or
#        at least on the right track, then we shouldn't need the code that's commented out.
# -----------------------------------------------------------------------------------------
# let the user know whats going on
# fun.player_instructions()

fun.view_instructions()

# Begin the actual game play
fun.start_game()

# pname_proxy = create_proxy()