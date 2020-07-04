///////////////////////////////////////////////////////////////////////////
//////////////////// Set up and initiate svg containers ///////////////////
///////////////////////////////////////////////////////////////////////////

var somData = [
	// ALABAMA
	0, .159080, .819875, 1.611198, 3.19792, 3.19384, 2.912393, 2.520810, 3.732268, 4.221746, 4.262535, 7.081112, 4.560301, 7.562431, 10.854169, 10.109755, 13.972550,
	// ALASKA
	.013670, .109358, .820182, 1.066237, 1.202934, .888530, .505779, .246055, .259724, .177706, .205045, .314403, 1.202934, 1.325961, 1.339631, 1.476327, 2.747610,
	// ARIZONA
	.009617, .048085, .637475, 1.497517, 1.950893, 1.670624, 2.108888, 2.581499, 3.155776, 3.749287, 3.628387, 3.363230, 6.855604, 11.692995, 16.732344, 26.909962, 33.515522,
	// ARKANSAS
	.019882, .185565, .904631, 1.153156, 1.534228, 1.570679, 3.244081, 2.173766, 1.358604, 2.322881, 3.618525, 3.578761, 6.252891, 7.922980, 10.312134, 13.698703, 13.297749,
	// CALIFORNIA
	.032648, .120722, .596018, 1.565338, 2.307640, 1.992548, 2.831276, 2.922640, 2.960350, 3.176232, 3.298473, 3.922837, 4.583392, 4.928601, 5.521836, 8.724389, 11.293720,
	// COLORADO
	0.08162, 0.39592, 2.00218, 3.99046, 4.29608, 4.29435, 2.66204, 5.95443, 5.02714, 3.94531, 3.64490, 3.22119, 3.62927, 2.06990, 2.04559, 2.52833, 3.08922,
	// CONNECTICUT
	0.01683, 0.42914, 2.39251, 7.88716, 16.71675, 17.10942, 20.23960, 12.90219, 11.45490, 10.32175, 10.50126, 6.59414, 4.71210, 3.42749, 2.74592, 1.55387, 1.82874,
	// DELAWARE
	0.04108, 0.26701, 1.02694, 2.70086, 8.37985, 8.89333, 12.66221, 14.64421, 12.37466, 13.18595, 11.94335, 8.06150, 5.90492, 3.69699, 4.03589, 4.93960, 7.71234,
	// FLORIDA
	0.01909, 0.18065, 0.95494, 3.03803, 3.64005, 3.03291, 2.93699, 1.88195, 2.39224, 2.04025, 2.54450, 2.14641, 3.21170, 4.13731, 7.84859, 13.07959, 25.64888,
	// GEORGIA
	0.03767, 0.23075, 1.16601, 3.60069, 4.91456, 5.46460, 4.84487, 4.25810, 4.92304, 4.33062, 4.28258, 4.39372, 4.49921, 4.82791, 5.59364, 9.59084, 15.64786,
	// HAWAII
	0.01413, 0.16951, 0.56502, 1.26424, 1.10886, 0.69922, 0.38845, 0.15538, 0.07769, 0.05650, 0.07063, 0, 0.05650, 0.26132, 0.49439, 0.62859, 0.67096,
	// IDAHO
	0, 0.12870, 0.90651, 3.95061, 2.58524, 1.43252, 1.27024, 1.00164, 0.91211, 0.96807, 1.02403, 1.31501, 1.59479, 1.38775, 2.46773, 6.27845, 9.66949,
	// ILLINOIS
	0.02131, 0.30777, 1.66985, 4.06966, 6.88693, 7.34780, 8.83930, 12.61381, 14.16923, 13.46610, 11.63921, 10.37499, 7.04398, 4.61181, 3.29471, 3.67429, 4.29930,
	// INDIANA
	0.01782, 0.09952, 0.84073, 3.55603, 4.91963, 4.73989, 5.19442, 7.12395, 6.93382, 5.27315, 5.76779, 4.65226, 4.49777, 3.93927, 3.99571, 3.29312, 4.05810,
	// IOWA
	0.05071, 0.08875, 0.42788, 1.37873, 2.07919, 2.76064, 5.65122, 10.20897, 12.40543, 8.29142, 7.22646, 8.33579, 6.72251, 6.57672, 6.19955, 7.48953, 9.60993,
	// KANSAS
	0.01716, 0.09954, 0.45996, 1.31809, 1.90161, 1.65447, 3.06867, 6.02750, 6.54238, 4.54465, 3.67623, 2.73915, 2.85929, 2.20368, 2.98286, 4.42451, 6.93368,
	// KENTUCKY
	0.02462, 0.06491, 0.46557, 1.16839, 1.52652, 2.18682, 2.35469, 2.74640, 3.17839, 2.45542, 2.12639, 1.90927, 3.24778, 2.59195, 2.70611, 2.99037, 2.96799,
	// LOUISIANA
	0.04087, 0.80236, 4.11505, 14.72425, 19.64596, 9.14000, 6.89856, 4.86578, 5.70255, 6.10266, 6.48555, 4.94322, 5.93702, 6.25969, 8.95286, 10.28439, 17.52282,
	// MAINE
	0.00744, 0.37940, 0.76625, 1.64409, 1.36883, 1.75568, 1.04894, 1.17541, 1.01175, 1.29444, 2.03093, 2.03093, 1.71104, 1.48042, 1.30188, 1.30932, 1.63665,
	// MARYLAND
	0.01489, 0.15714, 0.78238, 2.89628, 6.37480, 7.60708, 8.19263, 9.93271, 12.62389, 10.79945, 12.61727, 10.21887, 10.17090, 7.17703, 5.01515, 4.21458, 4.37668,
	// MASSACHUSETTS
	0.15234, 0.31919, 3.03083, 9.50163, 14.47225, 19.20928, 20.08269, 23.47768, 16.70801, 12.27566, 11.46463, 6.98005, 5.05041, 3.08741, 1.95720, 1.55096, 1.58723,
	// MICHIGAN
	0.01202, 0.32242, 2.52532, 7.94544, 10.72710, 7.76921, 6.03593, 6.09601, 4.27262, 3.94118, 3.93317, 2.50730, 2.22993, 1.25665, 1.12348, 1.69022, 2.37212,
	// MINNESOTA
	0.01596, 0.14185, 0.45570, 0.70217, 0.88658, 1.18802, 1.82636, 3.89032, 7.49872, 7.21678, 8.44913, 8.41722, 5.89755, 5.39574, 4.18290, 4.34071, 5.47376,
	// MISSISSIPPI
	0.00336, 0.16464, 1.46162, 2.32515, 3.63893, 4.58310, 5.13751, 5.58440, 6.28665, 6.03800, 5.84312, 7.22410, 7.35178, 6.46137, 7.25098, 13.02018, 14.29364,
	// MISSOURI
	0.00326, 0.04236, 0.77231, 2.17029, 2.77804, 2.56133, 1.97151, 2.02202, 2.89861, 1.59024, 1.66682, 2.17192, 2.25502, 2.17192, 2.47335, 4.09455, 4.66319,
	// MONTANA
	0.00936, 0.14035, 0.51461, 1.59060, 1.05728, 0.57075, 0.25262, 0.10292, 0.02807, 0.05614, 0.15906, 0.05614, 0.50525, 0.22456, 0.86080, 1.38476, 2.61981,
	// NEBRASKA
	0.05170, 0.11373, 0.21195, 0.89433, 1.71112, 2.52791, 5.46937, 11.15070, 15.03819, 11.50740, 10.38561, 9.49128, 9.59467, 6.19311, 5.68649, 4.81284, 5.71751,
	// NEVADA
	0.01299, 0.29219, 1.05514, 3.36996, 3.24010, 2.80830, 2.87972, 2.56481, 2.49338, 2.37975, 2.45442, 3.09400, 2.86349, 4.24978, 5.44453, 9.03526, 15.82387,
	// NEW HAMPSHIRE
	0.02942, 0.27947, 0.83841, 2.36080, 2.50053, 2.88297, 3.37572, 3.50074, 5.12609, 3.96408, 4.06704, 3.31688, 3.60371, 2.44905, 1.77244, 1.38265, 1.35323,
	// NEW JERSEY
	0.03040, 0.80273, 6.90595, 21.06913, 28.63821, 27.34686, 27.77693, 21.01171, 16.86859, 10.21032, 9.87144, 7.14126, 5.30838, 3.69954, 2.57932, 2.35190, 2.43183,
	// NEW MEXICO
	0.02861, 0.13830, 0.48168, 1.27335, 2.79470, 2.89962, 3.72944, 4.92172, 5.16017, 4.81680, 4.62126, 4.25404, 4.71665, 4.83587, 3.74852, 4.95510, 6.33337,
	// NEW YORK
	0.15730, 1.96571, 17.01796, 28.33569, 34.72680, 32.04915, 21.16630, 21.03060, 11.87289, 8.00984, 6.89180, 5.28181, 4.31798, 2.96038, 2.50237, 2.39288, 2.33325,
	// NORTH CAROLINA
	0.01335, 0.07818, 0.51392, 1.16418, 1.71051, 1.72958, 2.04327, 2.76600, 2.75360, 2.96527, 4.15042, 4.34016, 6.24900, 7.16527, 8.30180, 8.57640, 10.44900,
	// NORTH DAKOTA
	0.01312, 0.23620, 0.43304, 1.40409, 1.44345, 1.62716, 4.14664, 4.69778, 3.98918, 4.47470, 6.78422, 3.30682, 2.95252, 3.59551, 2.79505, 2.62446, 3.46429,
	// OHIO
	0.00428, 0.09753, 0.63991, 1.74094, 2.23285, 2.33294, 5.05000, 2.68883, 3.29110, 3.13797, 2.88645, 2.95232, 2.57847, 2.12249, 2.44074, 3.63415, 5.39135,
	// OKLAHOMA
	0.00758, 0.10867, 0.51049, 1.59465, 2.03438, 1.70080, 1.66794, 1.51884, 1.79936, 1.59718, 1.81452, 1.49104, 1.60982, 1.81705, 4.36698, 6.55552, 6.54794,
	// OREGON
	0.04979, 0.15174, 0.54057, 1.20918, 1.17362, 0.98394, 0.92704, 0.90807, 1.13568, 1.16176, 0.80138, 0.63778, 0.91992, 1.80903, 2.67679, 2.84987, 4.09224,
	// PENNSYLVANIA
	0.01718, 0.12732, 1.17326, 4.16263, 8.75801, 7.42619, 7.27856, 6.80363, 5.58663, 5.24997, 4.49618, 2.11842, 2.95032, 2.52929, 2.21059, 2.67537, 3.27996,
	// RHODE ISLAND
	0.02832, 0.36815, 1.14220, 4.64431, 10.10043, 19.92711, 22.82508, 22.32478, 18.02030, 14.02732, 14.67866, 8.71280, 7.84435, 5.06909, 3.84194, 3.50211, 2.84134,
	// SOUTH CAROLINA
	0.02331, 0.13401, 0.00583, 2.13257, 2.40448, 2.21220, 1.91504, 2.28795, 2.03352, 2.03352, 2.31126, 2.73661, 4.30593, 6.67351, 9.88985, 14.42885, 20.63622,
	// SOUTH DAKOTA
	0.09043, 0.06782, 0.36172, 1.34515, 3.18767, 9.76647, 7.29094, 5.57277, 5.15453, 10.02646, 5.17714, 6.13796, 5.13192, 4.72498, 5.01888, 4.18240, 4.67977,
	// TENNESSEE
	0.02489, 0.19915, 1.17584, 2.76461, 2.61964, 2.38389, 2.93447, 3.61537, 4.92153, 3.81159, 3.31226, 3.97998, 5.03868, 4.71507, 6.57327, 7.62171, 12.96789,
	// TEXAS
	0.00621, 0.41385, 0.43213, 1.12878, 1.91786, 2.14686, 1.89303, 2.11858, 2.51863, 2.91800, 2.90283, 2.58933, 3.49843, 4.02230, 6.30021, 11.05881, 15.19526,
	// UTAH
	0.01560, 0.22770, 1.01062, 2.09610, 2.81351, 2.20527, 2.89773, 3.30634, 3.28139, 3.19717, 3.50909, 3.26579, 5.90151, 7.60771, 8.06935, 11.02635, 12.15237,
	// VERMONT
	0.03205, 0.32052, 2.17953, 2.88467, 4.64752, 2.24363, 0.91348, 0.65706, 0.80130, 0.25641, 0.28847, 0.38462, 0.83335, 1.34618, 0.40065, 0.89745, 0.57693,
	// VIRGINIA
	0.01992, 0.09021, 0.42880, 1.45978, 2.73680, 3.33547, 4.37935, 5.33418, 6.27613, 6.94978, 6.98141, 8.16002, 7.29540, 5.45368, 4.09348, 4.23524, 4.28211,
	// WASHINGTON
	0.50821, 1.20685, 2.40450, 4.43604, 3.96985, 1.91073, 2.21934, 2.06700, 2.50036, 2.02498, 1.76496, 2.16287, 2.58047, 2.69209, 3.16879, 4.16946, 4.96921,
	// WEST VIRGINIA
	0, 0.02790, 0.39617, 0.78677, 1.70745, 1.20526, 1.35034, 0.80351, 0.90394, 0.82025, 0.88720, 1.74651, 1.03786, 0.66959, 1.04902, 1.45635, 2.18732,
	// WISCONSIN
	0.01202, 0.25247, 0.94806, 1.75700, 1.98371, 1.70032, 2.02149, 3.09493, 4.05501, 3.53804, 4.48266, 5.30534, 5.01165, 3.49338, 3.34911, 4.03783, 6.03012,
	// WYOMING
	0.01728, 0.29373, 0.65658, 1.62416, 1.53777, 0.98487, 0.62202, 1.43410, 1.17493, 0.79480, 1.36499, 1.01942, 0.72569, 1.45138, 1.95245, 2.52264, 3.12738,
];

