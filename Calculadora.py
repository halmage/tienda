import time
import os
from Package.Matematica.Operaciones import *


class Calculadora(Operaciones):
    def __init__(self, numero1, numero2, opcion):
        self.numero1 = numero1
        self.numero2 = numero2
        self.opcion = opcion

    def presentacionApertura(self):
        """
        MÉTODO QUE MUESTRA LA PRESENTACIÓN DE LA CALCULADORA
        """
        presentacion = """
        =======================
        |  CALCULADORA MAGICA |
        =======================
        |   [+] [-] [*] [/]   |
        ======================= 
        """
        print(presentacion)
        time.sleep(2)
        os.system("clear")

    def menu(self):
        """
        MÉTODO QUE MUESTRA LA OPCIÓN DE LA CALCULADORA
        """
        opciones = """
        =======================
        |  0) SALIR           |                
        |  1) SUMA            |        
        |  2) RESTA           |        
        |  3) MULTIPLICACION  | 
        |  4) DIVISION        |         
        ======================= 
        """
        print(opciones)
        self.opcion = input("\tINGRESE UNA DE LAS OPCIONES: ")
        while self.opcion.isdigit() == False:
            self.opcion = input("\tINGRESE UNA DE LAS OPCIONES: ")
        os.system("clear")

    def leerDatos(self):
        """
        MÉTODO QUE LEE LOS DATOS DE LA CALCULADORA
        """
        self.numero1 = input("\tINGRESE PRIMER NUMERO: ")
        while self.numero1.isdigit() == False:
            self.numero1 = input("\tINGRESE PRIMER NUMERO: ")
        self.numero2 = input("\tINGRESE SEGUNDO NUMERO: ")
        while self.numero2.isdigit() == False:
            self.numero2 = input("\tINGRESE SEGUNDO NUMERO: ")
        os.system("clear")

    def calculo(self):
        if self.opcion == "0":
            print("\tSE TERMINÓ EL PROGRAMA")
            time.sleep(2)
            os.system("clear")
            exit()
        if self.opcion == "1":
            self.leerDatos()
            print(
                "\tLA SUMA DE",
                self.numero1,
                "+",
                self.numero2,
                "ES:",
                Operaciones.suma(self.numero1, self.numero2),
            )
        elif self.opcion == "2":
            self.leerDatos()
            print(
                "\tLA RESTA DE",
                self.numero1,
                "-",
                self.numero2,
                "ES:",
                Operaciones.resta(self.numero1, self.numero2),
            )
        elif self.opcion == "3":
            self.leerDatos()
            print(
                "\tLA MULTIPLICACION DE",
                self.numero1,
                "*",
                self.numero2,
                "ES:",
                Operaciones.multiplicacion(self.numero1, self.numero2),
            )
        elif self.opcion == "4":
            self.leerDatos()
            if self.numero2 == "0":
                print("\tNO SE PUEDE DIVIDIR POR CERO")
            else:
                print(
                    "\tLA DIVISION DE",
                    self.numero1,
                    "/",
                    self.numero2,
                    "ES:",
                    Operaciones.division(self.numero1, self.numero2),
                )

    def main(self):
        self.presentacionApertura()
        while True:
            self.menu()
            self.calculo()


if __name__ == "__main__":
    Calculadora("", "", "").main()
