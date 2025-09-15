function listarMaterial() {
    $.ajax ({
        url: "/inventario-material/material/",
        type: "get",
        dataType: "json",
        success: function (response) {
            if ($.fn.DataTable.isDataTable("#tabla_material")) {
                $("#tabla_material").DataTable().clear().destroy();
            }
            $('#tabla_material tbody').html("");
            for (let i = 0; i < response.length; i++) {
                let fila = '<tr>';
                fila += '<td>' + (i + 1) + '</td>';
                fila += '<td>' + response[i].fields.material + '</td>';
                fila += '<td>' + response[i].fields.partida + '</td>';
                fila += '<td>' + response[i].fields.unidad_medida + '</td>';
                fila += '<td>' + response[i].fields.nivel_minimo + '</td>';
                fila += '<td>' + response[i].fields.cantidad_existente + '</td>';
                fila += '<td>' + response[i].fields.estado + '</td>';
                fila += '<td> <button>Editar</button><button>Eliminar</button> </td>';
                fila += '</tr>';
                $('#tabla_material tbody').append(fila);
            }
            $("#tabla_material").DataTable({
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
    listarMaterial();
});
