import zork_objects as obj
from js import document
# supress FutureWarning of deprecated feature from pyodide
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from pyodide import create_proxy

progress = 0

def game_progress(e):
    global progress
    global text

    inp = Element('prompt-input').element
    text = inp.value
    progress += 1
    # Element("test").write(f"{progress}")
    inp.value = ""

    if progress == 1:
        Element("important").write("")

        # intro statment
        Element("message").write('\"Year 2069, 6 years after the Betelgeuse Star went Supernova. In just seconds, the gamma rays wiped out 80% of life on earth. Few survived the initial flash, and less survived the radiation that pollutes the Earth now. Radiation is the leading cause of death for the remaining few. You are on a mission to travel to a hidden underground vault to find a special plant, the Chelsea-Wax Plant, to create a cure to suppress and combat the radiation sickness of the few remaining people. You may be humanity\'s final hope at survival.\"')

        Element("prompt").write("&gt;&nbsp&gt;&nbsp; What is your name?")

    elif progress == 2:
        Element("message").write(f"Welcome, {text}. You are on a mission to search for a hidden underground vault the goverment used to store seeds of all the plants known. Scientists have determined the rare Chelsea plant is needed to stop radiation sickness. It is up to you to search the barren wasteland for this vault. It will be dangerous and you may die. Travel looking for clues as to where the vault is and keep yourself safe along the way. Mankind depends on you!")

        Element("prompt").write("&gt;&nbsp;&gt;&nbsp; Would you like to view the instructions on how to play?")

        return obj.Player(text)

    elif progress == 3:
        if text != "" and text != "n":
            Element("important").write("INSTRUCTIONS:<br>")
            Element("message").write("' i ' . . .  Check inventory<br>' h ' . . .  Health<br>' c ' . . .  Armor<br>' nw ' . . .  Go North West<br>' n ' . . .  Go North<br>' ne ' . . .  Go North East<br><br><b>When encountering enemies:</b><br>' a ' . . .  Attack<br>' f ' . . .  Flee")
            # Element("message").write("Inventory... 'i'<br>Health... 'h'<br>Armor... 'c'<br>Go North West... 'nw'<br>Go North... 'n'<br>Go North East... 'ne'<br><br>When encountering enemies:<br>Attack... 'a'<br>Flee... 'f'")

            Element("prompt").write("<h3 align='center'>&gt;&nbsp; Press 'Enter' to proceed &nbsp;&lt;</h3>")

    else:
        pass

    proxy = create_proxy(game_progress)
    confirm_button = document.getElementById("confirm-btn")
    confirm_button.addEventListener("click", proxy)

if __name__ == "__main__":
    game_progress(progress)