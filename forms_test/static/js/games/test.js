var Canvas = {
	screen: null,
	init: function(canvas, width, height){
		this.screen = document.getElementById(canvas)
		this.screen.height = height;
		this.screen.width = width;
		this.screen.style = "border:1px solid #000000;"
		return this
	},
	contex: function(){
		return this.screen.getContext("2d")
	},
};

var Entity = {
	x: 0,
	y: 0,
	width: 0,
	height: 0,
	color: "#000000",
	init:function(x, y, w, h, color){
		this.x = x;
		this.y = y;
		this.width = w;
		this.height = h;
		this.color = color;
		return this;
	},
	render: function(contex){
		contex.fillStyle=this.color;
		contex.fillRect(this.x,this.y, this.width, this.height);
		contex.stroke(); 
	}
}

var canvas = Canvas.init("screen", 600, 300);


var box = Entity.init(20, 20, 150, 100, "#447755");
box.render(canvas.contex());

document.addEventListener('keydown', function(event) {
	console.log(event)
});