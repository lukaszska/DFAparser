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
    document.getElementById("command-input").value = "";
}

function setConsole(text){
    document.getElementById("console").innerHTML = document.getElementById("console").innerHTML + text + "<br>";
    document.getElementById("console").scrollTop = document.getElementById("console").scrollHeight;
}

function getText() {
    return document.getElementById("console").innerHTML;
}

function submitCode(command){
    $.post("index", {script: command}, function(req){
        console.log("Call success");
        console.log("Type: " + typeof req);
        console.log("Request: " + req);
        parseJson(req);
    });
}

function parseJson(json) {
    console.log(json);
    console.log(typeof json);
    json = JSON.parse(json);
    console.log(typeof json);
    console.log(json.graph);
    // if (json.result !== null) {
    //     window.alert('Result is: ' + json.result)
    // }
    createDFA(json.graph, json.transitions, json.result, json.start);
}

var height = $('#image').height();
var width = $('#image').width();

var centerX = width/2;
var centerY = height/2;
var radius = height/3;

var svgContainer = d3.select("svg");
var circle = svgContainer.selectAll("circle").data([1, 2, 3, 4]);

var arrayOfCircles = new Array();

function createCircle(x, y, r, c) {
    var newCircle = circle.enter().append("circle")
    .attr("cx", x)
    .attr("cy", y)
    .attr("fill", "white")
    .attr("stroke-width", 2)
    .attr("r", r)
    .attr("stroke", c);

    arrayOfCircles.push(newCircle);
}

function drawLine(xOne, yOne, xTwo, yTwo, radius) {
    svgContainer.append("line")
    .attr("x1", xOne)
    .attr("x2", xTwo)
    .attr("y1", yOne)
    .attr("y2", yTwo)
    .attr("stroke-width", 2)
    .attr("stroke", "black");
}

function drawText(x, y, text) {
    svgContainer.append("text")
    .attr("dx", x - 4)
    .attr("dy", y + 4)
    .text(text);
}

function linkArc(sourceX, sourceY, targetX, targetY, r) {
    var theta = Math.atan((targetX - sourceX) / (targetY - sourceY));
    var phi = Math.atan((targetY - sourceY) / (targetX - sourceX));

    var sinTheta = r * Math.sin(theta);
    var cosTheta = r * Math.cos(theta);
    var sinPhi = r * Math.sin(phi);
    var cosPhi = r * Math.cos(phi);

    // Set the position of the link's end point at the source node
    // such that it is on the edge closest to the target node
    if (targetY > sourceY) {
        sourceX = sourceX + sinTheta;
        sourceY = sourceY + cosTheta;
    }
    else {
        sourceX = sourceX - sinTheta;
        sourceY = sourceY - cosTheta;
    }

    // Set the position of the link's end point at the target node
    // such that it is on the edge closest to the source node
    if (sourceX > targetX) {
        targetX = targetX + cosPhi;
        targetY = targetY + sinPhi;    
    }
    else {
        targetX = targetX - cosPhi;
        targetY = targetY - sinPhi;   
    }

    // Draw an arc between the two calculated points
    var dx = targetX - sourceX,
        dy = targetY - sourceY,
        dr = Math.sqrt(dx * dx + dy * dy);
    
    drawLine(sourceX, sourceY, targetX, targetY);
    drawArrowhead(sourceX, sourceY, targetX, targetY, r / 2);
}

