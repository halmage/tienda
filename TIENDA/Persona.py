# Librerias del sistema
from package.Otros import Otros
from database.PersonasTable import PersonasTable

# Librerias externa
from os import system
import time


class Persona:

    def create(self):
        # Ingreso de datos del usuario
        anuncio = """
        ********************************
        |INGRESO DE DATOS DE LA PERSONA|
        ********************************
        """
        print(anuncio)
        cedula = str(input("cedula:"))
        nombre = str(input("Nombre:"))
        apellido = str(input("Apellido:"))
        telefono = str(input("Telefono:"))
        return {
            "cedula": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
        }

    def find(self):
        # Mostrar los datos de la persona
        anuncio = """
        *********************
        |DATOS DE LA PERSONA|
        *********************
        """
        print(anuncio)
        persona = PersonasTable()
        cedula = input("Ingrese cedula:")
        print("****************")
        datos = persona.find(cedula)
        if datos == None:  # No hay registros en la base de datos
            Otros.cargando(self)
            print("No hay resultados registrados.")
            while True:
                respuesta = input("Ingrese la letra (s|S) para salir: ")
                if respuesta == "s" or respuesta == "S":
                    Otros.cargando(self)
                    system("clear")
                    break
        else:  # Muestra todos los registros
            print(
                f"cedula:{datos[1]}\nnombre:{datos[2]}\napellido:{datos[3]}\ntelefono:{datos[4]}"
            )
            while True:
                respuesta = input("Ingrese la letra (s|S) para salir: ")
                if respuesta == "s" or respuesta == "S":
                    Otros.cargando(self)
                    system("clear")
                    break

    def all(self):
        # Mostrar todos los resultados guardados en la base de datos
        personas = PersonasTable()
        datos = personas.all()
        if len(datos) == 0:  # No hay registros en la base de datos
            Otros.cargando(self)
            print("No hay resultados registrados.")
        else:  # Muestra todos los registros
            anuncio = """
            *********************
            |PERSONAS INGRESADAS|
            *********************
            """
            print(anuncio)
            for row in datos:
                print("\n************************")
                print(
                    f"cedula:{row[1]}\nnombre:{row[2]}\napellido:{row[3]}\ntelefono:{row[4]}"
                )
            while True:
                respuesta = input("Ingrese la letra (s|S) para salir: ")
                if respuesta == "s" or respuesta == "S":
                    Otros.cargando(self)
                    system("clear")
                    break

    def menu(self):
        anuncio = """
        **********************
        |MENU SECCION PERSONA|
        **********************
        """
        print(anuncio)
        print("1. Ingreso de datos del usuario")
        print("2. Buscar persona")
        print("3. Visualizar datos de las personas")
        print("4. Salir")
        self.opcion = input("Elija una opcion: ")
        while self.opcion.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def operaciones(self):
        while True:
            self.menu()
            if self.opcion == "4":
                # salida del sistema
                Otros.cargando(self)
                print("Saliendo de la seccion persona")
                time.sleep(1)
                system("clear")
                break
            elif self.opcion == "1":
                system("clear")
                datos = self.create()
                persona_table = PersonasTable()
                persona_table.create(datos)
                Otros.cargando(self)
                print("Datos ingresados correctamente")
                time.sleep(1)
                system("clear")
            elif self.opcion == "2":
                system("clear")
                self.find()
            elif self.opcion == "3":
                system("clear")
                self.all()
