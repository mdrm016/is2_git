$('.carousel').carousel({
	interval:10000
});

$(document).on("click", ".usuarios", function () {
var id = $(this).data('id');
document.getElementById("link").setAttribute("href",'eliminar/'+id);
});

$(document).on("click", ".proyectos", function () {
	var id = $(this).data('id');
	document.getElementById("proyecto").setAttribute("href",'adm_proyecto/eliminar/'+id);
});

$(document).on("click", ".roles", function () {
	var id = $(this).data('id');
	document.getElementById("rol").setAttribute("href",'eliminar/'+id);
});
