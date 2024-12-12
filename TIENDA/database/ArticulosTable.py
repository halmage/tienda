import sqlite3


class ArticulosTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla 'operaciones' con los campos id, num1, num2, operacion y resultado
        conexion = sqlite3.connect("database/tienda.db")
        try:
            conexion.execute(
                """
                create table Articulos (
                                    id integer primary key autoincrement,
                                    codigo text, 
                                    nombre text,
                                    precio integer,
                                    cantidad integer
                                )"""
            )
        except sqlite3.OperationalError:
            print("La tabla articulos ya existe")
        conexion.close()

    def create(self, resultado):
        # Insertar un nuevo resultado en la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        conexion.execute(
            "insert into Articulos(codigo,nombre,precio,cantidad) values (?,?,?,?)",
            (
                resultado["codigo"],
                resultado["nombre"],
                resultado["precio"],
                resultado["cantidad"],
            ),
        )
        conexion.commit()

    def all(self):
        # Obtener todos los resultados almacenados en la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        res = conexion.execute("SELECT * FROM Articulos")
        return res.fetchall()
        conexion.close()