var MapColumns = 17, // up to July 2nd
	MapRows = 50; // TODO: CHANGE TO 50

	// var margin = {
	// 	top: 140,
	// 	right: 30,
	// 	bottom: 120,
	// 	left: 30
	// };

var margin = {
	top: 100,
	right: 60,
	bottom: 100,
	left: 60
};

//First try for width
var width = Math.max(Math.min(window.innerWidth, 1000), 500) - margin.left - margin.right - 20;
var height = window.innerHeight - margin.top - margin.bottom - 20;

//The maximum radius the hexagons can have to still fit the screen
var hexRadius = d3.min([width/(Math.sqrt(3)*MapColumns), height/(MapRows*1.5)]);
	
//Set the new height and width based on the max possible
var width = MapColumns*hexRadius*Math.sqrt(3);
var height = MapRows*1.5*hexRadius+0.5*hexRadius;

//SVG container
var svg = d3.select('#chart')
	.append("svg")
	.attr("width", width + margin.left + margin.right)
	.attr("height", height + margin.top + margin.bottom)
	.append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//Reset the overall font size
var newFontSize = width * 62.5 / 800;
d3.select("html").style("font-size", newFontSize + "%");
	
//Format to display numbers
var formatPercent = d3.format("%");

//Append a defs (for definition) element to your SVG
//Needed for gradients; the linearGradient element must be nested within this
var defs = svg.append("defs");

