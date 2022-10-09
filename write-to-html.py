# import webbrowser

f = open('game.html','w')

message = """<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  <link rel="stylesheet" href="styles.css" />
  <script defer src="https://pyscript.net/latest/pyscript.js"></script>
  <script src="https://cdn.jsdelivr.net/pyodide/v0.21.3/full/pyodide.js"></script>
  <py-env>
    - paths:
        - /Zork/zork_functions.py
        - /Zork/zork_objects.py
        - /Zork/main.py
  </py-env>
  </head>
  <body>
    <section class="contain">
    <div class="topbtn"><img src="oni.png" height="200px" width ="200px">
    </div>
    <div class="game">
      <p id="output"></p>
        <py-script src = "/Zork/main.py">
          # pyscript.write("output", create_player())

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
        </py-script>
        <div class="container">
          <iframe name="dummyframe" id="dummyframe" style="display: none;"></iframe>
          <form name=input action=/Zork/main.py method="post" target="dummyframe">
              <input type="text" id="prompt-input" name="prompt-input">
              <input type="submit" value="Confirm">
          </form>
        </div>
    </div>
    <div>
      <button class="btn-blue">PLAY</button>
      <button class="btn-green">SAVE</button>
      <button class="btn-red">EXIT</button>
    </div>
    </section>
    <script>
    var input = document.getElementById("prompt-input");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("confirm-btn").click();
        }
    })
    </script>
  </body>
</html>"""

f.write(message)
f.close()

# webbrowser.open_new_tab('game.html')