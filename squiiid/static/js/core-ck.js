// Javascript for Squiiid
//	Keycodes:
//		37: Left Arrow
//		38: Up Arrow
//		39: Right Arrow
//		40: Down Arrow
//		13: Enter
function loginShow(){$("#requestinvite").css("display","none");$("#login").css("display","block");layerlogin=!0;layerinvite=!1}function inviteShow(){$("#login").css("display","none");$("#requestinvite").css("display","block");layerinvite=!0;layerlogin=!1}function loginInviteHide(){$("#login").css("display","none");$("#requestinvite").css("display","none");layerinvite=!1;layerlogin=!1}function submitInviteRequest(){requestform.submit()}var layerlogin=!1,layerinvite=!1;$("#button-login").on("click",function(){layerlogin==1?loginInviteHide():loginShow()});$("#squid-button").on("click",function(){layerinvite==0&&inviteShow()});$("#requestinvite2").on("click",function(){layerinvite==0&&inviteShow()});var requestform=document.forms.requestinvite;$("#requestinvitebutton").on("click",function(){submitInviteRequest();loginInviteHide();$("#inviteconfirm").css("display","block")});$("#inviteconfirm").on("click",function(){$("#inviteconfirm").css("display","none")});