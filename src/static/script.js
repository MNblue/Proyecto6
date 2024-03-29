

function realizarSolicitud(metodo) {
    var xhr = new XMLHttpRequest();
    xhr.open(metodo, "/producto", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    let id_producto;
    // Obtener los datos del formulario
    if (metodo === 'PATCH') {
        id_producto = parseInt(document.getElementById('id_producto').value);
    } else if (metodo === 'POST'){
        id_producto = ""; //si hacemos un post no necesitamos el id
    }else{
        //para un delete debemos tomar los datos del input
        id_producto = parseInt(document.getElementById('deleteText').value);
    }

    let nombre = "";
    let descripcion = "";
    let marca = "";
    let precio = "";
    let stock = "";

    if (metodo != 'DELETE') {
        //guardamos el resto de valores introducidos en el formulario si es POST O PATCH
        nombre = document.getElementById('nombre').value;
        descripcion = document.getElementById('descripcion').value;
        marca = document.getElementById('marca').value;
        precio = document.getElementById('precio').value;
        stock = document.getElementById('stock').value;
    }


    // Construir el objeto JSON con los datos del formulario o los datos en blanco en caso de delete, excepto id que es necesario en delete
    var datos = {
        "id_producto": id_producto,
        "nombre": nombre,
        "descripcion": descripcion,
        "marca": marca,
        "precio": precio,
        "stock": stock
    };

    // Convertir datos a JSON
    var datosJSON = JSON.stringify(datos);

    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
            console.log('Solicitud ' + metodo + ' exitosa');
            // Aquí la solicitud se ha completado con éxito
        } else {
            console.error('Error en la solicitud ' + metodo);
            // Aquí podemos manejar errores 
        }
    };
    xhr.send(datosJSON);
}



function activarID() {
    let checkbox = document.getElementById("activarCampo");
    let selectIdProducto = document.getElementById("id_producto");
    let formulario = document.getElementById("formulario");
    let btnPatch = document.getElementById("patchBtn");
    let btnPost = document.getElementById("postBtn");

    // Habilitar o deshabilitar el campo id_producto según el estado del checkbox
    selectIdProducto.disabled = !checkbox.checked;

    // Llamar a la función actualizarFormulario() cuando cambie el valor del select id_producto
    selectIdProducto.addEventListener('change', function() {
        actualizarFormulario(selectIdProducto.value);
    });

    // Llamar a la función actualizarFormulario() al cargar la página para establecer el estado inicial
    if (checkbox.checked) {
        actualizarFormulario(selectIdProducto.value);
        // Habilitar o deshabilitar los botones según el estado del checkbox
        btnPatch.disabled = false;
        btnPost.disabled = true;
    } else {
        btnPatch.disabled = true;
        btnPost.disabled = false;
        formulario.reset();
    }
}


// Función para actualizar el formulario con los datos del producto seleccionado
function actualizarFormulario(idProducto) {
    // Buscar el registro correspondiente en la tabla y actualizar el formulario
    let tablaRegistros = document.querySelectorAll('.productos-table tbody tr');
    for (let i = 0; i < tablaRegistros.length; i++) {
        let registro = tablaRegistros[i];
        if (registro.cells[0].textContent === idProducto) {
            formulario.id_producto.value = idProducto;
            formulario.nombre.value = registro.cells[1].textContent;
            formulario.descripcion.value = registro.cells[2].textContent;
            formulario.marca.value = registro.cells[3].textContent;
            formulario.precio.value = registro.cells[4].textContent;
            formulario.stock.value = registro.cells[5].textContent;
            break;
        }
    }
}