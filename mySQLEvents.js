
var xhm1 = new XMLHttpRequest();

window.onload = function() {
	
	fetchData();
	setInterval(fetchData, 1000);

	var updateButton = document.getElementById("serverUpdate");
	var content2 = document.getElementById("updateStatus");
	
	var xhm2 = new XMLHttpRequest();

	updateButton.onclick = function() {
		xhm2.addEventListener("readystatechange",function() {
			content2.innerHTML = this.responseText;

		});
		xhm2.open("GET","updateInputs.php",false);
		xhm2.send();
		fetchData();
	};
};


function fetchData(){
	var content = document.getElementById("serverOut");
	xhm1.addEventListener("readystatechange",function() {
			content.innerHTML = this.responseText;
	});	
	xhm1.open("GET","fetchInputs.php",false);
	xhm1.send();
}
