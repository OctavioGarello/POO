import os
from controlador import Controlador

class Menu:
    __opcion: int
    __control: Controlador
    def __init__(self):
        self.__opcion=0
        self.__control=Controlador()

    def getMenu(self):
        centinela=0
        while(centinela!=None):
            self.__opcion=int(input("""
                    #Menu
Opcion >>[1] Mostrar Conjuntos
Opcion >>[2] Union de dos Conjuntos
Opcion >>[3] La diferencia de dos Conjuntos
Opcion >>[4] Verificar si los dos Conjuntos son Iguales
Opcion >>[0] Finalizar
            
Ingrese Opcion--> """))

            if self.__opcion==1:
                os.system("cls")
                self.__control.mostrar()

            if self.__opcion==2:
                os.system("cls")
                self.__control.union()

            if self.__opcion==3:
                os.system("cls")
                self.__control.diferencia()

            if self.__opcion==4:
                os.system("cls")
                self.__control.verificacion()

            if self.__opcion==0:
                os.system("cls")
                print("\n**Fin del Programa**")
                centinela=None

        




