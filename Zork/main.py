# Zork 2 main program
# Joseph Prater
# 10/05/2022
"""
THIS IS THE MAIN
PROGRAM FOR ZORK 2
"""
import zork_functions as fun
import zork_objects as obj

# intro statment
print(fun.intro())

# get input to create player
pname = input("What is your name? ")
player = obj.Player(pname)

# let the user know whats going on
fun.player_instructions(pname)

fun.view_instructions()

# Begin the actual game play
fun.start_game()
