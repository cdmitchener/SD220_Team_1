# Zork 2 Functions
# Joseph Prater
# 10/05/2022
"""
FUNCTIONS NEEDED FOR 
ZORK 2 TO RUN
 """
from ast import Or
import zork_objects as obj

# introduction statment of what is happening


def intro():
    x = '“Year 2069, 6 years after the Betelgeuse Star went Supernova.  \nIn just seconds, the gamma rays wiped out 80% of life on earth.  \nFew survived the initial flash, and less survived the radiation \nthat pollutes the Earth now.  Radiation is the leading cause of \ndeath for the remaining few.  You are on a mission to travel \nto a hidden underground vault to find a special plant, the Chelsea-Wax Plant, \nto create a cure to suppress and combat the radiation sickness \nof the few remaining people.  You may be humanities final hope at survival.”'
    return x

# instruct player how to plays


def player_instructions(name):
    x = print("Welcome {}. You are on a mission to search for a hidden \nunderground vault the goverment used to store seeds of all the \nplants known. Scientists have determined the rare Chelsea plant \nis needed to stop radiation sickness.  It is up to you to search \nthe baren waistland for this vault.  It will be dangerous \nand you may die.  Travel looking for clues as to where the vault \nis and keep your self safe along the way.  Man kind depends on you!".format(name))
    return x


def view_instructions():
    ans = input('Would you like to view instructions?')
    if ans != 'n':
        print('Instructions: \nTo view inventory, click "i"\nTo view health, click "h"\nTo view armor, click "s"\nTo navigate, type "nw" for northwest, "n" for North, "ne" for North East\nWhen encountering enemies, click "a" to attack and "f" to flee.')
    else:
        pass


def start_game():
    print('You just woke up in your radiation proof bio-pod headquarters.\nYou just traveled from a small community from the south and there is nothing back\nthere for you unless you retriev the special Chelsea-Wax plant.\nYou have the option to travel Northwest (nw), North (n), or NorthEast (ne).')
    x = input('Which direction are you going to travel first?')
    return x

if __name__=="__main__":
    start_game()