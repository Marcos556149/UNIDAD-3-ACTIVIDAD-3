from ClaseManejadorInscripcion import ManejadorInscripcion
from ClaseInscripcion import Inscripcion
class TallerCapacitacion:
    __idTaller= 0
    __nombre= ''
    __vacantes= 0
    __montoinscripcion= 0
    __inscripcionPorTaller= None
    def __init__(self, id= 0,nom= '',vac= 0,mon= 0):
        self.__idTaller= id
        self.__nombre= nom
        self.__vacantes= vac
        self.__montoinscripcion= mon
        self.__inscripcionPorTaller= []
    def __str__(self):
        return 'ID: {}, NOMBRE: {}, VACANTES: {}, MONTO: {}'.format(self.__idTaller,self.__nombre,self.__vacantes,self.__montoinscripcion)
    def MostrarAlumnosEnTaller(self):
        for Inscripcion in self.__inscripcionPorTaller:
            print(Inscripcion.getPersona())
    def getID(self):
        return self.__idTaller
    def getVacantes(self):
        return self.__vacantes
    def agregarInscripcion(self,fecha,persona,Inscripciones):
        inscripcionNueva= Inscripcion(persona,self,fecha)
        self.__inscripcionPorTaller.append(inscripcionNueva)
        Inscripciones.agregarInscripcion1(inscripcionNueva)
    def restarVacante(self):
        self.__vacantes -= 1
    def getNombreTaller(self):
        return self.__nombre
    def getMonto(self):
        return self.__montoinscripcion
    def getInscripcionDeTaller(self,indice):
        return self.__inscripcionPorTaller[indice]
    def getTotalInscriptos(self):
        return len(self.__inscripcionPorTaller)
    def buscarDNI(self,dni):
        EstaONo= -1
        m= 0
        while (EstaONo == -1)and(m < len(self.__inscripcionPorTaller)):
            if dni == self.__inscripcionPorTaller[m].getPersona().getDNI():
                EstaONo= m
            m += 1
        return EstaONo



