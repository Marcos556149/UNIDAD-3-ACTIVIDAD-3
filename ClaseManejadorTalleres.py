import csv
import numpy as np
from ClasePersona import Persona
from ClaseManejadorInscripcion import ManejadorInscripcion
from ClaseTallerCapacitacion import TallerCapacitacion
class ManejadorTalleres:
    __cantidadTalleres= None
    def __init__(self):
        self.__cantidadTalleres= None
    def leerArchivoTalleres(self):
        archivo= open('Talleres.csv')
        reader= csv.reader(archivo,delimiter=',')
        bandera= True
        i= 0
        for fila in reader:
            if bandera:
                self.__cantidadTalleres= np.empty(int(fila[0]),dtype= TallerCapacitacion)
                bandera= not bandera
            else:
                id= int(fila[0])
                nom= fila[1]
                vac= int(fila[2])
                mon= fila[3]
                nuevoTaller= TallerCapacitacion(id,nom,vac,mon)
                self.__cantidadTalleres[i]= nuevoTaller
                i += 1
        archivo.close()
    def buscarID(self,id1):
        comprobar= -1
        i=0
        while(comprobar == -1)and(i < len(self.__cantidadTalleres)):
            if id1 == self.__cantidadTalleres[i].getID():
                comprobar= i
                if self.__cantidadTalleres[i].getVacantes() == 0:
                    comprobar= -2
            i += 1
        return comprobar
    def buscarPersonaInscripta(self):
        dni= int(input('Ingrese el DNI de la persona: '))
        n= 0
        bandera= False
        while (bandera == False)and(n < len(self.__cantidadTalleres)):
            indice= self.__cantidadTalleres[n].buscarDNI(dni)
            if indice != -1:
                bandera = True
                print("El taller en el que se inscribio es: {}".format(self.__cantidadTalleres[n].getNombreTaller()))
                if self.__cantidadTalleres[n].getInscripcionDeTaller(indice).getPago():
                    print("La monto que la persona adeuda es: $0")
                else:
                    print("El monto que la persona adeuda es: ${}".format(self.__cantidadTalleres[n].getMonto()))
            n += 1
        if bandera == False:
            print("El DNI ingresado no corresponde con ninguna persona inscripta")
    def agregarInscripcionEnTaller(self,Personas,Inscripciones):
        id1= int(input('Ingrese la id del taller: '))
        indice= self.buscarID(id1)
        if indice >= 0:
            nomm= input('Ingrese el nombre de la persona: ')
            dir= input('Ingrese la direccion de la persona: ')
            dn= input('Ingrese el DNI de la persona: ')
            if Personas.buscarDNI1(dn) == False:
                personaa= Persona(nomm,dir,dn)
                fecha= input('Ingrese la fecha de la inscripcion: ')
                self.__cantidadTalleres[indice].agregarInscripcion(fecha,personaa,Inscripciones)
                self.__cantidadTalleres[indice].restarVacante()
                Personas.agregarPersona(personaa)
            else:
                print("El DNI ingresado ya corresponde a una persona inscripta en un taller, solo puede inscribirse en un taller")
        elif indice == -1:
            print("La ID ingresada no corresponde a ningun taller")
        else:
            print("El taller con ID {} no posee vacantes".format(id1))
    def listarAlumnos(self):
        idd= int(input('Ingrese el identificador de un taller: '))
        k= 0
        bandera= False
        while (bandera == False)and(k < len(self.__cantidadTalleres)):
            if idd == self.__cantidadTalleres[k].getID():
                if self.__cantidadTalleres[k].getTotalInscriptos() > 0:
                    print("LISTADO DE ALUMNOS QUE SE INSCRIBIERON EN EL TALLER CON ID {}".format(idd))
                    bandera= True
                    self.__cantidadTalleres[k].MostrarAlumnosEnTaller()
                else:
                    print("NINGUNA PERSONA SE INSCRIBIO EN EL TALLER CON ID {}".format(idd))
                    bandera= True
            k += 1
        if bandera == False:
            print("La ID ingresada no corresponde con ningun taller")
    def registrarPago(self):
        dnii= int(input('Ingrese el DNI de la persona: '))
        bandera= False
        g= 0
        while (bandera == False)and(g < len(self.__cantidadTalleres)):
            indice= self.__cantidadTalleres[g].buscarDNI(dnii)
            if indice != -1:
                bandera= True
                if self.__cantidadTalleres[g].getInscripcionDeTaller(indice).getPago() == False:
                    self.__cantidadTalleres[g].getInscripcionDeTaller(indice).modificarPago()
                    print("PAGO REALIZADO CON EXITO")
                else:
                    print("La persona ya registro el pago previamente")
            g += 1
        if bandera == False:
            print("El DNI ingresado no corresponde con ninguna persona inscripta")
    def GuardarEnArchivo(self):
        with open('Inscripciones.csv','w',newline='') as archivo2:
            writer= csv.writer(archivo2,delimiter=',')
            for TallerCapacitacion in self.__cantidadTalleres:
                for i in range(TallerCapacitacion.getTotalInscriptos()):
                    writer.writerow([TallerCapacitacion.getInscripcionDeTaller(i).getPersona().getDNI(),
                                     TallerCapacitacion.getInscripcionDeTaller(i).getTaller().getID(),
                                     TallerCapacitacion.getInscripcionDeTaller(i).getFecha(),
                                     TallerCapacitacion.getInscripcionDeTaller(i).getPago()])
            archivo2.close()
        print("ARCHIVO CREADO EXITOSAMENTE")











