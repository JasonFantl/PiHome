var xhm1 = new XMLHttpRequest();

window.onload = function() {
	
	updateTable();
	setInterval(updateTable, 1000);

	var updateButton = document.getElementById("serverUpdate");
	var content2 = document.getElementById("updateStatus");
	
	var xhm2 = new XMLHttpRequest();

	updateButton.onclick = function() {
		xhm2.addEventListener("readystatechange",function() {
			content2.innerHTML = this.responseText;
		});
		xhm2.open("GET","updateInputs.php",false);
		xhm2.send();
		updateTable();
	};
};

function updateTable(){
	var content = document.getElementById("serverOut");
	var recievedData = fetchData();
	//content.innerHTML = recievedData;
	
	var mySQLArray = JSON.parse(recievedData);
	
	var outputHTML = "";
	for(i = 0; i < mySQLArray.length; i++) {
		outputHTML += createHTML(mySQLArray[i]);
	}
	
	content.innerHTML = outputHTML;
}

function fetchData(){
	var returnVal;
	xhm1.addEventListener("readystatechange",function() {
			returnVal = this.responseText;
	});	
	xhm1.open("GET","fetchInputs.php",false);
	xhm1.send();
	
	return returnVal;
}

function createHTML(inObj) {
	var name = inObj.name;
	var value = inObj.value;
	var sensor = inObj.sensor;
	var read_only = inObj.read_only;
	
	
	var output =	"<div class=\"sensor\">" +
						"<p class=\"name\">" + name + "</p>";
						
	if(sensor == "LED") {
		output += "<img class=\"image\" src=\"imgs/bulb1.png\" alt=\"LED\">"
	}
	
	output += "<p>";
	
	if(value == "1") {
		output += "<mark class=\"on\">ON</mark> <mark class=\"off\">OFF</mark>";
	}
	else if(value == "0") {
		output += "<mark class=\"off\">ON</mark> <mark class=\"on\">OFF</mark>";
	}
	output += "</p>";
	
	if(read_only == "0") {
		var isOn = (value == "1") ? "on" : "off";
		output += "<input id=\"switchUpdate\" type=\"button\" class=\"button\" value=\"switch " + isOn + "\">";
	}
	
	output += "</div>";
	
	
	return output;
}
