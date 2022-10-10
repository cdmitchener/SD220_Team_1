
# from js import document
# from pyodide import create_proxy

import zork_functions as fun
import zork_objects as obj
from js import document
# supress FutureWarning of deprecated feature from pyodide
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from pyodide import create_proxy

progress = 0

def add_one():
    global progress
    progress = document.getElementById("progress")
    int_progress = int(progress)
    int_progress += 1
    Element("progress").write(int_progress)

    Element("test").write("Step 1")
    game_progress(int_progress)

def begin(e):
    pass

# def view_instructions(e):
#     inp = Element('prompt-input').element
#     text = inp.value
#     inp.value = ""
#     if text != "" and text != "n":
#         pyscript.write("message", f"Instructions: To view inventory, enter 'i' To view health, enter To view armor, enter To navigate, enter for northwest,for North, and for North East When encountering enemies, enter  to attack and  to flee.")

#         pyscript.write("prompt", "Press 'Enter' to proceed...")

    # input_proxy = create_proxy(begin)
    # confirm_button = document.getElementById("confirm-btn")
    # confirm_button.addEventListener("click", input_proxy)

def create_player(e):
    global name
    inp = Element('prompt-input').element
    text = inp.value
    inp.value = ""
    Element("test").write("Step 4")
    Element("message").write(f"Welcome, {text}. You are on a mission to search for a hidden underground vault the goverment used to store seeds of all the plants known. Scientists have determined the rare Chelsea plant is needed to stop radiation sickness. It is up to you to search the barren waistland for this vault. It will be dangerous and you may die. Travel looking for clues as to where the vault is and keep yourself safe along the way. Mankind depends on you!")

    obj.Player(text)

    Element("test").write("Step 4.1")
    Element("prompt").write("Would you like to view the instructions on how to play?")

    Element("test").write("Step 5")
    
    instructions_proxy = create_proxy(game_progress)
    confirm_button = document.getElementById("confirm-btn")
    confirm_button.addEventListener("click", add_one)
    confirm_button.addEventListener("click", instructions_proxy)

def start_game():
    Element("test").write("Step 1")
    game_progress(progress)

def game_progress(progress):
    print(progress)
    Element("test").write("Step 2")
    if progress == 0:
        Element("test").write("Step 3")
        # intro statment
        Element("message").write('\"Year 2069, 6 years after the Betelgeuse Star went Supernova. In just seconds, the gamma rays wiped out 80% of life on earth. Few survived the initial flash, and less survived the radiation that pollutes the Earth now. Radiation is the leading cause of death for the remaining few. You are on a mission to travel to a hidden underground vault to find a special plant, the Chelsea-Wax Plant, to create a cure to suppress and combat the radiation sickness of the few remaining people. You may be humanity\'s final hope at survival.\"')

        Element("prompt").write("What is your name?")

        name_proxy = create_proxy(create_player)
        confirm_button = document.getElementById("confirm-btn")
        confirm_button.addEventListener("click", add_one)
        confirm_button.addEventListener("click", name_proxy)
        
    elif progress == 1:
        print("Step 6")
        inp = Element('prompt-input').element
        text = inp.value
        inp.value = ""
        if text != "" and text != "n":
            Element("message").write(f"Instructions: To view inventory, enter 'i' To view health, enter To view armor, enter To navigate, enter for northwest,for North, and for North East When encountering enemies, enter  to attack and  to flee.")

            Element("prompt").write("Press 'Enter' to proceed...")

        begin_proxy = create_proxy(begin)
        confirm_button = document.getElementById("confirm-btn")
        confirm_button.addEventListener("click", add_one)
        confirm_button.addEventListener("click", begin_proxy)

    else:
        pass

if __name__ == "__main__":
    start_game()

# let the user know whats going on
# fun.player_instructions(pname)

# fun.view_instructions()

# Begin the actual game play
# fun.start_game()

# pname_proxy = create_proxy()