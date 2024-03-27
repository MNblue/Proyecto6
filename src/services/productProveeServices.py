from src.database.db_mysql import get_connection;
from src.models.productProveeModel import productProvee;
from flask import Flask, render_template,jsonify,request,json;

class productProveeServices():

    @staticmethod
    def format_result_as_html(result):
        html_table = "<table border='1'><tr><th>ID</th><th>Producto</th><th>Proveedor</th></tr>"
        for row in result:
         html_table += "<tr>"
         for col in row:
            html_table += "<td>{}</td>".format(col)
         html_table += "</tr>"
        html_table += "</table>"
        return html_table


    @classmethod
    def get_productProvee(cls):
        try:
            connection = get_connection()
            print(connection)
            
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM productoproveedor')
                result = cursor.fetchall()
                print(result)
                
            connection.close()

            formatted_html = cls.format_result_as_html(result)
            return formatted_html           
        except Exception as ex:
            print(ex)
            
           

    @classmethod
    def post_productProvee(cls, productProvee:productProvee):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                id_productProveed = productProvee.ID_ProdProvee
                id_producto = productProvee.ID_Producto
                id_proveedor = productProvee.ID_provee
               
                cursor.execute("INSERT INTO productoproveedor (ID_ProdProvee,ID_Producto,ID_Proveedor )"+
                           "VALUES ('{0}','{1}','{2}')".format(id_productProveed,id_producto,id_proveedor))
                connection.commit()

            connection.close()
            return 0
        except Exception as ex:
            print(ex)


    @classmethod
    def update_productProvee(cls, productprovee:productProvee):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                id_productProvee = int(productprovee.ID_ProdProvee)
                id_producto = productprovee.ID_Producto
                id_proveedor = productprovee.ID_provee

                cursor.execute("UPDATE productoproveedor SET ID_ProdProvee='{0}', ID_Producto='{1}', ID_Proveedor ='{2}' WHERE ID_ProdProvee = {0}".format(id_productProvee,id_producto,id_proveedor))                           
                connection.commit()

            connection.close()
            return 0
        except Exception as ex:
            print(ex)


    @classmethod
    def delete_productProvee(cls, productProvee:productProvee):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                id_productoProvee = int(productProvee.ID_ProdProvee)
               
                cursor.execute("DELETE FROM productoproveedor WHERE ID_ProdProvee = '{0}'".format(id_productoProvee))                           
                connection.commit()
                print("cucucucucucu")

            connection.close()
            return 0
        except Exception as ex:
            print("errorrrr delete")
            print(ex)

           