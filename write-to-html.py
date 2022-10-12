# import webbrowser

f = open('game.html','w')

message = """<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  <link rel="stylesheet" href="styles.css" />
  <link rel="stylesheet" href="crt_effect.css" />
  <script defer src="https://pyscript.net/latest/pyscript.js"></script>
  <py-env>
    - paths:
        - /Zork/zork_objects.py
        - /Zork/main.py
  </py-env>
  </head>
  <body>
    <py-config>
      lang = "python"
    </py-config>
    <section class="contain">
    <div class="topbtn"><img src="oni.png" height="200px" width ="200px">
    </div>
    <div class="game">
      <h2 id="important">&gt;&nbsp; loading...</h2>
      <p id="message"></p>
      <p id="horizontal-div" style="text-align:center;"></p>
      <p id="prompt"></p>
      <h3 id="test"></h3>
      <h2 id="progress"></h2>
      <p id="notify" style="text-align:center;"></p>
          <div class="overlay">
        <py-script src = "/Zork/main.py">
        </py-script>
                </div>
        <div class="container">
          <iframe name="dummyframe" id="dummyframe" style="display: none;"></iframe>
          <form name=input action=/Zork/main.py method="post" autocomplete="off" target="dummyframe">
              <input type="text" id="prompt-input" name="prompt-input">
              <div class="confirm-contain">
              <input type="button" id="confirm-btn" class="confirm" value="Confirm"><span id="post"></span>
              </div>
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