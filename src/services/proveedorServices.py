from src.database.db_mysql import get_connection;
from src.models.proveedorModel import proveedor;
from flask import Flask, render_template;

class proveeddorServices():

    @staticmethod
    def format_result_as_html(result):
        html_table = "<table border='1'><tr><th>ID</th><th>Nombre</th><th>Dirección</th><th>Teléfono</th></tr>"
        for row in result:
         html_table += "<tr>"
         for col in row:
            html_table += "<td>{}</td>".format(col)
         html_table += "</tr>"
        html_table += "</table>"
        return html_table


    @classmethod
    def get_proveedor(cls):
        try:
            connection = get_connection()
            print(connection)


            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM proveedor')
                result = cursor.fetchall()
                print(result)
       

            connection.close()


            formatted_html = cls.format_result_as_html(result)
            return (formatted_html)
           
        except Exception as ex:
            print(ex)
    

    @classmethod
    def post_proveedor(cls, proveedor:proveedor):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                id_proveedor = proveedor.id_proveedor
                nameProveedor = proveedor.nombre
                direccionProveedor = proveedor.direccion
                tlfProveedor = proveedor.telefono
               

                cursor.execute("INSERT INTO proveeddor (ID_Proveedor,nombre,direccion, telefono )"+
                           "VALUES ('{0}','{1}','{2}','{3}')".format(id_proveedor,nameProveedor,direccionProveedor,tlfProveedor))
                connection.commit()

            connection.close()
            return 0
        except Exception as ex:
            print(ex)


    @classmethod
    def update_proveedor(cls, proveedor:proveedor):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                id_proveedor = int(proveedor.id_proveedor)
                nameProveedor = proveedor.nombre
                direccionProveedor = proveedor.direccion
                tlfProveedor = proveedor.telefono

                cursor.execute("UPDATE proveedor SET nombre='{1}', direccion='{2}', telefono ='{3}' WHERE ID_Proveedor = {0}".format(id_proveedor,nameProveedor,direccionProveedor,tlfProveedor))                           
                connection.commit()

            connection.close()
            return 0
        except Exception as ex:
            print(ex)


    @classmethod
    def delete_proveedor(cls, proveedor:proveedor):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                id_proveedor = int(proveedor.id_proveedor)
                # nameProveedor = proveedor.nombre
                # direccionProveedor = proveedor.direccion
                # tlfProveedor = proveedor.telefono

                cursor.execute("DELETE FROM proveedor WHERE ID_Proveedor = {0}".format(id_proveedor))                           
                connection.commit()

            connection.close()
            return 0
        except Exception as ex:
            print(ex)

           