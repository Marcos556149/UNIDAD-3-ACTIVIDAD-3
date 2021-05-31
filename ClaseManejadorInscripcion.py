import numpy as np
from ClaseInscripcion import Inscripcion
class ManejadorInscripcion:
    __Inscripcioness= None
    __cantidad= 0
    __dimension=0
    __incremento= 5
    def __init__(self,dim,inc= 5):
        self.__Inscripcioness= np.empty(dim,dtype= Inscripcion)
        self.__cantidad= 0
        self.__dimension= dim
        self.__incremento= inc
    def agregarInscripcion1(self,inscripcionNueva):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Inscripcioness.resize(self.__dimension)
        self.__Inscripcioness[self.__cantidad] = inscripcionNueva
        self.__cantidad += 1


