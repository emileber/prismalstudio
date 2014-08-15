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
		// var msg = "Handler for .mousemove() called at ";
		// msg += event.pageX + ", " + event.pageY;
		// console.log (msg);

		var xMouseRatio = event.pageX / $(window).width();
		// var yMouseRatio = event.pageY / $(window).height();
		// var mouseRatio = (yMouseRatio + xMouseRatio) / 2;

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

// var sizeCurve = new Parabola();
// // parabola.solveWithPoints(0, 1, 0.5, 0.5, 1, 1);
// sizeCurve.solveWithY(1, 0.2, 0.8);
//
// var yCurve = new Parabola();
// yCurve.solveWithY(1, 0.5, 0.8);
//
// function seatMouseMoveHandler(event) {
// // var msg = "Handler for .mousemove() called at ";
// // msg += event.pageX + ", " + event.pageY;
// // console.log (msg);
//
// var xMouseRatio = event.pageX / $(window).width();
// var yMouseRatio = event.pageY / $(window).height();
// var mouseRatio = (yMouseRatio + xMouseRatio) / 2;
//
// // console.log(parabola.valueAt(xMouseRatio));
//
// // entre 50 et 100%
// var x = xMouseRatio;
// // var sizeRatio = (2 * (Math.pow(x, 2))) -(2*x) + 1;
// var sizeRatio = sizeCurve.valueAt(x);
// // var yCurve = 1-((2 * (Math.pow(x, 2))) -(2*x) + 1);
// var yPos = 1 - yCurve.valueAt(x);
// console.log(sizeRatio);
//
// var xPosRatio = xMouseRatio * 0.66 * 100;
// var yPosRatio = yPos * 0.66 * 100;
// // set the size
// $('#prismal-seat').css({
// 'width' : sizeRatio * 100 + '%'
// });
// $('#prismal-seat').css({
// 'right' : xPosRatio + '%'
// });
// $('#prismal-seat').css({
// 'bottom' : yPosRatio + '%'
// });
// }
