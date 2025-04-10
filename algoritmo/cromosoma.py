import random
from typing import List

from algoritmo.datos import *
class Cromosoma:
    HORARIOS = [
        "1:40-2:30", "2:30-3:20", "3:20-4:10", "4:10-5:00", "5:00-5:50",
        "5:50-6:40", "6:40-7:30", "7:30-8:20", "8:20-9:10", "9:10-10:00"
    ]
    HORARIOS_TIEMPO = [(datetime.strptime(h.split("-")[0], "%H:%M"), 
                       datetime.strptime(h.split("-")[1], "%H:%M")) 
                      for h in HORARIOS]

    def __init__(self):
        self.Genes: List[Gen] = []
        self.puntuacion = 100

    def GenerarSolucion(self, cursos: List[Curso], docentes: List[Docente], salones: List[Salon]):
        for i, curso in enumerate(cursos):
            # Elegir docente disponible para este curso
            docentes_posibles = [j for j, d in enumerate(docentes) if i in d.cursos_posibles]
            if not docentes_posibles:
                raise ValueError(f"No hay docentes disponibles para {curso.nombre}")
            docente = random.choice(docentes_posibles)
            salon = random.randint(0, len(salones) - 1)
            horario = random.randint(0, 9)
            gen = Gen(i, docente, salon, horario)
            self.Genes.append(gen)
            #print("Curso: ", curso.nombre, "Docente: ", docentes[docente].nombre, "Salon: ", salones[salon].nombre, "Horario: ", self.HORARIOS[horario])
        self.calcularPuntuacion(cursos, docentes, salones)

    def calcularPuntuacion(self, cursos: List[Curso], docentes: List[Docente], salones: List[Salon]):
        horarios_docentes = {}
        horarios_cursos_obligatorios = {}
        horarios_salones = {}  
        for gen in self.Genes:
            curso = cursos[gen.curso]
            docente = docentes[gen.docente]
            inicio, fin = self.HORARIOS_TIEMPO[gen.horario]
            
            # Verificacion Disponibilidad del docente
            if inicio < docente.horaEntrada or fin > docente.horaSalida:
                self.puntuacion -= 10
            
            # Verificar traslape docente
            if gen.docente in horarios_docentes:
                if gen.horario in horarios_docentes[gen.docente]:
                    self.puntuacion -= 10
                else:
                    horarios_docentes[gen.docente].append(gen.horario)
            else:
                horarios_docentes[gen.docente] = [gen.horario]
            #validacion traslape de salones
            if gen.salon in horarios_salones:
                if gen.horario in horarios_salones[gen.salon]:
                    self.puntuacion -= 10
                else:
                    horarios_salones[gen.salon].append(gen.horario)
            else:
                horarios_salones[gen.salon] = [gen.horario]
            
            # verificacion traslpae del mismo semestre carrera
            if curso.tipo == "Obligatorio":
                key = (curso.carrera, curso.semestre)
                if key in horarios_cursos_obligatorios:
                    if gen.horario in horarios_cursos_obligatorios[key]:
                        self.puntuacion -= 10
                    else:
                        horarios_cursos_obligatorios[key].append(gen.horario)
                else:
                    horarios_cursos_obligatorios[key] = [gen.horario]
        
        #continuidad de semestre
        for carrera in set(c.carrera for c in cursos):
            for semestre in set(c.semestre for c in cursos if c.carrera == carrera):
                horarios = sorted([g.horario for g in self.Genes 
                                 if cursos[g.curso].carrera == carrera and 
                                 cursos[g.curso].semestre == semestre])
                for i in range(len(horarios) - 1):
                    if horarios[i + 1] == horarios[i] + 1:
                        self.puntuacion += 10

    def getHorario(self, i: int) -> str:
        return self.HORARIOS[i] if 0 <= i < len(self.HORARIOS) else "Horario inválido"
    def solucion(self,cursos,docentes,salones):
        for gen in self.Genes:
            print("Curso: ", cursos[gen.curso].nombre, "Docente: ", docentes[gen.docente].nombre, "Salon: ", salones[gen.salon].nombre, "Horario: ", self.HORARIOS[gen.horario])


    def mutacion_random_resetting(self, cursos: List[Curso], docentes: List[Docente], salones: List[Salon], prob_mutacion=0.1):
    
        for gen in self.Genes:
            # Mutación en docente
            if random.random() < prob_mutacion:
                docentes_posibles = [j for j, d in enumerate(docentes) if gen.curso in d.cursos_posibles]
                if docentes_posibles:  
                    gen.docente = random.choice(docentes_posibles)
            
            # Mutación en salón
            if random.random() < prob_mutacion:
                gen.salon = random.randint(0, len(salones) - 1)
            
            # Mutación en horario
            if random.random() < prob_mutacion:
                gen.horario = random.randint(0, 9)  

        self.calcularPuntuacion(cursos, docentes, salones)
class Gen:
    def __init__(self,curso:int,docente:int,salon:int,horario:int):
        self.curso:int = curso
        self.docente:int = docente
        self.salon:int = salon
        self.horario:int = horario
        pass