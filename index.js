
// Use unobstrusive styling
(function() {
	"use strict";
	window.onload = init;
	// This function initialze the event.
	function init() {
		document.getElementById("submit").onclick = show_warning;
        document.getElementById("afm").onchange= preview;
	}

	function show_warning() {
		alert("File subbmitted");
	}

    function preview(){
        var source = document.getElementById("afm").files[0];
        console.log(source);

        document.getElementById("afmImage").src = window.URL.createObjectURL(source);
    }


})();