///////////////////////////////////////////////////////////////////////////
//////////////// Calculate hexagon centers and put into array /////////////
///////////////////////////////////////////////////////////////////////////	

var SQRT3 = Math.sqrt(3),
    hexWidth = SQRT3 * hexRadius,
    hexHeight = 2 * hexRadius;
var hexagonPoly = [[0,-1],[SQRT3/2,0.5],[0,1],[-SQRT3/2,0.5],[-SQRT3/2,-0.5],[0,-1],[SQRT3/2,-0.5]];
var hexagonPath = "m" + hexagonPoly.map(function(p){ return [p[0]*hexRadius, p[1]*hexRadius].join(','); }).join('l') + "z";

var points = [];
for (var i = 0; i < MapRows; i++) {
	for (var j = 0; j < MapColumns; j++) {
		var a;
		var b = (3 * i) * hexRadius / 2;
		if (i % 2 === 0) {
			a = SQRT3 * j * hexRadius;
		} else {
			a = SQRT3 * (j - 0.5) * hexRadius;
		}//else
		points.push({x: a, y: b});
	}//for j
}//for i

///////////////////////////////////////////////////////////////////////////
//////// Get continuous color scale for the Yellow-Green-Blue fill ////////
///////////////////////////////////////////////////////////////////////////

