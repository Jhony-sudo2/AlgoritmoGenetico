
import random
from typing import List
from algoritmo import funcionAptitud
from algoritmo.cromosoma import Cromosoma
from algoritmo.datos import *


class AlgoritmoGenetico:
    def __init__(self,cursos, docentes, salones, asignacionesDocentes):
        self.cursos:List[Curso] = cursos
        self.docentes:List[Docente] = docentes
        self.salones:List[Salon] = salones
        self.asignacione:List[asignacionDocente] = asignacionesDocentes
        self.Cromosomas:Cromosoma = []
        self.NoPoblacion:int = 10
        self.seleccionados:List[Cromosoma] = []
        pass

    def Iniciar(self):
        continuar = True
        while(continuar):
            self.generarPoblacionInicial()
            self.Seleccion()
            self.Cruzamiento()
            self.Mutacion()
            continuar = self.finalizacion()
            pass

    def generarPoblacionInicial(self):
        aptitud = funcionAptitud.funcionAptitud(self.cursos,self.salones,self.docentes,self.asignacione)
        for i in range(self.NoPoblacion):
            # Generar un nuevo cromosoma)
            cromosoma = Cromosoma()
            cromosoma.GenerarSolucion(self.cursos, self.docentes, self.salones)
            self.Cromosomas.append(cromosoma)
            aptitud.calcularAptitud(cromosoma)
            print("Puntuacion: ",cromosoma.puntuacion)
        pass

    def Seleccion(self):
        #SELECCIONANDO POBLACION METODO: seleccion por torneo
        for i in range(int(self.NoPoblacion/2)):
            competidores = random.sample(self.Cromosomas, 2)
            ganador = max(competidores, key=lambda x: x.puntuacion)
            print(f"Torneo: {[c.puntuacion for c in competidores]} -> Ganador: {ganador.puntuacion}")
            self.seleccionados.append(ganador)


    def Cruzamiento(self):
        pass

    def Mutacion(self):
        pass

    def finalizacion(self):
        return False
        

    def saludar(self):
        print("saludando desde el algoritmo genetico")