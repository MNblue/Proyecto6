from flask import Flask, request, jsonify, json;

#registrar rutas
from .routes import productoRoutes
from .routes import proveedorRoutes
from .routes import productProveeRoutes

app= Flask(__name__)

#pruebaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# @app.before_request
# def before_request():
#     # Establecer el tipo de contenido en application/json si no está establecido
#     if request.method == 'GET' and not request.content_type:
#         request.environ['CONTENT_TYPE'] = 'application/json'

# @app.route('/productProvee/', methods=['GET'])
# def product_provee():
#     data = request.args.get('data')
#     if data is not None:
#         # Decodificar el JSON vacío
#         data_json = json.loads(data)
#         return jsonify({"message": "Received JSON data", "data": data_json})
#     else:
#         return jsonify({"message": "No JSON data received"})

#pruebaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(productoRoutes.main, url_prefix='/producto')
    app.register_blueprint(proveedorRoutes.main,url_prefix='/proveedor')
    app.register_blueprint(productProveeRoutes.main,url_prefix='/productProvee')
    
    return app
