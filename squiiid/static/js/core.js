// Javascript for Squiiid


//--------------------------------------------------------
//
//						Home Page
//
//--------------------------------------------------------

//	Keycodes:
//		37: Left Arrow
//		38: Up Arrow
//		39: Right Arrow
//		40: Down Arrow
//		13: Enter

var layerlogin = false;
var layerinvite = false;
var image_id = 0;

function prepphotoshare(_image_id) {
	image_id = _image_id
	var ratio = parseFloat(document.getElementById("a-photo-"+String(image_id)).clientHeight) / parseFloat(document.getElementById("a-photo-"+String(image_id)).clientWidth)
	alert(document.getElementById("a-photo-"+String(image_id)).clientHeight)
	var small_height = Math.floor(200.0 * ratio) + 1
	var medium_height = Math.floor(500.0 * ratio) + 1
	var large_height = Math.floor(900.0 * ratio) + 1
	document.getElementById("share-embed-small").innerHTML = "<object src=\"http://squiiid.com/image/" + _image_id + "/\" width=\"200px\" height=\"" + small_height + "px\"></object>"
	document.getElementById("share-embed-medium").innerHTML = "<object src=\"http://squiiid.com/image/" + _image_id + "/\" width=\"500px\" height=\"" + medium_height + "px\"></object>"
	document.getElementById("share-embed-large").innerHTML = "<object src=\"http://squiiid.com/image/" + _image_id + "/\" width=\"900px\" height=\"" + large_height + "px\"></object>"
}

function loginShow() {
	// Fade out INVITE slide whether open or not
	$("#requestinvite").animate({opacity:0},300, function(){
		$("#requestinvite").css("display","none");
	});
	layerinvite = false;
	// Fade out LOGIN BUTTON
	$("#button-login").animate({opacity:0},300, function(){
		$("#button-login").css("display","none");
	});
	// Fade in LOGIN slide
	$("#login").css("display","block").animate({opacity:1},300);
	layerlogin = true;
	// Fade in BACK BUTTON
	$("#button-back").css("display","block").animate({opacity:1},300);
}

function inviteShow() {
	// Fade out LOGIN slide whether open or not
	$("#login").animate({opacity:0},300, function(){
		$("#login").css("display","none");
	});
	layerinvite = true;
	// Fade out LOGIN BUTTON
	$("#button-login").animate({opacity:0},300, function(){
		$("#button-login").css("display","none");
	});
	// Fade in INVITE slide
	$("#requestinvite").css("display","block").animate({opacity:1},300);
	layerlogin = false;
	// Fade in BACK BUTTON
	$("#button-back").css("display","block").animate({opacity:1},300);
}
function loginInviteHide() {
	// Fade in LOGIN BUTTON
	$("#button-login").css("display","block").animate({opacity:1},300);
	// Fade out INVITE slide
	$("#requestinvite").animate({opacity:0},300, function(){
		$("#requestinvite").css("display","none");
	});
	layerinvite = false;
	// Fade out LOGIN slide
	$("#login").animate({opacity:0},300, function(){
		$("#login").css("display","none");
	});
	layerlogin = false;
	// Fade out BACK BUTTON
	$("#button-back").animate({opacity:0},300, function(){
		$("#button-back").css("display","none");
	});
}

// User clicks "back arrow" button 
$("#button-back").on("click",function(){
	loginInviteHide();
});
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

//--------------------------------------------------------
//
//						Operations
//
//--------------------------------------------------------

// Function for fading out layers
	function hidelayers() {
		// Looks at all the "layers" and determines if they are visible or not
		// If visible, fades them out

		// 1. Photo sharing
		if ($("#photosharing").css("display") == "block") {
			$("#photosharing").animate({'opacity':0},300, function(){
				$("#photosharing").css("display","none");
			});
		}
		// 2. Settings
		if ($("#settings").css("display") == "block") {
			$("#settings").animate({'opacity':0},300, function(){
				$("#settings").css("display","none");
			});
		}
		// 3. Search
		if ($("#search").css("display") == "block") {
			$("#search").animate({'opacity':0},300, function(){
				$("#search").css("display","none");
			});
		}
		// 4. Uploader
		if ($("#uploader").css("display") == "block") {
			$("#uploader").animate({'opacity':0},300, function(){
				$("#uploader").css("display","none");
			});
		}

		// Always fade out the white overlay
		$("#omgwhiteeverywhere").animate({'opacity':0},300, function(){
			$("#omgwhiteeverywhere").css("display","none");
		});
	}

// Function for sizing overlays on "My Photos"
	function sizeOverlays() {
		// $(".a-photo").each(function(index, box){
		// 	$imgheight = $(box).height();
		// 	$imgwidth = $(box).width();
		// 	$imgoffset = Number($imgheight)* -1;
		// 	$(box).siblings(".photo-hover-box").css({
		// 		'width': $imgwidth,
		// 		'height': $imgheight,
		// 		'margin-bottom': $imgoffset,
		// 	});
		// 	$(box).attr("rel",$imgoffset);
		// });
		$(".a-photo").each(function(index, box){
			$imgheight = $(box).height();
			$imgwidth = $(box).width();
			$imgoffset = Number($imgheight)* -1;
			$(box).siblings(".photo-hover-box").css({
				'width': $imgwidth,
				'height': $imgheight,
				'margin-bottom': $imgoffset,
			});
			$(box).attr("rel",$imgoffset);
		});
	}

