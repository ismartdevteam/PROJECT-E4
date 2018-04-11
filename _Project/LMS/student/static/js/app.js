function start(){
	el = d3.select("body")
			.append("p")
			.text("Load text with d3.js! today");

	console.log(el)
}

function svgExample(){
	var canvas = d3.select("body")
					.append("svg")
					.attr("width", 700)
					.attr("height", 700)

	var circle = canvas.append("circle")
						.attr("cx", 50)
						.attr("cy", 50)
						.attr("r", 20)
						.attr("fill", "blue")
}