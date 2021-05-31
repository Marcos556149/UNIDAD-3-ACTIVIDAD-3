from ClasePersona import Persona
class ManejadorPersona:
    __listaPersonas= []
    def __init__(self):
        self.__listaPersonas= []
    def MostrarPersonas(self):
        for Persona in self.__listaPersonas:
            print(Persona)
    def agregarPersona(self,personaa):
        self.__listaPersonas.append(personaa)
    def buscarDNI1(self,dni):
        bandera= False
        m=0
        while (bandera == False)and(m < len(self.__listaPersonas)):
            if dni == self.__listaPersonas[m].getDNI():
                bandera= True
            m += 1
        return bandera

