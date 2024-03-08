class Estudiante:
    def __init__(self):
        self.nombre = []
        self.apellido = []
        self.edad = []

    def leerDatosEstudiantes(self):
        for i in range(3):
            self.nombre.append(input("INGRESE NOMBRE DEL ESTUDIANTE: "))
            self.apellido.append(input("INGRESE APELLIDO DEL ESTUDIANTE: "))
            self.edad.append(input("INGRESE EDAD DEL ESTUDIANTE: "))

    def imprimirDatosEstudiantes(self):
        for i in range(3):
            print(self.nombre[i])
            print(self.apellido[i])
            print(self.edad[i])


if __name__ == "__main__":
    estudiante = Estudiante()
    estudiante.leerDatosEstudiantes()
    estudiante.imprimirDatosEstudiantes()
