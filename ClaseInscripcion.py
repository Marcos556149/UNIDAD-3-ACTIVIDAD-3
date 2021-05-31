class Inscripcion:
    __fechaInscripcion= None
    __pago= False
    __persona= None
    __taller= None
    def __init__(self,persona,taller,fecha= None):
        self.__fechaInscripcion= fecha
        self.__pago= False
        self.__persona= persona
        self.__taller= taller
    def getPersona(self):
        return self.__persona
    def getTaller(self):
        return self.__taller
    def getPago(self):
        return self.__pago
    def getFecha(self):
        return self.__fechaInscripcion
    def modificarPago(self):
        self.__pago= True


