$('.carousel').carousel({
	interval:10000
});

$(document).on("click", ".open-Modal", function () {
var user_id = $(this).data('id');
document.getElementById("link").setAttribute("href",'eliminar/'+user_id);
});