// endpoint al mircoservicio
const endpointMicroservicioCrudEmpleados = "http://127.0.0.1:3001/registro-empleados";

//======================================================================
//=================         VER EMPLEADOS       ========================
//======================================================================
const getEmpleados = () => {

    fetch(endpointMicroservicioCrudEmpleados)
        .then((respuestaServer) => {
            if (!respuestaServer.ok) {
                throw new Error(`Error en la solicitud: ${respuestaServer.status}`);
            }

            console.log("Servidor conectado");

            // Accedemos al contenido de la respuesta por medio de json
            return respuestaServer.json();
        })
        .then((jsonEmpleados) => {

            // Seleccionamos el contenedor de empleados
            const contenedorEmpleados = document.querySelector(".contendor_empleados");

            // Generamos el HTML para cada empleado
            const htmlEmpleados = jsonEmpleados.empleados.map(empleado => `
                <div class="empleado_registrado">
                    <img src="../../static/img/imagenEmpleado.jpg.png" alt="foto_empleado">
                    <h2>${empleado.cargo}</h2>
                    <p>ID: ${empleado.id}</p>
                    <p>Nombre: ${empleado.nombres} ${empleado.apellidos}</p>
                    <p>Cédula: ${empleado.cedula}</p>
                    <p>Correo: ${empleado.correo}</p>
                </div>
            `).join('');

            // Añadir el HTML al contenedor
            contenedorEmpleados.innerHTML = htmlEmpleados;
        })
        .catch((error) => {
            console.log(`Error: ${error}`);
        });
};
getEmpleados();

//======================================================================
//=================        CREAR EMPLEADOS      ========================
//======================================================================
const postEmpleados = () => {
    // Recopilamos los datos del formulario
    const nombres = document.getElementById('nombres').value;
    const apellidos = document.getElementById('apellidos').value;
    const cedula = document.getElementById('cedula').value;
    const cargo = document.getElementById('cargo').value;
    const correo = document.getElementById('correo').value;
    const clave = document.getElementById('clave').value;

    // Creamos un objeto con los datos del formulario
    const datosEmpleado = {
        nombres: nombres,
        apellidos: apellidos,
        cedula: cedula,
        cargo: cargo,
        correo: correo,
        clave: clave
    };

    // Enviamos la solicitud POST
    fetch(endpointMicroservicioCrudEmpleados, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // especificar el tipo de contenido
        },
        body: JSON.stringify(datosEmpleado)  // Convertimos los datos a JSON
    })
    .then((respuestaServer) => {
        if (!respuestaServer.ok) {
            throw new Error(`Error en la solicitud: ${respuestaServer.status}`);
        }
        return respuestaServer.json();
    })
    .then((mensaje) => {
        // Manejar la respuesta del servidor
        console.log(mensaje.message);
        alert(mensaje.message);  // Muestra un mensaje al usuario
    })
    .catch((error) => {
        console.error('Hubo un problema con la solicitud:', error);
    });
};
document.getElementById('regritar_empleado').addEventListener('click', (event) => {
    event.preventDefault();  // Prevenir el envío del formulario por defecto
    postEmpleados();
    setTimeout(() => {
        location.reload();  // Recarga la página para mostrar los nuevos datos
    }, 3000)
});

//======================================================================
//=================        EDITAR EMPLEADOS      =======================
//======================================================================
const putEmpleado = () => {
    // Obtener los valores del formulario
    const idEmpleado = document.getElementById('id_empleado').value;
    const atributo = document.getElementById('edicion_atributo').value;
    const nuevoValor = document.getElementById('nuevo_valor_empleado').value;

    // Verificar que todos los campos estén completos
    if (!idEmpleado || !atributo || !nuevoValor) {
        alert('Por favor, complete todos los campos.');
        return;
    }

    // Preparar los datos para enviar
    const datosEmpleado = {
        [atributo]: nuevoValor
    };

    // Construir la URL con el ID del empleado par qiue el microservicio la acepte
    const urlConId = `${endpointMicroservicioCrudEmpleados}/${idEmpleado}`;

    // Enviar la solicitud al microservicio
    fetch(urlConId, {
        method: 'PUT',  
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datosEmpleado)
    })
    .then(respuestaServer => {
        if (!respuestaServer.ok) {
            throw new Error(`Error en la solicitud: ${respuestaServer.status}`);
        }
        return respuestaServer.json();
    })
    .then(data => {
        console.log('Respuesta del servidor:', data);
        alert('Datos del empleado actualizados correctamente.');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un problema al actualizar los datos del empleado.');
    });
};

// Asignar la función al botón de editar empleado
document.getElementById('editar_empleado').addEventListener('click', (event) => {
    event.preventDefault();  // Prevenir el envío del formulario por defecto
    putEmpleado();
    setTimeout(() => {
        location.reload();  // Recarga la página para mostrar los nuevos datos
    }, 3000)
});

//======================================================================
//=================        ELIMINAR EMPLEADOS      =====================
//======================================================================
const deleteEmpleado = () => {
    // Obtener el ID del empleado del campo de entrada
    const idEmpleado = document.getElementById('id_empleado_eliminar').value;

    // Verificar si se ha ingresado un ID
    if (!idEmpleado) {
        alert('Por favor, ingrese un ID de empleado.');
        return;
    }

    // Construir la URL del endpoint con el ID del empleado
    const url = `${endpointMicroservicioCrudEmpleados}/${idEmpleado}`;

    // Enviar la solicitud DELETE al servidor
    fetch(url, {
        method: 'DELETE'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Manejar la respuesta del servidor
        alert(data.message);
        // Recargar la página después de un pequeño retraso para mostrar los cambios
        setTimeout(() => {
            location.reload();
        }, 3000);
    })
    .catch(error => {
        console.error('Hubo un problema con la solicitud:', error);
    });
};

// Asignar la función al botón de eliminar empleado
document.getElementById('eliminar_empleado').addEventListener('click', (event) => {
    event.preventDefault();  // Prevenir el envío del formulario por defecto
    deleteEmpleado();
});