var coloursYGB = ["#FFFFDD","#AAF191","#80D385","#61B385","#3E9583","#217681","#285285","#1F2D86","#000086"];
var colourRangeYGB = d3.range(0, 1, 1.0 / (coloursYGB.length - 1));
colourRangeYGB.push(1);
		   
//Create color gradient
var colorScaleYGB = d3.scale.linear()
	.domain(colourRangeYGB)
	.range(coloursYGB)
	.interpolate(d3.interpolateHcl);

//Needed to map the values of the dataset to the color scale
var colorInterpolateYGB = d3.scale.linear()
	.domain(d3.extent(somData))
	.range([0,1]);

///////////////////////////////////////////////////////////////////////////
///////////////////// Create the YGB color gradient ///////////////////////
///////////////////////////////////////////////////////////////////////////


//Calculate the gradient
//Append a linearGradient element to the defs and give it a unique id
defs.append("linearGradient")
	.attr("id", "gradient-ygb-colors") // It’s very important that the gradient gets a unique id that can be referenced later when we set the fill of the rectangle.
	// Next we have to define the direction of the gradient. Do we want it to go from left to right (horizontal), top to bottom (vertical) or along an angle? To set this, we use the x1, y1, x2 and y2 attributes in the same manner as an SVG line. These values define a vector, an arrow, from the starting point [x1,y1] to the end point [x2,y2] along which the gradient should run.
	// if we have a rectangle that is 300px wide, then 0% for the x attributes would have the same result as 0px and 100% would be the same using 300px. In most cases, it is easier to work with percentages. A horizontal gradient would thus have x1 at 0%, x2 at 100% and both y1 and y2 the same (so 0% is fine). If we want a vertical gradient from top to bottom, we only have to switch the values of x2 and y2
	.attr("x1", "0%").attr("y1", "0%")
	.attr("x2", "100%").attr("y2", "0%")
	// You need at least two colors to have a gradient. However, there is no upper limit to the number of colors that you can use. For each color along the gradient, you have to append a stop element. And a stop element can have 3 attributes: 1) stop-color: the color you want to have in the gradient. 2) offset: at what location along the directional vector/arrow that you defined with the x and y attributes should the stop-color be its exact color (i.e. the pure color). This is set in percentages along the directional arrow. 3) stop-opacity: the opacity of the stop-color at the offset location. This is very useful if you want a gradient that goes from a color to transparent (the default is 1)
	.selectAll("stop")
	// We can append multiple colors faster by using D3’s data().enter() step and seeing the colors as a dataset. Instead of normally appending circles to a scatterplot with data().enter(), we are now appending stop elements to the linearGradient. Below you can see one way of quickly setting 9 colors along the gradient.
	// .data([
    //     {offset: "0%", color: "#2c7bb6"},
    //     {offset: "12.5%", color: "#00a6ca"},
    //     {offset: "25%", color: "#00ccbc"},
    //     {offset: "37.5%", color: "#90eb9d"},
    //     {offset: "50%", color: "#ffff8c"},
    //     {offset: "62.5%", color: "#f9d057"},
    //     {offset: "75%", color: "#f29e2e"},
    //     {offset: "87.5%", color: "#e76818"},
    //     {offset: "100%", color: "#d7191c"}
    //   ])
    // .enter().append("stop")
    // .attr("offset", function(d) { return d.offset; })
	// .attr("stop-color", function(d) { return d.color; });
	// This can be done even faster and less hard-coded if you want the colors spread out evenly by using a color scale. This is probably something that you’ve defined anyway for the colors of you data visualization elements, such as circles in a scatterplot or hexagons in a heatmap.
	//A color scale
