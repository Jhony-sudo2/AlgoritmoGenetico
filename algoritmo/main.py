
import random
import time
import tracemalloc
from typing import List
from algoritmo.cromosoma import Cromosoma, Gen
from algoritmo.datos import *
from algoritmo.Archivos import *
import matplotlib.pyplot as plt

class AlgoritmoGenetico:
    def __init__(self,cursos, docentes, salones,asignacionesManuales,NoPoblacion,generacionesMaxima):
        self.cursos:List[Curso] = cursos
        self.docentes:List[Docente] = docentes
        self.salones:List[Salon] = salones
        self.asignacionesManuales = asignacionesManuales
        self.Cromosomas:Cromosoma = []
        self.NoPoblacion:int = NoPoblacion
        self.seleccionados:List[Cromosoma] = []
        self.poblacionesFinales:List[Cromosoma] = []
        self.generacionesMaxima = generacionesMaxima
        self.opcionMejor:Cromosoma
        self.promedios = []
        self.generaciones = []
        self.estadisticas:Estadisticas = Estadisticas()
        self.estadisticas.Iteraciones = self.generacionesMaxima

    def Iniciar(self):
        inicio_tiempo = time.perf_counter()
        tracemalloc.start()
        continuar = True
        self.generarPoblacionInicial()
        while continuar:
            self.Seleccion()
            self.Cruzamiento()
            self.Mutacion()
            continuar = self.finalizacion()
        self.mejorOpcion()
        self.graficar()
        
        fin_tiempo = time.perf_counter()
        tiempo_ejecucion = fin_tiempo - inicio_tiempo
        memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        memoria_pico_mb = memoria_pico / (1024 * 1024)  # Convertir de bytes a MB
        self.estadisticas.espacioMemoria = memoria_pico_mb
        self.estadisticas.TiempoEjecucion = tiempo_ejecucion
        crerPdf("horario.pdf", self.opcionMejor, self.cursos, self.docentes, self.salones)
        crearPDFEstadisticas(self.estadisticas)
        crearCSV("horario.csv", self.opcionMejor, self.cursos, self.docentes, self.salones)
        return self.opcionMejor

    def generarPoblacionInicial(self):
        for i in range(self.NoPoblacion):
            # Generar un nuevo cromosoma)
            cromosoma = Cromosoma()
            cromosoma.GenerarSolucion(self.cursos, self.docentes, self.salones,self.asignacionesManuales,self.estadisticas)
            self.Cromosomas.append(cromosoma)
        pass

    def Seleccion(self):
        #SELECCIONANDO POBLACION METODO: seleccion por torneo

        if self.seleccionados:
            self.Cromosomas = []
            self.Cromosomas = self.seleccionados
            self.seleccionados = []
        for i in range(int(self.NoPoblacion/2)):
            competidores = random.sample(self.Cromosomas, 2)
            ganador = max(competidores, key=lambda x: x.puntuacion)
            self.seleccionados.append(ganador)

    def Cruzamiento(self):
        #Cruzamiento metodo: cruce multipunto  con 2 puntos de cruce.
        for i in range(0, len(self.seleccionados), 2):
            padre1 = self.seleccionados[i]
            padre2 = self.seleccionados[i + 1] if i + 1 < len(self.seleccionados) else self.seleccionados[0]
            hijo1, hijo2 = self.cruce_multipunto(padre1, padre2)
            self.seleccionados.append(hijo1)
            self.seleccionados.append(hijo2)
        pass

    def cruce_multipunto(self, padre1: Cromosoma, padre2: Cromosoma) -> tuple[Cromosoma, Cromosoma]:
        hijo1 = Cromosoma()
        hijo2 = Cromosoma()
        puntos = sorted(random.sample(range(len(padre1.Genes)), 2))  
    
        for i in range(len(padre1.Genes)):
            if i < puntos[0] or i >= puntos[1]:
                hijo1.Genes.append(Gen(padre1.Genes[i].curso, padre1.Genes[i].docente,
                                      padre1.Genes[i].salon, padre1.Genes[i].horario))
                hijo2.Genes.append(Gen(padre2.Genes[i].curso, padre2.Genes[i].docente,
                                      padre2.Genes[i].salon, padre2.Genes[i].horario))
            else:
                hijo1.Genes.append(Gen(padre2.Genes[i].curso, padre2.Genes[i].docente,
                                      padre2.Genes[i].salon, padre2.Genes[i].horario))
                hijo2.Genes.append(Gen(padre1.Genes[i].curso, padre1.Genes[i].docente,
                                  padre1.Genes[i].salon, padre1.Genes[i].horario))
    
        hijo1.calcularPuntuacion(self.cursos, self.docentes, self.salones,self.estadisticas)
        hijo2.calcularPuntuacion(self.cursos, self.docentes, self.salones,self.estadisticas)
        return hijo1, hijo2
    

    def Mutacion(self):
        for cromosoma in self.seleccionados:
            cromosoma.mutacion_random_resetting(self.cursos, self.docentes, self.salones,self.estadisticas)
        pass
    
    
    def finalizacion(self):
        #print("generacion: ",self.generacionesMaxima)
        #for gen in self.seleccionados:
        #    print("Puntuacion: ",gen.puntuacion," Promedio solucion: " + str(self.promedioPoblacion(self.seleccionados)))
            #print("Puntuacion promedio: ",self.promedioPoblacion(self.seleccionados))

        promediotmp = self.promedioPoblacion(self.seleccionados)
        self.poblacionesFinales.append(self.seleccionados)
        self.promedios.append(promediotmp)
        self.generaciones.append(len(self.promedios))
        self.generacionesMaxima -=1
        if(self.generacionesMaxima <= 0 ):
            return False
        else:
            return True
    
    def mejorOpcion(self):
        puntuacion = -100000
        for tmp in self.poblacionesFinales:
            for tmp2 in tmp:
                if(tmp2.puntuacion > puntuacion):
                    puntuacion = tmp2.puntuacion
                    self.opcionMejor = tmp2
        print("mejor opcion",self.opcionMejor.puntuacion)
        
    def promedioPoblacion(self,cromosomas:List[Cromosoma]):
        puntuacion = 0
        for tmp in cromosomas:
            puntuacion += tmp.puntuacion
        promedio = puntuacion/len(cromosomas)
        return promedio

    def graficar(self):
        plt.plot(self.generaciones,self.promedios)
        plt.title("Funcion aptitud x=numero de generaciones, y = valor de aptitud")
        plt.show()