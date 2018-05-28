var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
		var myObj = JSON.parse(this.responseText);
		document.getElementById("countrycode").innerHTML = myObj.geoplugin_countryCode;
	}
};
xmlhttp.open("GET", "http://www.geoplugin.net/json.gp", true);
xmlhttp.send();