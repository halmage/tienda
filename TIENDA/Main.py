# Librerias del sistema
from package.Otros import Otros
from database.ArticulosTable import ArticulosTable
from database.PersonasTable import PersonasTable


# Librerias externa
from os import system
import time


class Main:
    def menu(self):
        print("0. Crear base de datos")
        print("1. Salir")
        self.opcion = input("Elija una opcion: ")
        while self.opcion.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def operaciones(self):
        while True:
            self.menu()
            if self.opcion == "1":
                # salida del sistema
                Otros.cargando(self)
                print("Gracias por utilizar nuestro sistema")
                time.sleep(1)
                system("clear")
                break
            elif self.opcion == "0":
                # creacion de base de datos
                persona_table = PersonasTable()
                persona_table.createDatabase()
                articulo_table = ArticulosTable()
                articulo_table.createDatabase()
                Otros.cargando(self)
                print("Base de datos creada correctamente")
                time.sleep(1)
                system("clear")


main = Main()
main.operaciones()
