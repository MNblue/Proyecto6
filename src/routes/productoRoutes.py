from flask import Blueprint, request, render_template
from src.services.productoServices import productoServices
from src.models.productoModel import producto;

main = Blueprint('producto_blueprint',__name__)

@main.route('/',methods=['GET','POST', 'PATCH','DELETE'])

def get_producto():

    print(request)
    print(request.method)


    #........................................solo se hace cuando NO sea get .............
    if request.method != 'GET':

        print(request.json)
        id_product = request.json["id_producto"]    
        name = request.json["nombre"]
        descript = request.json["descripcion"]
        marca = request.json["marca"]
        precio = request.json["precio"]
        stock = request.json["stock"]
        
        product = producto(id_product,name,descript,marca,precio,stock)

# ......................................................................................................



    if request.method == 'GET':
        get_product= productoServices.get_product()
        print('GET productoooo')
        # return get_product
        return render_template("index.html",tabla = get_product)
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

    
