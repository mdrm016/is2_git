$('.carousel').carousel({
	interval:10000
});

$(document).on("click", ".usuarios", function () {
var id = $(this).data('id');
document.getElementById("link").setAttribute("href",'eliminar/'+id);
});

$(document).on("click", ".proyectos", function () {
	var id = $(this).data('id');
		document.getElementById("proyecto").setAttribute("href",'eliminar/'+id);
});


$(document).on("click", ".roles", function () {
	var id = $(this).data('id');
	document.getElementById("rol").setAttribute("href",'eliminar/'+id);
});

$(document).on("click", ".fases", function () {
	var id = $(this).data('id');
	document.getElementById("fase").setAttribute("href",'eliminar/'+id);
});

$(document).on("click", ".tipoitems", function () {
	var id = $(this).data('id');
	document.getElementById("tipoitem").setAttribute("href",'eliminar/'+id);
});

$(document).on("click", ".tipoatributo", function () {
	var id = $(this).data('id');
	document.getElementById("tipoAtributo").setAttribute("href",'eliminar/'+id);
});

$(document).on("click", ".items", function () {
	var id = $(this).data('id');
	document.getElementById("item").setAttribute("href",'eliminar/'+id);
});

$(document).on("click", ".relaciones", function () {
	var id = $(this).data('id');
	document.getElementById("relacion").setAttribute("href",'eliminar/'+id);
});

$(document).on("click", ".solicitudRealizada", function () {
	var id = $(this).data('id');
		document.getElementById("solicitudRealizada").setAttribute("href",'/adm_proyectos/solicitudes_realizadas/cancelar_solicitud/'+id);
});

$(document).on("click", ".credencial", function () {
	var id = $(this).data('id');
		document.getElementById("credencial").setAttribute("href",'/adm_proyectos/admin_credenciales/cancelar_credencial/'+id);
});

$(document).ready(function() {
    var posicion = $("#caja_flotante").offset();
    var margenSuperior = 15;
     $(window).scroll(function() {
         if ($(window).scrollTop() > posicion.top) {
             $("#caja_flotante").stop().animate({
                 marginTop: $(window).scrollTop() - posicion.top + margenSuperior
             });
         } else {
             $("#caja_flotante").stop().animate({
                 marginTop: 0
             });
         };
     });
});