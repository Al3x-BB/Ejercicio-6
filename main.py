from Menu import claseMenu
from Manejador import claseManejador
import os
def test():
    manejador = claseManejador()
    manejador.crearObj()
    manejador.mostrar()
    manejador.suma()
    manejador.compGT()
if __name__ == '__main__':
    if(input('¿Testear?: ').lower() == 'si'):
        test()
    else:
        #variables
        band = False
        #inicializando varibales
        menu = claseMenu()
        #tareas
        menu.menu(1)
        os.system('cls')
        while not band:
            print('|----MENU----|\n1. Suma\n2. Resta\n3. Comparación\n4. Salir')
            op = int(input('Opción: '))
            os.system('cls')
            menu.menu(op+1)
            ban = op == 4