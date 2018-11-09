document.getElementById("command-input").onkeydown = checkKey;

function checkKey(e){
    e = e || window.event;

    if(e.keyCode == '13' && (document.activeElement === document.getElementById("command-input"))){
        //console.log("enter key pressed");
        enterCommand();
    }
}

function enterCommand(){
    var text = document.getElementById("command-input").value;
    setConsole(text);
    submitCode(text);
    //runCommand(text);
    document.getElementById("command-input").value = "";
}

function setConsole(text){
    document.getElementById("console").innerHTML = document.getElementById("console").innerHTML + text + "<br>";
    document.getElementById("console").scrollTop = document.getElementById("console").scrollHeight;
    readInput(text);
}

function getText() {
    return document.getElementById("console").innerHTML;
}

function setImage(){
    document.getElementById("image").src = "pepehands.png";
    //console.log(getText());
}

function submitCode(command){
    var response = "";
    $.post("index", {script: command}, function(req){
        console.log("Call success");
        console.log("Type: " + typeof req);
        console.log("Request: " + req);
        setConsole(req);
        window.alert(req);
        response = req;
        //window.alert(response);
    });
    return response;
}

function readInput(text) {
    if (text === "left to right") {
        leftToRight();
    } else if (text === "right to left") {
        rightToLeft();
    } else if (text === "left to left") {
        leftToLeft();
    } else if (text === "right to right") {
        rightToRight();
    }
}