// var colorScale = d3.scale.linear()
// .range(["#2c7bb6", "#00a6ca","#00ccbc","#90eb9d","#ffff8c",
// 		"#f9d057","#f29e2e","#e76818","#d7191c"]);
	.data(coloursYGB)                  
	.enter().append("stop") 
	.attr("offset", (d,i) => { return i/(coloursYGB.length-1); })   
	.attr("stop-color", (d) => { return d; });

///////////////////////////////////////////////////////////////////////////
//////////// Get continuous color scale for the Rainbow ///////////////////
///////////////////////////////////////////////////////////////////////////

var coloursRainbow = ["#2c7bb6", "#00a6ca","#00ccbc","#90eb9d","#ffff8c","#f9d057","#f29e2e","#e76818","#d7191c"];
var colourRangeRainbow = d3.range(0, 1, 1.0 / (coloursRainbow.length - 1));
colourRangeRainbow.push(1);
		   
//Create color gradient
var colorScaleRainbow = d3.scale.linear()
	.domain(colourRangeRainbow)
	.range(coloursRainbow)
	.interpolate(d3.interpolateHcl);

//Needed to map the values of the dataset to the color scale
var colorInterpolateRainbow = d3.scale.linear()
	.domain(d3.extent(somData))
	.range([0,1]);

///////////////////////////////////////////////////////////////////////////
//////////////////// Create the Rainbow color gradient ////////////////////
///////////////////////////////////////////////////////////////////////////

