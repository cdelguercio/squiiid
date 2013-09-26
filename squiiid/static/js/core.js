var layerlogin = false;
var layerinvite = false;
var image_id = 0;
function prepphotoshare(_image_id) {
	image_id = _image_id
	var ratio = parseFloat(document.getElementById("a-photo-"+String(image_id)).clientHeight) / parseFloat(document.getElementById("a-photo-"+String(image_id)).clientWidth)
	var small_height = Math.floor(200.0 * ratio) + 1
	var medium_height = Math.floor(500.0 * ratio) + 1
	//var large_height = Math.floor(900.0 * ratio) + 1
	document.getElementById("share-embed-small").innerHTML = "<object data=\"http://squiiid.com/image/" + _image_id + "/\" width=\"200px\" height=\"" + small_height + "px\"></object>"
	document.getElementById("share-embed-medium").innerHTML = "<object data=\"http://squiiid.com/image/" + _image_id + "/\" width=\"500px\" height=\"" + medium_height + "px\"></object>"
	//document.getElementById("share-embed-large").innerHTML = "<object data=\"http://squiiid.com/image/" + _image_id + "/\" width=\"900px\" height=\"" + large_height + "px\"></object>"
	var large_width = Math.floor(492.0 / ratio)
	document.getElementById("share-embed-large").innerHTML = "<object data=\"http://squiiid.com/image/" + _image_id + "/\" width=\"" + large_width + "px\" height=\"492px\"></object>"
}
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

		searchlayer = false;
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


// Dashboard: Image hover actions
	// Mouse over
	function dashphotomouseenter(imageid) {
		$("#photo-hover-box-"+imageid).css("opacity","1");
	}
	$(".photo-box").on("mouseenter",function(){
		$imageid = $(this).attr("value");
		dashphotomouseenter($imageid);
	});
	// Mouse leave
	function dashphotomouseleave(imageid) {
		$("#photo-hover-box-"+imageid).css("opacity","0");
	}
	$(".photo-box").on("mouseleave",function(){
		$imageid = $(this).attr("value");
		dashphotomouseleave($imageid);
	});
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
			$("#first-settings-save").css("display","block").animate({'opacity':'1'},250);
		}
		else {
			$("#settings-checkbox").attr("rel","0");
			$("settings-checkbox-hidden").attr("value","0");
			$("#first-settings-save").animate({'opacity':'0'},250,function(){
				$("#first-settings-save").css("display","none");
			});
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
// Search Results : Clicking squiiid logo goes back
	$("body").delegate("#squiiid-gohome", "click", function(){
		window.history.back();
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
	// Hitting escape has the same effect as clicking the Squiiid Logo
	$(document).keyup(function(e) {
	  if (e.keyCode == 27) {
	  	hidelayers();
	  }
	});
// Show search layer when user starts typing
	searchlayer = false; // Search layer is closed by default
	$(document).keyup(function(e) {
		if (((e.keyCode >= 48 && e.keyCode <= 90) || (e.keyCode == 32)) && (searchlayer == false)) {
	  		$("#search").css("display","block").animate({'opacity':1},300);
			$("#omgwhiteeverywhere").css("display","block").animate({'opacity':1},300);
			$("#search-field").select();
			$("#search-field").val(String.fromCharCode(e.keyCode));
			searchlayer = true;
		}
	});
// Fade in handlers
	// 1. Settings
	$("body").delegate("#nav-settings", "click", function(){
		$("#settings").css("display","block").animate({'opacity':1},300);
		$("#omgwhiteeverywhere").css("display","block").animate({'opacity':1},300);
		searchlayer = true;
	});
	// 2. Search
	$("body").delegate("#nav-search", "click", function(){
		$("#search").css("display","block").animate({'opacity':1},300);
		$("#omgwhiteeverywhere").css("display","block").animate({'opacity':1},300);
		$("#search-field").select();
	});
	$("body").delegate("#search", "click", function(){
		$("#search-field").select();
	});
	// 3. Uploader
	$("body").delegate("#nav-upload", "click", function(){
		$("#uploader").css("display","block").animate({'opacity':1},300);
		$("#omgwhiteeverywhere").css("display","block").animate({'opacity':1},300);
		searchlayer = true;
	});
	// 4. Photo Sharing
	function showphotoshare() {
		$("#photosharing").css("display","block").animate({'opacity':1},300);
		$("#omgwhiteeverywhere").css("display","block").animate({'opacity':1},300);
		searchlayer = true;
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