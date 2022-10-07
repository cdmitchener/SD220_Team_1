import cgi
import zork_functions as fun
import zork_objects as obj

def input():
    form = cgi.FieldStorage()
    # assign the player's name to the variable input
    input=form["input"].value
    # pass the player's name to player_instructions()
    fun.player_instructions(input)
    # pass the player's name to the class Player
    obj.Player(input)