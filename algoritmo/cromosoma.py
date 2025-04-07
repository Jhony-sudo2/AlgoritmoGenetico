import random
from typing import List

from algoritmo.datos import *
class Cromosoma:
    def __init__(self):
        self.Genes:Gen = []
        self.puntuacion = 100
        pass

    def GenerarSolucion(self,cursos:List[Curso],docentes:List[Docente],salones:List[Salon]):
        for i in range(len(cursos)):
            curso:int = i
            docente:int = random.randint(0,len(docentes)-1)
            salon:int = random.randint(0,len(salones)-1)
            horario:int = random.randint(0,9)
            gen = Gen(curso,docente,salon,horario)
            self.Genes.append(gen)
            print("Curso: ",cursos[curso].nombre," Docente: ",docentes[docente].nombre," Salon: ",salones[salon].nombre," Horario: ",self.getHorario(horario))
            pass
    def getHorario(self,i:int):
        match i:
            case 0:
                return "1:40-2:30"
            case 1:
                return "2:30-3:20"
            case 2:
                return "3:20-4:10"
            case 3:
                return "4:10-5:00"
            case 4:
                return "5:00-5:50"
            case 5:
                return "5:50-6:40"
            case 6:
                return "6:40-7:30"
            case 7:
                return "7:30-8:20"
            case 8:
                return "8:20-9:10"
            case 9:
                return "9:10-10:00"
            

class Gen:
    def __init__(self,curso:int,docente:int,salon:int,horario:int):
        self.curso:int = curso
        self.docente:int = docente
        self.salon:int = salon
        self.horario:int = horario
        pass