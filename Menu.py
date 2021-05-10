from Manejador import claseManejador
class claseMenu:
    __manejador = None

    def __init__(self, manejador=claseManejador()):
        self.__manejador = manejador

    def menu(self, op):
        if (op == 1):  # crear dos objetos para trabajar
            print('|----CREAR OBJETOS----|')
            self.__manejador.crearObj()
            print('DATO: los objetos de han creado')
            input()
        elif (op == 2):  # suma de los dos objetos
            self.__manejador.suma()
            input()
        elif (op == 3):  # resta de los dos objetos
            print('|----OPCIÓN----|\n1. Obj1 - Obj2\n2. Obj2 - Obj1')
            op2 = int(input('Opción: '))
            band = self.__manejador.compGT(1)
            if (op2 == 1):
                if (band == True):
                    self.__manejador.resta(op2)
                else:
                    print('ERROR: Obj1 es menor que Obj2')
            elif (op2 == 2):
                if (band == False):
                    self.__manejador.resta(op2)
                else:
                    print('ERROR: Obj2 es menor que Obj1')
            else:
                print('ERROR: opción inválida')
            input()
        elif (op == 4):  # compara los dos objetos
            print('|----OPCIÓN----|\n1. Obj1 > Obj2\n2. Obj2 > Obj1')
            op2 = int(input('Opción: '))
            if (op2 == 1):
                print(self.__manejador.compGT(op2))
            elif (op2 == 2):
                print(self.__manejador.compGT(op2))
            else:
                print('ERROR: opción inválida')
            input()
        elif (op == 5):  # salir
            print('DATO: finalizando...')
        else:
            print('ERROR: opción inválida')
