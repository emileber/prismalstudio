/**
 * specific js script for app Prismal.
 */

function seatMouseMoveHandler(event) {
	var msg = "Handler for .mousemove() called at ";
	msg += event.pageX + ", " + event.pageY;
	//console.log (msg);
	
	
	var xMouseRatio = event.pageX/$(window).width();
	var yMouseRatio = event.pageY/$(window).height();
	
	
	// entre 50 et 100%
	var sizeRatio = 100 - ((xMouseRatio * 0.5)+(yMouseRatio*0.5)) * 100;
	
	var xPosRatio = xMouseRatio  * 0.33 * 100;
	var yPosRatio = yMouseRatio  * 0.33 * 100;
	// set the size
	$('#prismal-seat img').css({'width':sizeRatio + '%'});
	$('#prismal-seat').css({'right':xPosRatio + '%'});
	$('#prismal-seat').css({'bottom':yPosRatio + '%'});
}