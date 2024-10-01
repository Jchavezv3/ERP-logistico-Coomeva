// endpoint al mircoservicio
const endpointMicroservicioCrudMovimientos = "http://192.168.18.253:3003/movimientos-inventario"

//========================================================
//==============       VER ARTICULOS       ===============
//========================================================
const obtenerDatosMovimientos = () => {
    fetch(endpointMicroservicioCrudMovimientos)
        .then(response => {
            if (!response.ok) {
                throw new Error("Error al obtener datos del microservicio");
            }
            return response.json();
        })
        .then(data => {
            // Llenar los select con las categorías, subcategorías y artículos
            llenarSelect("#categoria_articulo", data.items_categorias);
            llenarSelect("#subcategoria_articulo", data.items_subcategorias);
            llenarSelect("#Articulo", data.items_articulo);

            // Llenar la tabla con los movimientos
            llenarTablaMovimientos(data.movimientos);
        })
        .catch(error => {
            console.error("Error:", error);
        });
};

// Función para llenar los selectores con los datos obtenidos del microservicio
const llenarSelect = (selector, items) => {
    const selectElement = document.querySelector(selector);
    items.forEach(item => {
        const option = document.createElement("option");
        option.value = item;
        option.textContent = item;
        selectElement.appendChild(option);
    });
};

// Función para llenar la tabla con los movimientos obtenidos del microservicio
const llenarTablaMovimientos = (movimientos) => {
    const tbody = document.querySelector("table tbody");
    tbody.innerHTML = "";  // Limpiar la tabla antes de llenarla

    movimientos.forEach(movimiento => {
        const tr = document.createElement("tr");

        const tdId = document.createElement("td");
        tdId.textContent = movimiento.id;
        tr.appendChild(tdId);

        const tdArticulo = document.createElement("td");
        tdArticulo.textContent = movimiento.articulo;
        tr.appendChild(tdArticulo);

        const tdTipo = document.createElement("td");
        tdTipo.textContent = movimiento.tipo_movimiento;
        tr.appendChild(tdTipo);

        const tdCantidad = document.createElement("td");
        tdCantidad.textContent = movimiento.cantidad;
        tr.appendChild(tdCantidad);

        const tdCosto = document.createElement("td");
        tdCosto.textContent = `$${movimiento.costo}`;
        tr.appendChild(tdCosto);

        tbody.appendChild(tr);
    });
};

// Llamada inicial para cargar los datos al cargar la página
obtenerDatosMovimientos();