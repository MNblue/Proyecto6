from src.database.db_mysql import get_connection;
from src.models.productoModel import producto;
from flask import Flask, render_template;

class productoServices():

    @staticmethod
    def format_result_as_html(result):
        html_table = "<table border='1'><tr><th>ID</th><th>Nombre</th><th>Descripción</th><th>marca</th><th>Precio</th><th>Cantidad</th></tr>"
        for row in result:
         html_table += "<tr>"
         for col in row:
            html_table += "<td>{}</td>".format(col)
         html_table += "</tr>"
        html_table += "</table>"
        return html_table


    @classmethod
    def get_product(cls):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM producto')
                result = cursor.fetchall()
                print(result)
       
            connection.close()

            formatted_html = cls.format_result_as_html(result)
            return (formatted_html)
           
        except Exception as ex:
            print(ex)
    

    @classmethod
    def post_product(cls, product:producto):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                id_product = product.id_producto
                nameProduct = product.nombre
                marcaProduct = product.marca
                descriptProduct = product.descripcion
                precioProduct = product.precio
                stockProduct = product.stock

                cursor.execute("INSERT INTO producto (ID_Producto,nombre,descripcion, marca, precio, stock )"+
                           "VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(id_product,nameProduct,descriptProduct, marcaProduct, precioProduct, stockProduct))
                connection.commit()

            connection.close()
            return 0
        except Exception as ex:
            print(ex)


    @classmethod
    def update_product(cls, product:producto):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                id_product = int(product.id_producto)
                nameProduct = product.nombre
                marcaProduct = product.marca
                descriptProduct = product.descripcion
                precioProduct = product.precio
                stockProduct = product.stock

                cursor.execute("UPDATE producto SET nombre='{1}', descripcion='{2}', marca ='{3}',precio={4},stock={5} WHERE ID_Producto = {0}".format(id_product,nameProduct,descriptProduct,marcaProduct,precioProduct,stockProduct))                           
                connection.commit()

            connection.close()
            return 0
        except Exception as ex:
            print(ex)


    @classmethod
    def delete_product(cls, product:producto):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                id_product = int(product.id_producto)
                nameProduct = product.nombre
                marcaProduct = product.marca
                descriptProduct = product.descripcion
                precioProduct = product.precio
                stockProduct = product.stock

                cursor.execute("DELETE FROM producto WHERE ID_Producto = {0}".format(id_product))                           
                connection.commit()

            connection.close()
            return 0
        except Exception as ex:
            print(ex)

           