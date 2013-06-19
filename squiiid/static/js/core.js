// Javascript for Squiiid


//	Keycodes:
//		37: Left Arrow
//		38: Up Arrow
//		39: Right Arrow
//		40: Down Arrow
//		13: Enter

var layerlogin = false;
var layerinvite = false;

function loginShow() {
	$("#requestinvite").css("display","none")
	$("#login").css("display","block")
	layerlogin = true;
	layerinvite = false;
}

function inviteShow() {
	$("#login").css("display","none")
	$("#requestinvite").css("display","block")
	layerinvite = true;
	layerlogin = false;
}
function loginInviteHide() {
	$("#login").css("display","none")
	$("#requestinvite").css("display","none")
	layerinvite = false;
	layerlogin = false;
}

// User clicks "sunshine" login button at the top
$("#button-login").on("click",function(){
	// If already displaying login view, hide it
	if (layerlogin == true) {
		loginInviteHide();
	}
	else {
		loginShow();
	}
});

// User clicks big squid button on home page
$("#squid-button").on("click",function(){
	// If already displaying login view, hide it
	if (layerinvite == false) {
		inviteShow();
	}
});
// Request invite link at bottom of page
$("#requestinvite2").on("click",function(){
	// If already displaying login view, hide it
	if (layerinvite == false) {
		inviteShow();
	}
});


var requestform = document.forms['requestinvite'];
// Submit form
function submitInviteRequest() {
		requestform.submit();
}
// From request invite screen, user clicks submit
$("#requestinvitebutton").on("click",function(){
	submitInviteRequest();
	// Hide Invite View
	loginInviteHide();
	// Show confirmation page
	$("#inviteconfirm").css("display","block");
});

// User clicks anywhere on confirmation page
$("#inviteconfirm").on("click",function(){
	// Hide confirmation page
	$("#inviteconfirm").css("display","none");
});