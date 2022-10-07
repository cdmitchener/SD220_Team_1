# Zork 2 main program
# Joseph Prater
# 10/05/2022
"""
THIS IS THE MAIN
PROGRAM FOR ZORK 2
"""
# from js import document
# from pyodide import create_proxy
import player_input as pinput
import zork_functions as fun
import zork_objects as obj

# intro statment
print(fun.intro())

# get input to create player
print("What is your name?")

# let the user know whats going on
fun.player_instructions()

fun.view_instructions()

# Begin the actual game play
fun.start_game()

# pname_proxy = create_proxy()