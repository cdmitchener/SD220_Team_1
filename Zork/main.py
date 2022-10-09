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
# pname = input("What is your name? ")
# player = obj.Player(pname)
def create_player():
    try:
        print("What is your name?")

        # player = obj.Player(pname)

    except EOFError:
        return

# create_player()

pyscript.write("output", create_player())

def input():
    form = cgi.FieldStorage()
    # assign the player's input to the variable input
    # player_input=form["prompt-input"].value
    player_input= "Test"
    progress = 0
    match progress:
        case 0:
            # pass the player's name to player_instructions()
            fun.player_instructions(player_input)
            # pass the player's name to the class Player
            obj.Player(player_input)

    print(player_input)

# -----------------------------------------------------------------------------------------
# chels: If I can get create_proxy() to work and my logic between the py-script tags is
#        at least on the right track, then we shouldn't need the code that's commented out.
# -----------------------------------------------------------------------------------------
# let the user know whats going on
# fun.player_instructions(pname)

# fun.view_instructions()

# Begin the actual game play
# fun.start_game()

# pname_proxy = create_proxy()