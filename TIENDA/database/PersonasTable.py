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

    def create(self, datos):
        # Insertar un nuevo datos en la tabla 'personas'
        conexion = sqlite3.connect("database/tienda.db")
        conexion.execute(
            "insert into Personas(cedula,nombre,apellido,telefono) values (?,?,?,?)",
            (
                datos["cedula"],
                datos["nombre"],
                datos["apellido"],
                datos["telefono"],
            ),
        )
        conexion.commit()

    def all(self):
        # Obtener todos los resultados almacenados en la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        res = conexion.execute("SELECT * FROM Personas")
        return res.fetchall()
        conexion.close()

    def find(self, cedula):
        # Obtener todos los resultados almacenados en la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        res = conexion.execute(f"SELECT * FROM Personas WHERE cedula ={cedula}")
        return res.fetchone()
        conexion.close()
