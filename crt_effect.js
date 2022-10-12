// VARS
let echo = true;
let commands = new Map();

document.body.onload = function () {
  // INIT vars
  let message = document.getElementById("message");
  let prompt = document.getElementById("prompt");
  let pre = document.getElementById("pre");
  let carat = document.getElementById("carat");
  let post = document.getElementById("post");

  prompt.innerHTML = "User>";
  carat.innerHTML = " ";
  document.addEventListener("keydown", handleKeypress);
  var intro = document.createElement("span");
  intro.innerHTML =
    'Welcome to my "Terminal Emulator."\nActually it\'s just a web dev exercise\nand a bit of fun. :)\ntype "help" for commands\n';
  document.getElementById("message").appendChild(intro);
};

function message(text) {
  document.getElementById("message");
}
