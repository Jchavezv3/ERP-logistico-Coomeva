// endpoint al mircoservicio
const endpointMicroservicioCrudArticulos = "http:///127.0.0.1:3002/registro-nuevo-inventario";

//========================================================
//==============       VER ARTICULOS       ===============
//========================================================
const getArticulos = () => {
    fetch(endpointMicroservicioCrudArticulos)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la solicitud');
            }
            return response.json();
        })
        .then(data => {
            const articulos = data.articulos; // Asegúrate que 'articulos' coincide con la clave del JSON retornado
            const tbody = document.querySelector('tbody'); // Selecciona el tbody donde se agregarán las filas

            // Limpiar el contenido actual del tbody
            tbody.innerHTML = '';

            // Iterar sobre los artículos y agregar cada uno a la tabla
            articulos.forEach(articulo => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${articulo.id || '-'}</td>
                    <td>${articulo.codigo || '-'}</td>
                    <td>${articulo.categoria || '-'}</td>
                    <td>${articulo.subcategoria || '-'}</td>
                    <td>${articulo.articulo || '-'}</td>
                    <td>${articulo.alerta_amarilla || '-'}</td>
                    <td>${articulo.alerta_roja || '-'}</td>
                `;

                tbody.appendChild(tr);
            });

            // Si el número de artículos es menor que la cantidad de filas predeterminadas,
            // puedes agregar filas vacías para mantener el mismo número de filas visibles
            const filasAdicionales = 23 - articulos.length;
            for (let i = 0; i < filasAdicionales; i++) {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>-</td>
                    <td>-</td>
                    <td>-</td>
                    <td>-</td>
                    <td>-</td>
                    <td>-</td>
                    <td>-</td>
                `;
                tbody.appendChild(tr);
            }
        })
        .catch(error => {
            console.error('Error al obtener los artículos:', error);
        });
};
getArticulos();

//==========================================================
//==============       CREAR ARTICULOS       ===============
//==========================================================
const postArticulos = () => {
    // Obtener los valores de los campos del formulario
    const categoria = document.getElementById("Categoría").value;
    const codigo = document.getElementById("Codigo").value;
    const subcategoria = document.getElementById("Subcategoría").value;
    const articulo = document.getElementById("Artículo").value;
    const alertaAmarilla = document.getElementById("alerta_amarilla").value;
    const alertaRoja = document.getElementById("alerta_roja").value;

    // Crear un objeto con los datos
    const datosArticulo = {
        categoria: categoria,
        codigo: codigo,
        subcategoria: subcategoria,
        articulo: articulo,
        alerta_amarilla: parseInt(alertaAmarilla), // Convertir a número
        alerta_roja: parseInt(alertaRoja) // Convertir a número
    };

    // Enviar la solicitud POST
    fetch(endpointMicroservicioCrudArticulos, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datosArticulo) // Convertir el objeto a JSON
    })
    .then(response => response.json()) // Parsear la respuesta JSON
    .then(data => {
        alert("Artículo creado exitosamente: " + data.mensaje); // Mostrar mensaje de éxito
    })
    .catch(error => {
        console.error("Error:", error); // Mostrar error en consola
        alert("Hubo un problema al crear el artículo");
    });
};

// Asignar la función al botón
document.getElementById("crear_articulo").addEventListener("click", (event) => {
    event.preventDefault();
    postArticulos()
    setTimeout(() => {
        location.reload();  // Recarga la página para mostrar los nuevos datos
    }, 3000)
});

//==========================================================
//==============       EDITAR ARTICULOS      ===============
//==========================================================
const putArticulos = () => {
    // Obtener el valor del código del artículo (ID)
    const codigoArticulo = document.getElementById("Código_artículo").value;
    
    // Obtener el atributo a editar
    const atributo = document.getElementById("edicion_atributo").value;
    
    // Obtener el nuevo valor del atributo
    const nuevoValor = document.getElementById("nuevo_valor").value;

    // Verificar que todos los campos estén completos
    if (codigoArticulo === "" || atributo === "" || nuevoValor === "") {
        alert("Por favor, complete todos los campos.");
        return;
    }

    // Crear el objeto con los datos a enviar
    const datos = {};
    datos[atributo] = nuevoValor;

    // Construir la URL completa con el código del artículo
    const url = `${endpointMicroservicioCrudArticulos}/${codigoArticulo}`;

    // Hacer la petición PUT al microservicio
    fetch(url, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        if (data.mensaje) {
            alert("Artículo actualizado exitosamente.");
            // Puedes actualizar la interfaz de usuario aquí si es necesario
        } else {
            alert("Error al actualizar el artículo.");
        }
    })
    .catch(error => {
        console.error("Error al hacer la solicitud:", error);
        alert("Error al hacer la solicitud.");
    });
};
// Agregar un listener al botón de editar
document.getElementById("editar_articulo").addEventListener("click", (event) => {
    event.preventDefault()
    putArticulos()
    setTimeout(() => {
        location.reload()
    }, 3000)
});

//==========================================================
//==============       EDITAR ARTICULOS      ===============
//==========================================================
const deleteArticulos = () => {
    // Obtener el valor del ID del artículo
    const codigoArticulo = document.getElementById("codigo_articulo").value;

    // Verificar que el ID del artículo esté completo
    if (codigoArticulo === "") {
        alert("Por favor, ingrese el codigo del artículo.");
        return;
    }

    // Construir la URL completa con el ID del artículo
    const url = `${endpointMicroservicioCrudArticulos}/${codigoArticulo}`;

    // Hacer la petición DELETE al microservicio
    fetch(url, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.mensaje) {
            alert(data.mensaje);
            // Puedes actualizar la interfaz de usuario aquí si es necesario
        } else {
            alert("Error al eliminar el artículo.");
        }
    })
    .catch(error => {
        console.error("Error al hacer la solicitud:", error);
        alert("Error al hacer la solicitud.");
    });
};

// Agregar un listener al botón de eliminar
document.getElementById("eliminar_articulo").addEventListener("click", (event) => { 
    event.preventDefault()
    deleteArticulos()
    setTimeout(() => {
        location.reload()
    }, 3000)
});
