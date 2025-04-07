from typing import List

from algoritmo.cromosoma import Cromosoma, Gen
from algoritmo.datos import *


class funcionAptitud:
    def __init__(self,cursos,salones,docentes,asignacionesDocentes):
        self.cursos:List[Curso] = cursos
        self.docentes:List[Docente] = docentes
        self.salones:List[Salon] = salones
        self.asignacionesDocentes:List[asignacionDocente] = asignacionesDocentes
        pass

    def calcularAptitud(self,cromosoma:Cromosoma):
        for i in range(len(cromosoma.Genes)):
            gen:Gen = cromosoma.Genes[i]
            
            if self.verificarTraslapeDocente(gen,cromosoma.Genes) == True:
                cromosoma.puntuacion -= 1
            if self.verificarTraslapeSalon(gen,cromosoma.Genes) == True:
                cromosoma.puntuacion -= 1
            if self.verificarDocenteAsignado(gen) == True:
                cromosoma.puntuacion -= 1
            if self.verificarTraslapeSemestre(gen,cromosoma.Genes) == True:
                cromosoma.puntuacion -= 1
            if self.verificarCursoRepetido(gen,cromosoma.Genes) == True:
                cromosoma.puntuacion -= 1
        pass

    def verificarDocenteAsignado(self,gen:Gen):
        for asignacion in self.asignacionesDocentes:
            if asignacion.docente == gen.docente and asignacion.cursos == gen.curso:
                print("EL DOCENTE PUEDE DAR EL CURSO")
                return False
        print("EL DOCENTE NO PUEDE DAR EL CURSO")
        return True
    
    def verificarCursoRepetido(self,gen:Gen,Genes:List[Gen]):
        for otroGen in Genes:
            if otroGen is not gen:
                if otroGen.curso == gen.curso:
                    print("Se detecto un curso repetido: ",otroGen.curso,"==",gen.curso)
                    return True
        return False


    def verificarTraslapeDocente(self,gen:Gen,Genes:List[Gen]):
        for nuevoGen in Genes:
            if nuevoGen is not gen:
                curso = self.cursos[gen.curso]
                cursotmp2 = self.cursos[nuevoGen.curso]
                if nuevoGen.docente == gen.docente and nuevoGen.horario == gen.horario and curso.semestre == cursotmp2.semestre:
                    print("TRASLAPE DOCENTE")
                    return True
        return False
       
    def verificarTraslapeSalon(self,gen:Gen,Genes:List[Gen]):
        for otroGen in Genes:
            if otroGen is not gen:
                if otroGen.salon == gen.salon and otroGen.horario == gen.horario:
                    print("Se detecto un traslape de salon: ",otroGen.salon,"==",gen.salon," y ",otroGen.horario,"==",gen.horario)
                    return True
        return False
    
    def verificarTraslapeSemestre(self,gen:Gen,Genes:List[Gen]):
        curso = self.cursos[gen.curso]
        for otroGen in Genes:
            if otroGen is not gen:
                cursotmp2 = self.cursos[otroGen.curso]
                if cursotmp2.carrera == curso.carrera and otroGen.horario == gen.horario:
                    print("Traslape Semestre: ",cursotmp2.carrera,"==",curso.carrera," y ",otroGen.horario,"==",gen.horario)
                    return True
        return False   
       
        

  