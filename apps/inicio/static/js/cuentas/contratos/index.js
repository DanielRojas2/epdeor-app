function listarContratos() {
    $.ajax ({
        url: "/cuentas/contratos/",
        type: "get",
        dataType: "json",
        success: function (response) {
            if ($.fn.DataTable.isDataTable("#tabla_contratos")) {
                $("#tabla_contratos").DataTable().clear().destroy();
            }
            $('#tabla_contratos tbody').html("");
            for (let i = 0; i < response.length; i++) {
                let fila = '<tr>';
                fila += '<td>' + (i + 1) + '</td>';
                fila += '<td>' + response[i].fields.cargo + '</td>';
                fila += '<td>' + response[i].fields.personal + '</td>';
                fila += '<td>' + response[i].fields.estado + '</td>';
                fila += '<td> <button>Editar</button><button>Eliminar</button> </td>';
                fila += '</tr>';
                $('#tabla_contratos tbody').append(fila);
            }
            $("#tabla_contratos").DataTable({
                responsive: true,
                pageLength: 5,
                lengthMenu: [5, 10, 20, 50],
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
            listarContratos();
            cerrar_modal_creacion();
        },
        error: function (error) {
            console.log(error);
        }
    })
}

$(document).ready(function() {
    listarContratos();
});
