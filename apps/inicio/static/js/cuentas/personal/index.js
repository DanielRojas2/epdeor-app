function listarPersonal() {
    $.ajax ({
        url: "/cuentas/personal/",
        type: "get",
        dataType: "json",
        success: function (response) {
            if ($.fn.DataTable.isDataTable("#tabla_personal")) {
                $("#tabla_personal").DataTable().clear().destroy();
            }
            $('#tabla_personal tbody').html("");
            for (let i = 0; i < response.length; i++) {
                let fila = '<tr>';
                fila += '<td>' + (i + 1) + '</td>';
                fila += '<td>' + response[i].fields.nombre_personal + '</td>';
                fila += '<td>' + response[i].fields.apellido_paterno + '</td>';
                fila += '<td>' + response[i].fields.apellido_materno + '</td>';
                fila += '<td>' + response[i].fields.estado + '</td>';
                fila += '<td> <button>Editar</button><button>Eliminar</button> </td>';
                fila += '</tr>';
                $('#tabla_personal tbody').append(fila);
            }
            $("#tabla_personal").DataTable({
                language: {
                    decimal: "",
                    emptyTable: "No hay información",
                    info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                    infoFiltered: "(Filtrado de _MAX_ total entradas)",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "Mostrar _MENU_ Entradas",
                    loadingRecords: "Cargando...",
                    processing: "Procesando...",
                    search: "Buscar:",
                    zeroRecords: "Sin resultados encontrados",
                    paginate: {
                        first: "Primero",
                        last: "Ultimo",
                        next: "Siguiente",
                        previous: "Anterior",
                    },
                },
                responsive: true,
            });
        },
        error: function (error) {
            console.log(error);
        }
    })
}

function registrar() {
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function (response) {
            listarPersonal();
            cerrar_modal_creacion();
        },
        error: function (error) {
            console.log(error);
        }
    })
}

$(document).ready(function() {
    listarPersonal();
});
