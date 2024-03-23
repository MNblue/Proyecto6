from flask import Blueprint, request
from src.services.productoServices import productoServices
from src.models.productoModel import producto;

main = Blueprint('producto_blueprint',__name__)

@main.route('/',methods=['GET','POST', 'PATCH','DELETE'])

def get_producto():

    print(request)
    print(request.method)
    print(request.json)

    name = request.json["nombre"]
    descript = request.json["descripcion"]
    marca = request.json["marca"]
    precio = request.json["precio"]
    stock = request.json["stock"]

    id_product = request.json["id_producto"]

    # product = producto(0,name,descript,marca,precio,stock)
    product = producto(id_product,name,descript,marca,precio,stock)


    if request.method == 'GET':
        get_product= productoServices.get_product()
        print('GET productoooo')
        return get_product
    elif request.method == 'POST':
        get_product = productoServices.post_product(product)
        print("POST Productoooooo")
        return("resultadooooo")
    elif request.method == 'PATCH':
        get_product = productoServices.update_product(product)
        return("resultadooooo")
    elif request.method == 'DELETE':
        get_product = productoServices.delete_product(product)
        return("resultadooooo")


    # return get_product
    