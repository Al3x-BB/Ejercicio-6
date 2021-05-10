from FechaHora import claseFechaHora
class claseManejador:
    __obj1 = None   #objeto 1
    __obj2 = None   #objeto 2
    def crearObj(self): #crea los objetos con los que se va a tarabajar
        print('Obj1:')
        d = int(input('Día: '))
        m = int(input('Mes: '))
        a = int(input('Año: '))
        h = int(input('Hora: '))
        mi = int(input('Minutos: '))
        s = int(input('Segundos: '))
        if (d >= 1 and d <= 31):
            if (m >= 1 and m <= 12):
                if (a >= 0):
                    if (h >= 0 and h <= 24):
                        if (mi >= 0 and mi <= 60):
                            if (s >= 0 and s <= 60):
                                self.__obj1 = claseFechaHora(d, m, a, h, mi, s)
                            else:
                                print('ERROR: segundos inválido')
                        else:
                            print('ERROR: minutos inválido')
                    else:
                        print('ERROR: hora inválido')
                else:
                    print('ERROR: año inválido')
            else:
                print('ERROR: mes inválido')
        else:
            print('ERROR: día inválido')
        print('Obj2:')
        d = int(input('Día: '))
        m = int(input('Mes: '))
        a = int(input('Año: '))
        h = int(input('Hora: '))
        mi = int(input('Minutos: '))
        s = int(input('Segundos: '))
        if (d >= 1 and d <= 31):
            if (m >= 1 and m <= 12):
                if (a >= 0):
                    if (h >= 0 and h <= 24):
                        if (mi >= 0 and mi <= 60):
                            if (s >= 0 and s <= 60):
                                self.__obj2 = claseFechaHora(d, m, a, h, mi, s)
                            else:
                                print('ERROR: segundos inválido')
                        else:
                            print('ERROR: minutos inválido')
                    else:
                        print('ERROR: hora inválido')
                else:
                    print('ERROR: año inválido')
            else:
                print('ERROR: mes inválido')
        else:
            print('ERROR: día inválido')
    def suma(self): #suma de los objetos
        suma = self.__obj1 + self.__obj2
        suma.actualizar()
        print(suma)
    def resta(self, op): #resta de los objetos
        if(op == 1):
            resta = self.__obj1 - self.__obj2
        elif(op == 2):
            resta = self.__obj2 - self.__obj1
        print(resta)
    def compGT(self, op):   #comparación de los objetos
        if(op == 1):
            band = self.__obj1 > self.__obj2
        if(op == 2):
            band = self.__obj2 > self.__obj1
        return band
    def mostrar(self):  #mostrar contenido de los objetos
        print(self.__obj1)
        print(self.__obj2)