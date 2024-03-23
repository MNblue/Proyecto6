class DevelopmentConfig():
    DEBUG = True


config={
    'development':DevelopmentConfig
}




# from flask import request, jsonify;

# class DevelopmentConfig:
#     DEBUG = True

#     @staticmethod
#     def init_app(app):
#         @app.after_request
#         def after_request(response):
#             response.headers.add('Content-Type', 'text/html')
#             return response

#         @app.before_request
#         def before_request():
#             if request.method == 'GET' :  
#                 # if request.content_type != 'application/json':
#                     request.headers.add('Content-Type', 'application/json')
                   
#                     # return jsonify({'error': 'Content-Type debeeeeeeeeeee ser application/json'}), 400    
#                     return request

# # @app.route('/', methods=['POST'])
# # def index():
# #     data = request.json
# #     return jsonify({'message': 'Solicitud JSON recibida correctamente', 'data': data})



# from flask import request,jsonify

# class DevelopmentConfig:
#     DEBUG = True

#     @staticmethod
#     def init_app(app):
#         @app.after_request
#         def after_request(response):
#             response.headers.add('Content-Type', 'application/json')
#             request.environ['CONTENT_TYPE'] = 'application/json'
            
#             return response

#         @app.before_request
#         def before_request():
#             request.headers.add("application/json")
#             request.content_type = ("application/json")
#             request.environ['CONTENT_TYPE'] = 'application/json'
          
         
            
#             if request.method == 'GET' and request.content_type != 'application/json':
#                 print("punto A")
#                 return jsonify({'error': 'Content-Type debe ser application/json'}), 400

#             # Permitir todas las solicitudes GET sin verificar el tipo de contenido
#             if request.method == 'GET':
#                 print("punto B")
#                 return "test"









