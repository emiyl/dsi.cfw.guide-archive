var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
		var myObj = JSON.parse(this.responseText);
		var countrycode = myObj.geoplugin_countryCode;
		if(countrycode=="DE") {
			document.getElementById("translations").innerHTML = 'A German translation of this guide is available at <a href="http://dsi.de.cfw.guide">dsi.de.cfw.guide</a>.';
			document.getElementById("translations").style.display = "block";
		} else if(countrycode=="ES") {
			document.getElementById("translations").innerHTML = 'A Spanish translation of this guide is available at <a href="http://dsi.es.cfw.guide">dsi.es.cfw.guide</a>.';
			document.getElementById("translations").style.display = "block";
		} else if(countrycode=="IT") {
			document.getElementById("translations").innerHTML = 'An Italian translation of this guide is available at <a href="http://dsi.it.cfw.guide">dsi.it.cfw.guide</a>.';
			document.getElementById("translations").style.display = "block";
		} else if(countrycode=="FR") {
			document.getElementById("translations").innerHTML = 'A French translation of this guide is available at <a href="http://dsi.fr.cfw.guide">dsi.fr.cfw.guide</a>.';
			document.getElementById("translations").style.display = "block";
		}
	}
};
xmlhttp.open("GET", "http://www.geoplugin.net/json.gp", true);
xmlhttp.send();