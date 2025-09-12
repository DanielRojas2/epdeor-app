document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modal");
    const tabla = document.getElementById("tabla-materiales");

    function openModal(html) {
        modal.innerHTML = html;
        modal.classList.remove("hidden");
    }

    function closeModal() {
        modal.innerHTML = "";
        modal.classList.add("hidden");
    }

    async function fetchHTML(url, options = {}) {
        const res = await fetch(url, options);
        const html = await res.text();
        return html;
    }

    // Crear material
    document.getElementById("btn-add-material").addEventListener("click", async () => {
        try {
            const html = await fetchHTML("/material/material/create/");
            openModal(html);
        } catch (err) {
            console.error("Error cargando modal de material:", err);
        }
    });

    // Delegación de eventos en tabla
    tabla.addEventListener("click", async e => {
        const target = e.target;
        if (target.classList.contains("btn-edit")) {
            const id = target.dataset.id;
            try {
                const html = await fetchHTML(`/material/material/${id}/update/`);
                openModal(html);
            } catch (err) {
                console.error("Error cargando edición de material:", err);
            }
        }
        if (target.classList.contains("btn-delete")) {
            const id = target.dataset.id;
            try {
                const html = await fetchHTML(`/material/material/${id}/delete/`);
                tabla.innerHTML = html;
            } catch (err) {
                console.error("Error eliminando material:", err);
            }
        }
    });

    // Delegación de submit en modal
    modal.addEventListener("submit", async e => {
        e.preventDefault();
        const form = e.target;
        const url = form.getAttribute("action") || window.location.pathname;
        const formData = new FormData(form);

        try {
            const html = await fetchHTML(url, { method: "POST", body: formData });
            if (form.id === "form-material") {
                tabla.innerHTML = html; // actualiza tabla
                closeModal();
            } else {
                openModal(html); // vuelve a mostrar formulario con errores
            }
        } catch (err) {
            console.error("Error enviando formulario:", err);
        }
    });

    // Abrir sub-modales de Partida y UdM desde el modal de Material
    modal.addEventListener("click", async e => {
        if (e.target.id === "btn-add-partida") {
            try {
                const html = await fetchHTML("/material/partida/create/");
                openModal(html);
            } catch (err) {
                console.error("Error cargando modal de partida:", err);
            }
        }
        if (e.target.id === "btn-add-udm") {
            try {
                const html = await fetchHTML("/material/udm/create/");
                openModal(html);
            } catch (err) {
                console.error("Error cargando modal de UdM:", err);
            }
        }
    });

    // Submit para los formularios de Partida y UdM
    modal.addEventListener("submit", async e => {
        const form = e.target;
        if (form.id === "form-partida" || form.id === "form-udm") {
            e.preventDefault();
            const url = form.getAttribute("action") || window.location.pathname;
            const formData = new FormData(form);

            try {
                const html = await fetchHTML(url, { method: "POST", body: formData });
                // Insertamos nueva opción en el select de Material
                if (form.id === "form-partida") {
                    const select = document.querySelector("select[name='partida']");
                    const tempDiv = document.createElement("div");
                    tempDiv.innerHTML = html;
                    const option = tempDiv.querySelector("option");
                    if (option) select.add(option);
                }
                if (form.id === "form-udm") {
                    const select = document.querySelector("select[name='unidad_medida']");
                    const tempDiv = document.createElement("div");
                    tempDiv.innerHTML = html;
                    const option = tempDiv.querySelector("option");
                    if (option) select.add(option);
                }
                closeModal();
            } catch (err) {
                console.error("Error guardando Partida o UdM:", err);
            }
        }
    });
});
