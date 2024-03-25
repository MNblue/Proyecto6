from flask import Flask, request, jsonify, json;

#registrar rutas
from .routes import productoRoutes
from .routes import proveedorRoutes
from .routes import productProveeRoutes

app= Flask(__name__)




def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(productoRoutes.main, url_prefix='/producto')
    app.register_blueprint(proveedorRoutes.main,url_prefix='/proveedor')
    app.register_blueprint(productProveeRoutes.main,url_prefix='/productProvee')
    
    return app
