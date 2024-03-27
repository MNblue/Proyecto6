from flask import Blueprint, request, render_template
from src.services.proveedorServices import proveeddorServices
from src.models.proveedorModel import proveedor;

main = Blueprint('proveedor_blueprint',__name__)

@main.route('/',methods=['GET','POST', 'PATCH','DELETE'])

def get_proveed():

    print(request)
    print(request.method)


    if request.method != 'GET':

        print(request.json)
        id_proveedor = request.json["id_proveedor"]
        nombre = request.json["nombre"]
        direccion = request.json["direccion"]
        telefono = request.json["telefono"]
        proveedor1 = proveedor(id_proveedor,nombre,direccion,telefono)


    if request.method == 'GET':
        get_proveedor1 = proveeddorServices.get_proveedor()
        print(get_proveedor1)
        return get_proveedor1
    elif request.method == 'POST':
        post_proveedor = proveeddorServices.post_proveedor(proveedor1)
        print("POST Proveedor")
        return "Post Proveedor correcto"
    elif request.method == 'PATCH':
        patch_proveedor = proveeddorServices.update_proveedor(proveedor1)
        return "Patch proveedor correcto"
    elif request.method == 'DELETE':
        delete_proveedor = proveeddorServices.delete_proveedor(proveedor1)
        return "Delete proveedor correcto"


    
