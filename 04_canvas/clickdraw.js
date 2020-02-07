var mode = "Square";
var canv = document.getElementById("slate");
var toggle = document.getElementById("but");
var refresh = document.getElementById("refresh");
var ctx = canvas.getContext("2d");


var draw = function (e, state){
	var rect = canv.getBoundingClientRect();
	var x = e.clientX - rect.left; // offsets the xy
	var y = e.clientY - rect.top;
	if (e.buttons > 0){             // if the mouse button is down
		if (state === "Dot"){
	                ctx.beginPath();
	                ctx.arc(x, y, 5, 5, 2 * Math.PI);
	                ctx.stroke();
	        }
	        else {
	                ctx.beginPath();
	                ctx.rect(x, y, 20, 20);
			ctx.stroke();
		}
	}
};

var swap = function(e){
	if (mode === "Dot"){
		mode = "Square";
		status.innerHTML = "Swap to Dot?";
	}

	else{
		mode = "Dot";
		status.innerHTML = "Swap to Square? ";

	}

};

refresh.addEventListener("click", function(){ctx.clearRect(0, 0, 600, 600);});
toggle.addEventListener("click", swap);
canv.addEventListener("mousemove", function(e, state){draw(e, mode)});
