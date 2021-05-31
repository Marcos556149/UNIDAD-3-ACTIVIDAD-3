class Persona:
    __nombre= ''
    __direccion= ''
    __dni= ''
    def __init__(self,nomm= '',dir= '',dn= ''):
        self.__nombre= nomm
        self.__direccion= dir
        self.__dni= int(dn)
    def __str__(self):
        return 'Nombre: {}, Direccion: {}, DNI: {}'.format(self.__nombre,self.__direccion,self.__dni)
    def getDNI(self):
        return self.__dni


