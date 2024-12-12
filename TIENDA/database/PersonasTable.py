import sqlite3


class PersonasTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla 'operaciones' con los campos id, num1, num2, operacion y resultado
        conexion = sqlite3.connect("database/tienda.db")
        try:
            conexion.execute(
                """
                create table Personas (
                                    id integer primary key autoincrement,
                                    cedula text, 
                                    nombre text,
                                    apellido text,
                                    telefono text
                                )"""
            )
        except sqlite3.OperationalError:
            print("La tabla persona ya existe")
        conexion.close()

    def create(self, resultado):
        # Insertar un nuevo resultado en la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        conexion.execute(
            "insert into Personas(cedula,nombre,apellido,telefono) values (?,?,?,?)",
            (
                resultado["cedula"],
                resultado["nombre"],
                resultado["apellido"],
                resultado["telefono"],
            ),
        )
        conexion.commit()

    def all(self):
        # Obtener todos los resultados almacenados en la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        res = conexion.execute("SELECT * FROM Personas")
        return res.fetchall()
        conexion.close()
