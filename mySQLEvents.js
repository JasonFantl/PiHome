var xhm1 = new XMLHttpRequest();

window.onload = function() {
	
	updateTable();
	setInterval(updateTable, 1000);

};

function updateTable(){
	var content = document.getElementById("serverOut");
	var recievedData = fetchData();
	
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
	
	
	var output = "<div class=\"sensor\" id=\"" + name + "\"";
	
	if(read_only == "0") {
		var isOn = (value == "1") ? "on" : "off";
		output += " onclick=\"updateServer(\'" + name + "\')\"";
	}
	
	output += "><p class=\"name\">" + name + "</p>";
						
	if(sensor == "LED") {
		output += "<img class=\"image\" src=\"imgs/bulb1.png\" alt=\"LED\">"
	}
	else if(sensor == "button") {
		output += "<img class=\"image\" src=\"imgs/switch2.png\" alt=\"LED\">"
	}
	
	output += "<p>";
	
	if(value == "1") {
		output += "<mark class=\"on\">ON</mark> <mark class=\"off\">OFF</mark>";
	}
	else if(value == "0") {
		output += "<mark class=\"off\">ON</mark> <mark class=\"on\">OFF</mark>";
	}
	output += "</p></div>";
	
	return output;
}


var updateServer = function(id) {
	var sensorDiv = document.getElementById("updateStatus");
	sensorDiv.innerHTML = "updating " + id;
	$("#updateStatus").show();
	$("#updateStatus").fadeTo(0, 1);
	$("#updateStatus").fadeTo(1000, 0);

	  $.post("updateInputs.php",
	  { name: id },
	  function(data, status){
		 //console.log("Data: " + data + "\nStatus: " + status);
	  });
	  
	updateTable();

};
