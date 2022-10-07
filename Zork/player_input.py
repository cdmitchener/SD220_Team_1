# import cgi
# import zork_functions as fun
# import zork_objects as obj

# def input(progress):
#     form = cgi.FieldStorage()
#     # assign the player's input to the variable input
#     player_input=form["prompt-input"].value
#     match progress:
#         case 0:
#             # pass the player's name to player_instructions()
#             fun.player_instructions(player_input)
#             # pass the player's name to the class Player
#             obj.Player(player_input)

#     print(player_input)