//Calculate the gradient	
defs.append("linearGradient")
	.attr("id", "gradient-rainbow-colors")
	.attr("x1", "0%").attr("y1", "0%")
	.attr("x2", "100%").attr("y2", "0%")
	.selectAll("stop")
	.data([
		    {offset: "0%", color: "#2c7bb6"},
		    {offset: "12.5%", color: "#00a6ca"},
		    {offset: "25%", color: "#00ccbc"},
		    {offset: "37.5%", color: "#90eb9d"},
		    {offset: "50%", color: "#ffff8c"},
		    {offset: "62.5%", color: "#f9d057"},
		    {offset: "75%", color: "#f29e2e"},
		    {offset: "87.5%", color: "#e76818"},
		    {offset: "100%", color: "#d7191c"}
		  ])
		.enter().append("stop")
		.attr("offset", function(d) { return d.offset; })
		.attr("stop-color", function(d) { return d.color; });
	// .data(coloursRainbow)                  
	// .enter().append("stop") 
	// .attr("offset", (d,i) => { return i/(coloursRainbow.length-1); })   
	// .attr("stop-color", (d) => { return d; });

///////////////////////////////////////////////////////////////////////////
//////////////////////////// Draw Heatmap /////////////////////////////////
///////////////////////////////////////////////////////////////////////////

//Append title to the top
svg.append("text")
	.attr("class", "title")
    .attr("x", width/2-10)
    .attr("y", -35)
    .text("New Confirmed Cases of Covid-19");

svg.append("g")
	.selectAll(".hexagon")
	.data(points)
	.enter().append("path")
	.attr("class", "hexagon")
	.attr("d", function (d) { return "M" + d.x + "," + d.y + hexagonPath; })
	.style("stroke", "#fff")
	.style("stroke-width", "1px")
	.style("fill", "white")
	.on("mouseover", mover)
	.on("mouseout", mout);

///////////////////////////////////////////////////////////////////////////
////////////////////////// Draw the legend ////////////////////////////////
///////////////////////////////////////////////////////////////////////////

var legendWidth = width * 0.6,
	legendHeight = 10;

//Color Legend container
var legendsvg = svg.append("g")
	.attr("class", "legendWrapper")
	.attr("transform", "translate(" + (width/2 - 10) + "," + (height+50) + ")");

//Draw the Rectangle
legendsvg.append("rect")
	.attr("class", "legendRect")
	.attr("x", -legendWidth/2)
	.attr("y", 10)
	//.attr("rx", legendHeight/2)
	.attr("width", legendWidth)
	.attr("height", legendHeight)
	.style("fill", "none");
	
//Append title
legendsvg.append("text")
	.attr("class", "legendTitle")
	.attr("x", 0)
	.attr("y", -2)
	.text("Number of Cases");

//Set scale for x-axis
var xScale = d3.scale.linear()
	 .range([0, legendWidth])
	 .domain([0,100]); // TODO: CHANGE THIS TO 10K?
	 //.domain([d3.min(pt.legendSOM.colorData)/100, d3.max(pt.legendSOM.colorData)/100]);

//Define x-axis
var xAxis = d3.svg.axis()
	  .orient("bottom")
	  .ticks(5)  //Set rough # of ticks
	  //.tickFormat(formatPercent)
	  .scale(xScale);

//Set up X axis
legendsvg.append("g")
	.attr("class", "axis")  //Assign "axis" class
	.attr("transform", "translate(" + (-legendWidth/2) + "," + (10 + legendHeight) + ")")
	.call(xAxis);

///////////////////////////////////////////////////////////////////////////
////////////////////////// Mouse Interactions /////////////////////////////
///////////////////////////////////////////////////////////////////////////

//Function to call when you mouseover a node
function mover(d) {
	var el = d3.select(this)
		.transition()
		.duration(10)		  
		.style("fill-opacity", 0.3);
}

//Mouseout function
function mout(d) { 
	var el = d3.select(this)
	   .transition()
	   .duration(1000)
	   .style("fill-opacity", 1);
};

//Transition the colors to a rainbow
function updateRainbow() {
	//Fill the legend rectangle
	svg.select(".legendRect")
		.style("fill", "url(#gradient-rainbow-colors)");
	//Transition the hexagon colors
	svg.selectAll(".hexagon")
		.transition().duration(1000)
		.style("fill", function (d,i) { return colorScaleRainbow(colorInterpolateRainbow(somData[i])); })
}//updateRainbow

//Start set-up
updateRainbow();
var currentFill = "rainbow";