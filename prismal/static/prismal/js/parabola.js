/**
 * @class Parabola
 */
function Parabola() {
	this.a = 1;
	this.b = 1;
	this.c = 0;

	this.valueAt = function(x) {
		return (this.a * Math.pow(x, 2)) + (this.b * x) + this.c;
	};

}

Parabola.prototype = {
	solveWithPoints : function(x1, y1, x2, y2, x3, y3) {

		var denom = (x1 - x2) * (x1 - x3) * (x2 - x3);
		this.a = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom;
		this.b = (Math.pow(x3, 2) * (y1 - y2) + Math.pow(x2, 2) * (y3 - y1) + Math
				.pow(x1, 2)
				* (y2 - y3))
				/ denom;
		this.c = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2
				* (x1 - x2) * y3)
				/ denom;
	},
	// valueAt : function(x) {
	// return (this.a * Math.pow(x, 2)) + (this.b * x) + this.c;
	// },

	solveWithY : function(start, peak, end) {
		this.solveWithPoints(0, start, 0.5, peak, 1, end);
	}

};
