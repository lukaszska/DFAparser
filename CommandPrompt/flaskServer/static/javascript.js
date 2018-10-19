document.onkeydown = checkKey;

function checkKey(e){
    e = e || window.event;

    if(e.keyCode == '13' && (document.activeElement === document.getElementById("command-input"))){
        console.log("enter key pressed");
        enterCommand();
    }
}

function enterCommand(){
    var text = document.getElementById("command-input").value;
    setConsole(text);
    //runCommand(text);
    document.getElementById("command-input").value = "";
}

function setConsole(text){
    document.getElementById("console").innerHTML = document.getElementById("console").innerHTML + text + "<br>";
    document.getElementById("console").scrollTop = document.getElementById("console").scrollHeight;
}

function getText() {
    return document.getElementById("console").innerHTML;
}

function setImage(){
    document.getElementById("image").src = "static/img/pepehands.png";
    console.log(getText());
}