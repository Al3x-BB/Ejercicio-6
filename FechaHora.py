class claseFechaHora:
    __d = 0     #dia
    __m = 0     #mes
    __a = 0     #año
    __h = 0     #hora
    __mi = 0    #minutos
    __s = 0     #segundos
    def __init__(self, dia = 1, mes = 1, año = 2020, hora = 0, min = 0, seg = 0):
        self.__d = dia
        self.__m = mes
        self.__a = año
        self.__h = hora
        self.__mi = min
        self.__s = seg
    def __str__(self):
        cadena = """\
                +--------------------------+
                | {:2}/{:2}/{:4} ---- {:2}:{:2}:{:2} |
                +--------------------------+\
                """
        return cadena.format(self.__d, self.__m, self.__a, self.__h, self.__mi, self.__s)
    def PonerEnHora(self, h = 0, m = 0, s = 0):
        self.__h = h
        self.__mi = m
        self.__s = s
    def AdelantarHora(self, h = 0, m = 0, s = 0):
        self.__h += h
        self.__mi += m
        self.__s += s
    def actualizar(self):
        band = False    #indica si el año es bisiesto
        if (self.__a % 100 == 0):  # verifica que el año sea bisiesto
            if (self.__a % 400 == 0):
                band = True
        elif (self.__a % 4 == 0):
            band = True
        if (self.__s >= 60):
            self.__mi += 1
            self.__s -= 60
        if (self.__mi >= 60):
            self.__h += 1
            self.__mi -= 60
        if (self.__h >= 24):
            self.__d += 1
            self.__h -= 24
        if (band == True and self.__m == 2 and self.__d > 29):
            self.__m += 1
            self.__d -= 29
        elif (self.__m == 2 and self.__d >= 28):
            self.__m += 1
            self.__d -= 28
        if ((self.__m == 1 or self.__m == 3 or self.__m == 5 or self.__m == 7 or self.__m == 8 or self.__m == 10 or
                self.__m == 12) and self.__d > 31):
            self.__m += 1
            self.__d -= 31
        if ((self.__m == 4 or self.__m == 6 or self.__m == 9 or self.__m == 11) and self.__d < 30):
            self.__m += 1
            self.__d -= 30
        if (self.__m > 12):
            self.__a += 1
            self.__m -= 12
    def getDia(self):   #retorna día
        return self.__d
    def getMes(self):   #retorna mes
        return self.__m
    def getAno(self):   #retorna año
        return self.__a
    def getHr(self):    #retorna hora
        return self.__h
    def getMin(self):   #retorna minutos
        return self.__mi
    def getSeg(self):   #retorna segundos
        return self.__s
    def __add__(self, other):   #suma
        return claseFechaHora(self.__d + other.getDia(), self.__m + other.getMes(), self.__a + other.getAno(),
                              self.__h + other.getHr(), self.__mi + other.getMin(), self.__s + other.getSeg())
    def __sub__(self, other):   #resta  MODIFICAR
        band = False  # indica si el año es bisiesto
        if (self.__a % 100 == 0):  # verifica que el año sea bisiesto
            if (self.__a % 400 == 0):
                band = True
        elif (self.__a % 4 == 0):
            band = True
        #resta
        seg = self.__s - other.getSeg()
        if(seg < 0):    #si los segundos son negativos, se pide un minuto
            self.__m-=1
            seg+=60
        min = self.__mi - other.getMin()
        if(min < 0):    #si los minutos son negativos, se pide una hora
            self.__h-=1
            min+=60
        hr = self.__h - other.getHr()
        if(hr < 0):     #si las horas son negativas, se pide un día
            self.__d-=1
            hr+=24
        dia = self.__d - other.getDia()
        if(dia < 0):    #si los días son negativos, se pide un mes
            self.__m-=1
            #como en los meses hay diferentes cantidad de días según el mes
            if (self.__m == 1 or self.__m == 3 or self.__m == 5 or self.__m == 7 or self.__m == 8 or self.__m == 10 or
                 self.__m == 12):
                self.__d+=31    #se sumará 31 días
            if (self.__m == 4 or self.__m == 6 or self.__m == 9 or self.__m == 11):
                self.__d+=30    #se sumará 30 días
            if(band == True):   #si el año es bisiesto
                if(self.__m == 2):
                  self.__d+=29  #se sumará 29 días
            else:   #si el año no es bisiesto
                if (self.__m == 2):
                    self.__d+=28  #se sumará 28 días
        mes = self.__m - other.getMes()
        if(mes < 0):
            self.__a-=1
            mes+=12
        ano = self.__a - other.getAno()
        return claseFechaHora(dia, mes, ano, hr, min, seg)
    def __gt__(self, other):    #comparación (mayor que)
        op = False
        if(self.__a > other.getAno()):
            op = True
        elif(self.__a == other.getAno()):
            if(self.__m > other.getMes()):
                op = True
            elif(self.__m == other.getMes()):
                if(self.__d > other.getDia()):
                    op = True
                elif(self.__d == other.getDia()):
                    if(self.__h > other.getHr()):
                        op = True
                    elif(self.__h == other.getHr()):
                        if(self.__mi > other.getMin()):
                            op = True
                        elif(self.__mi == other.getMin()):
                            if(self.__s > other.getSeg()):
                                op = True
                            elif(self.__s == other.getSeg()):
                                op = None
        return op