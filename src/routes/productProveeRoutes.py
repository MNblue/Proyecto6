from flask import Blueprint, request, jsonify, json
from src.services.productProveeServices import productProveeServices
from src.models.productProveeModel  import productProvee;

main = Blueprint('productProvee_blueprint',__name__)

@main.route('/',methods=['GET','POST', 'PATCH','DELETE'])

def get_productProvee():

    print(request)
    print(request.method)

    print(request.content_type)

    if request.method != 'GET':

        print(request.json)
        id_productProvee = request.json["ID_ProdProvee"]
        id_producto = request.json["ID_Producto"]
        id_provee = request.json["ID_Proveedor"]
        productProvee1 = productProvee(id_productProvee,id_producto,id_provee)

   
    if request.method == 'GET':
        get_productProvee = productProveeServices.get_productProvee()
        print('GET proveedorrrrrr')
        return get_productProvee
    elif request.method == 'POST':
        post_productProvee = productProveeServices.post_productProvee(productProvee1)
        print("POST Proveedor")
        return "resultado proveedor post"
    elif request.method == 'PATCH':
        get_productProvee = productProveeServices.update_productProvee(productProvee1)
        return "resultado provee patch"
    elif request.method == 'DELETE':
        get_productProvee = productProveeServices.delete_productProvee(productProvee1)
        return "delete resultadoooo"


    
