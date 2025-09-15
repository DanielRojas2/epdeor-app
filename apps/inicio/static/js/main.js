var $ = jQuery.noConflict();

document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.getElementById('hamburger-btn');
    const navbar = document.getElementById('navbar-links');

    if (hamburger && navbar) {
        hamburger.addEventListener('click', function() {
            navbar.classList.toggle('active');
        });
    }
});

function abrir_modal_edicion(url) {
    $('#edicion').load(url, function() {
        $(this).modal('show');
    });
}
function cerrar_modal_edicion() {
    $('#edicion').modal('hide');
}

function abrir_modal_creacion(url) {
    $('#creacion').load(url, function() {
        var modal = new bootstrap.Modal(document.getElementById('creacion'));
        modal.show();
    });
}

function cerrar_modal_creacion() {
    var modal = bootstrap.Modal.getInstance(document.getElementById('creacion'));
    modal.hide();
}
