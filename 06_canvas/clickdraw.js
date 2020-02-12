var curr_state = "circle"


const canvas = document.getElementById("playground");
const status = document.getElementById("status");
const clear = document.getElementById("clear");
const ctx = canvas.getContext("2d");
var lastx;
var lasty;

canvas.addEventListener('mousedown', e => {
  var x = e.offsetX;
  var y = e.offsetY;
  ctx.beginPath();
  ctx.arc(x, y, 10, 0, 2 * Math.PI);
  ctx.fill();
  ctx.closePath();
  if(lastx!=null){
    ctx.beginPath();
    ctx.moveTo(lastx,lasty);
    ctx.lineTo(e.offsetX,e.offsetY);
    ctx.closePath();
    ctx.stroke();
  }
  lastx=e.offsetX;
  lasty=e.offsetY;
});

var toggle = function(e){
	if (curr_state === "circle"){
		curr_state = "rect";
		status.innerHTML = "rectangle";
	}

	else{
		curr_state = "circle";
		status.innerHTML = "circle";

	}


};

var clearcanvas = function(canvas, contex){
	context.clearRect(0, 0, canvas.width, canvas.height);
};

var draw = function (e, state){
	var rect = canvas.getBoundingClientRect();
	const x = e.clientX - rect.left; // offsets the xy
	const y = e.clientY - rect.top;
	if (e.buttons > 0){             // if the mouse button is down
		if (state === "circle"){
	                ctx.beginPath();
	                ctx.arc(x, y, 5, 0, 2 * Math.PI);
	                ctx.stroke();
	        }
	        else {
	                ctx.beginPath();
	                ctx.rect(x, y, 8, 8);
			ctx.stroke();
		}
	}
};


// adding all the listeners
clear.addEventListener("click", function(){ctx.clearRect(0, 0, canvas.width, canvas.height);});
canvas.addEventListener("mousemove", function(e, state){draw(e, curr_state)});
