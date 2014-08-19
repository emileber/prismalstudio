/**
 * specific js script for app Prismal.
 */

function PrismalSeat(tagId) {
	this.tagId = tagId;
	this.sizeCurve = new Parabola();
	this.yCurve = new Parabola();
	
	
	this.sizeCurve.solveWithY(1, 0.2, 0.8);
	this.yCurve.solveWithY(1, 0.5, 0.8);
};

PrismalSeat.prototype = {
	update : function(event) {

		var xMouseRatio = event.pageX / $(window).width();

		// console.log(parabola.valueAt(xMouseRatio));

		// entre 50 et 100%
		var x = xMouseRatio;
		// var sizeRatio = (2 * (Math.pow(x, 2))) -(2*x) + 1;
		var sizeRatio = this.sizeCurve.valueAt(x);
		// var yCurve = 1-((2 * (Math.pow(x, 2))) -(2*x) + 1);
		var yPos = 1 - this.yCurve.valueAt(x);
		// console.log(sizeRatio);

		var xPosRatio = xMouseRatio * 0.66 * 100;
		var yPosRatio = yPos * 0.66 * 100;
		// set the size
		$(this.tagId + " img").css({
			'width' : sizeRatio * 100 + '%'
		});
		$(this.tagId).css({
			'right' : xPosRatio + '%'
		});
		$(this.tagId).css({
			'bottom' : yPosRatio + '%'
		});
	}

};


