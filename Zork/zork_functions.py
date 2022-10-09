import zork_objects as obj

# instruct player how to play
def player_instructions(name):
    x = print("Welcome {}. You are on a mission to search for a hidden \nunderground vault the goverment used to store seeds of all the \nplants known. Scientists have determined the rare Chelsea plant \nis needed to stop radiation sickness.  It is up to you to search \nthe barren waistland for this vault.  It will be dangerous \nand you may die.  Travel looking for clues as to where the vault \nis and keep yourself safe along the way.  Mankind depends on you!".format(name))
    return x


def view_instructions():
    # putting pass for now until I can get create_proxy() working
    pass
#     # ans = input('Would you like to view instructions?')
#     if ans != 'n':
#         print('Instructions: \nTo view inventory, click "i"\nTo view health, click "h"\nTo view armor, click "s"\nTo navigate, type "nw" for northwest, "n" for North, "ne" for North East\nWhen encountering enemies, click "a" to attack and "f" to flee.')
#     else:
#         pass


def start_game():
    print('You just woke up in your radiation proof bio-pod headquarters.\nYou just traveled from a small community from the south and there is nothing back\nthere for you unless you retrieve the special Chelsea-Wax plant.\nYou have the option to travel Northwest (nw), North (n), or NorthEast (ne).')
    # commenting out for now until I can get create_proxy() working
    # x = input('Which direction are you going to travel first?')
    # return x

if __name__=="__main__":
    start_game()