function drawArrowhead(x1, y1, x2, y2, r) {
    var x, y;
    var angle = Math.abs(Math.atan(y1-y2, x2-x1) * (180 / Math.PI));

    if (Math.abs(y1-y2) > Math.abs(x2-x1)) {
        if (x2 > x1) {
            x = x2 + r * Math.abs(Math.cos((135 - angle) * (Math.PI / 180)));
        } else {
            x = x2 - r * Math.abs(Math.cos((135 - angle) * (Math.PI / 180)));
        }

        if (y2 > y1) {
            y = y2 - r * Math.abs(Math.sin((135 - angle)  * (Math.PI / 180)));
        } else {
            y = y2 + r * Math.abs(Math.sin((135 - angle)  * (Math.PI / 180)));
        }
    } else {
        if (x2 > x1) {
            x = x2 + r * Math.abs(Math.cos((180 - angle) * (Math.PI / 180)));
        } else {
            x = x2 - r * Math.abs(Math.cos((180 - angle) * (Math.PI / 180)));
        }

        if (y2 > y1) {
            y = y2 - r * Math.abs(Math.sin((180 - angle) * (Math.PI / 180)));
        } else {
            y = y2 + r * Math.abs(Math.sin((180 - angle) * (Math.PI / 180)));
        }
    }
    if (parseInt(y2, 10) != parseInt(y1, 10)) {
        drawLine(x, y, x2, y2);
    }

    if (Math.abs(y1-y2) > Math.abs(x2-x1)) {
        if (x2 > x1) {
            x = x2 - r * Math.abs(Math.cos((90 + angle) * (Math.PI / 180)));
        } else {
            x = x2 + r * Math.abs(Math.cos((90 + angle) * (Math.PI / 180)));
        }

        if (y2 > y1) {
            y = y2 - r * Math.abs(Math.sin((90 + angle)  * (Math.PI / 180)));
        } else {
            y = y2 + r * Math.abs(Math.sin((90 + angle)  * (Math.PI / 180)));
        }
    } else {
        if (x2 > x1) {
            x = x2 - r * Math.abs(Math.cos((angle + 45) * (Math.PI / 180)));
        } else {
            x = x2 + r * Math.abs(Math.cos((angle + 45) * (Math.PI / 180)));
        }

        if (y2 > y1) {
            y = y2 + r * Math.abs(Math.sin((angle + 45)  * (Math.PI / 180)));
        } else {
            y = y2 - r * Math.abs(Math.sin((angle + 45)  * (Math.PI / 180)));
        }
    }

    drawLine(x, y, x2, y2);
}

/*Create a DFA of 3 circles. Draw lines connecting them.
First should be named first, second, second, etc.*/

function createDFA(nodes, connections, answer, start) {
    svgContainer.selectAll("*").remove();
    var numCircles = nodes.length;
    if (numCircles == 1) {
        createCircle(centerX, centerY, height / (numCircles * 3), "black");
        drawText(centerX - nodes[0].length * 3.5, centerY, nodes[0]);
        return;
    }
    var angle = 0;
    var centers = new Array();
    for (i = 1; i <= numCircles; i++) {
        centers.push([centerX - radius * Math.cos(angle), centerY - radius * Math.sin(angle), nodes[i - 1]]);
        angle += (Math.PI * 2) / numCircles;
    }

    angle = 0;

    for (i = 1; i <= numCircles; i++) {
        if (centers[i - 1][2] === answer) {
            createCircle(centerX - radius * Math.cos(angle), centerY - radius * Math.sin(angle), height / (numCircles * 2), "red");
        } else if (centers[i - 1][2] === start) {
            createCircle(centerX - radius * Math.cos(angle), centerY - radius * Math.sin(angle), height / (numCircles * 2), "blue");
        } else {
            createCircle(centerX - radius * Math.cos(angle), centerY - radius * Math.sin(angle), height / (numCircles * 2), "black");
        }
        angle += (Math.PI * 2) / numCircles;

        drawText(centers[i - 1][0] - centers[i - 1][2].length * 3.5, centers[i - 1][1], centers[i - 1][2]);
    }

    for (i = 0; i < connections.length; i++) {
        var circle1 = connections[i][0];
        var circle2 = connections[i][1];
        var x1, y1, x2, y2;

        for (j = 0; j < centers.length; j++) {
            if (centers[j][2] === circle1) {
                x1 = centers[j][0];
                y1 = centers[j][1];
            } else if (centers[j][2] === circle2) {
                x2 = centers[j][0];
                y2 = centers[j][1];
            }
        }

        if (circle1 !== circle2) {
            linkArc(x1, y1, x2, y2, height / (numCircles * 2));
        }
    }
}

//createDFA(["LUL", "monkaS", "BabyRage", "Jebaited", "OMEGALUL"], [["BabyRage", "monkaS"], ["Jebaited", "BabyRage"], ["LUL", "OMEGALUL"]]);
//createDFA(["Give Up", "Runtime Error", "Clean Compile", "Project Done", "Write Code"], [["Write Code", "Clean Compile"], ["Clean Compile", "Runtime Error"], ["Runtime Error", "Give Up"], ["Give Up", "Write Code"]]);
//createDFA(["LOL"], []);

setConsole("<b>WELCOME TO FINITE STATE MACHINE GENERATOR!!!</b>");
setConsole("\n<b>Commands:</b>");
setConsole("add node [node_name]");
setConsole("add alphabet [letter]");
setConsole("add transition [node1] to [node2] if [input_from_alphabet]");
setConsole("start at node [starting_node]");
setConsole("kill node [node_name]");
setConsole("kill alphabet [letter]");
setConsole("kill transition [transition]\n");