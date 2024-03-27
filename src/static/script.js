

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
            // Aquí puedes hacer algo adicional después de que la solicitud se complete con éxito
        } else {
            console.error('Error en la solicitud ' + metodo);
            // Aquí puedes manejar errores si es necesario
        }
    };
    xhr.send(datosJSON);
}
