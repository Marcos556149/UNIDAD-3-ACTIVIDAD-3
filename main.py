from ClaseManejadorInscripcion import ManejadorInscripcion
from ClaseManejadorPersona import ManejadorPersona
from ClaseManejadorTalleres import ManejadorTalleres
if __name__=='__main__':
    Talleress= ManejadorTalleres()
    Talleress.leerArchivoTalleres()
    Personas= ManejadorPersona()
    Inscripciones= ManejadorInscripcion(5,5)
    while True:
        print("_____MENU DE OPCIONES_____")
        print("[1]...Inscribir una persona en un taller")
        print("[2]...Consultar inscripcion")
        print("[3]...Consultar inscriptos")
        print("[4]...Registrar pago")
        print("[0]...Salir")
        try:
            op= int(input('Seleccione una opcion: '))
            if op in range(5):
                if op == 1:
                    Talleress.agregarInscripcionEnTaller(Personas,Inscripciones)
                if op == 2:
                    Talleress.buscarPersonaInscripta()
                if op == 3:
                    Talleress.listarAlumnos()
                if op == 4:
                    Talleress.registrarPago()
                if op == 0:
                    print("_____MENU FINALIZADO_____")
                    break
            else:
                print("ERROR, solo puede ingresar numeros del 0 al 5")
        except ValueError:
            print("ERROR, ingrese solamente numeros")
    Talleress.GuardarEnArchivo()





