# Librerias del sistema
from package.Otros import Otros
from database.ArticulosTable import ArticulosTable

# Librerias externa
from os import system
import time


class Articulo:

    def create(self):
        # Ingreso de datos del usuario
        anuncio = """
        *********************************
        |INGRESO DE DATOS DE LA ARTICULO|
        *********************************
        """
        print(anuncio)
        codigo = str(input("Codigo:"))
        nombre = str(input("Nombre:"))
        precio = str(input("Precio:"))
        cantidad = str(input("Cantidad:"))
        return {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        }

    def mostrarTodosLosResultados(self):
        # Mostrar todos los resultados guardados en la base de datos
        articulos = ArticulosTable()
        datos = articulos.all()
        if len(datos) == 0:  # No hay registros en la base de datos
            Otros.cargando(self)
            print("No hay resultados registrados.")
        else:  # Muestra todos los registros
            anuncio = """
            **********************
            |ARTICULOS INGRESADOS|
            **********************
            """
            print(anuncio)
            for row in datos:
                print("\n************************")
                print(
                    f"codigo:{row[1]}\nnombre:{row[2]}\nprecio:{row[3]}\ncantidad:{row[4]}"
                )
            while True:
                respuesta = input("Ingrese la letra (s|S) para salir: ")
                if respuesta == "s" or respuesta == "S":
                    Otros.cargando(self)
                    system("clear")
                    break

    def menu(self):
        anuncio = """
        ***********************
        |MENU SECCION ARTICULO|
        ***********************
        """
        print(anuncio)
        print("1. Ingreso de datos del articulo")
        print("2. Visualizar datos de los articulos")
        print("3. Salir")
        self.opcion = input("Elija una opcion: ")
        while self.opcion.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def operaciones(self):
        while True:
            self.menu()
            if self.opcion == "3":
                # salida del sistema
                Otros.cargando(self)
                print("Saliendo de la seccion articulo")
                time.sleep(1)
                system("clear")
                break
            elif self.opcion == "1":
                system("clear")
                datos = self.create()
                articulo = ArticulosTable()
                articulo.create(datos)
                Otros.cargando(self)
                print("Datos ingresados correctamente")
                time.sleep(1)
                system("clear")
            elif self.opcion == "2":
                system("clear")
                self.mostrarTodosLosResultados()