// Uploader: Function for switching open sections
	var opensection = '480px';
	var closedsection = '54px';
	function switchsection(sectionid) {
		// Assign objects from sectionid
		if (sectionid == "section-tags") {var exception = $("#section-tags");}
		else if (sectionid == "section-contributors") {var exception = $("#section-contributors");}
		else if (sectionid == "section-geo") {var exception = $("#section-geo");}
		else if (sectionid == "section-camera") {var exception = $("#section-camera");}
		else if (sectionid == "section-products") {var exception = $("#section-products");}
		// Check all sections, collapse all that are not the targeted one
		$.each($(".upload-details > .upload-section"), function (i, section) {
			if (section.getAttribute("id") == sectionid) {
				section.setAttribute("rel","open");
			}
			else {
				section.setAttribute("rel","closed");
			}
		});
	}
// Error: Fade in & Out Functions
	function showerror() {
		$(".error").css("display","block").animate({'opacity':'1'},250);
	}
	function hideerror() {
		$(".error").animate({'opacity':'0'},250,function() {
			$(".error").css("display","none")
		});
	}
// Uploader: Keeps form from submitting on enter
	$('#upload-form').bind("keyup", function(e) {
		var code = e.keyCode || e.which; 
		if (code  == 13) {               
			e.preventDefault();
			return false;
		}
	});

//--------------------------------------------------------
//
//						Handlers
//
//--------------------------------------------------------

// Uploader: User clicks on the icon for a section
	// Uploader: Tags section
	$("body").delegate("#upload-tags", "click", function(){
		if ($("#section-tags").attr("rel") == "closed") {switchsection("section-tags");}
		else {}
	});
	// Uploader: Contributors section
	$("body").delegate("#upload-contributors", "click", function(){
		if ($("#section-contributors").attr("rel") == "closed") {switchsection("section-contributors");}
		else {}
	});
	// Uploader: Geo section
	$("body").delegate("#upload-geo", "click", function(){
		if ($("#section-geo").attr("rel") == "closed") {switchsection("section-geo");}
		else {}
	});
	// Uploader: Camera section
	$("body").delegate("#upload-camera", "click", function(){
		if ($("#section-camera").attr("rel") == "closed") {switchsection("section-camera");}
		else {}
	});
	// Uploader: Products section
	$("body").delegate("#upload-products", "click", function(){
		if ($("#section-products").attr("rel") == "closed") {switchsection("section-products");}
		else {}
	});
// Uploader: User clicks "iii'm done", show loading layer until page is refreshed
	function showloading() {
		$("#loading").css("display","block").animate({'opacity':'1'},300);
	}
// Checkbox toggle in settings
	$("body").delegate("#settings-checkbox", "click", function(){
		if ($("#settings-checkbox").attr("rel") == "0") {
			$("#settings-checkbox").attr("rel","1");
			$("settings-checkbox-hidden").attr("value","1");
		}
		else {
			$("#settings-checkbox").attr("rel","0");
			$("settings-checkbox-hidden").attr("value","0");
		}
	});
// Hide Error Layer when X is clicked
	$("body").delegate("#error-x", "click", function(){
		hideerror();
	});
// Photo sharing: show/hide embed box
	// Show
	$("body").delegate("#share-embed", "click", function(){
		$("#share-embed-box").css("display","block").animate({'opacity':'1'},250);
		$("#share-embed-code").focus().select();
	});
	// Clicks on the textarea auto select all
	$("body").delegate(".share-embed-code", "click", function(){
		$(this).focus().select();
	});
	// Hide
	$("body").delegate("#share-embed-x", "click", function(){
		$("#share-embed-box").animate({'opacity':'0'},250, function(){
			$("#share-embed-box").css("display","none")
		});
	});
// Fade out handlers
	// The X button on the photo-sharing menu
	$("body").delegate("#photo-share-x", "click", function(){
		hidelayers();
	});
	// Clicking the Squiiid logo
	$("body").delegate("#squiiid-logo", "click", function(){
		hidelayers();
	});
	// The "save" popsicle in settings
	$("body").delegate("#settings-save", "click", function(){
		hidelayers();
	});
// Fade in handlers
	// 1. Settings
	$("body").delegate("#nav-settings", "click", function(){
		$("#settings").css("display","block").animate({'opacity':1},300);
		$("#omgwhiteeverywhere").css("display","block").animate({'opacity':1},300);
	});
	// 2. Search
	$("body").delegate("#nav-search", "click", function(){
		$("#search").css("display","block").animate({'opacity':1},300);
		$("#omgwhiteeverywhere").css("display","block").animate({'opacity':1},300);
	});
	// 3. Uploader
	$("body").delegate("#nav-upload", "click", function(){
		$("#uploader").css("display","block").animate({'opacity':1},300);
		$("#omgwhiteeverywhere").css("display","block").animate({'opacity':1},300);
	});
	// 4. Photo Sharing
	function showphotoshare() {
		$("#photosharing").css("display","block").animate({'opacity':1},300);
		$("#omgwhiteeverywhere").css("display","block").animate({'opacity':1},300);
	}

// On document ready, load photos
	$(window).ready(function(){
		$(".a-photo").each(function(index, box){
			$imgheight = $(box).height();
			$imgwidth = $(box).width();
			$imgoffset = Number($imgheight)* -1;
			$(box).siblings(".photo-hover-box").css({
				'width': $imgwidth,
				'height': $imgheight,
				'margin-bottom': $imgoffset,
			});
			$(box).attr("rel",$imgoffset);
			$(box).load(function(){
				$imgheight = $(this).height();
				$imgwidth = $(this).width();
				$imgoffset = Number($imgheight)* -1;
				$(this).siblings(".photo-hover-box").css({
					'width': $imgwidth,
					'height': $imgheight,
					'margin-bottom': $imgoffset,
				});
				$(this).attr("rel",$imgoffset);
			});
		});
	});

// On window resize, fix sizing of overlays
	$(window).resize(function() {
		sizeOverlays();
	});