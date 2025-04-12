import random
from typing import List

from algoritmo.datos import *
class Cromosoma:
    HORARIOS = [
        "13:40-14:30", "14:30-15:20", "15:20-16:10", "16:10-17:00", "17:00-17:50",
        "17:50-18:40", "18:40-19:30", "19:30-20:20", "20:20-21:10"
    ]
    HORARIOS_TIEMPO = [(datetime.strptime(h.split("-")[0], "%H:%M").time(), 
                       datetime.strptime(h.split("-")[1], "%H:%M").time()) 
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
            horario = random.randint(0, 8)
            gen = Gen(i, docente, salon, horario)
            self.Genes.append(gen)
            #print("Curso: ", curso.nombre, "Docente: ", docentes[docente].nombre, "Salon: ", salones[salon].nombre, "Horario: ", self.HORARIOS[horario])
        self.calcularPuntuacion(cursos, docentes, salones)

    def calcularPuntuacion(self, cursos: List[Curso], docentes: List[Docente], salones: List[Salon]):
        self.puntuacion = 100
        horarios_docentes = {}
        horarios_cursos_obligatorios = {}
        horarios_salones = {}  
        for gen in self.Genes:
            curso = cursos[gen.curso]
            docente = docentes[gen.docente]
            inicio, fin = self.HORARIOS_TIEMPO[gen.horario]
            
            # Verificacion Disponibilidad del docente
            if inicio < docente.horaEntrada or fin > docente.horaSalida:
                self.puntuacion -= 5
            
            # Verificar traslape docente
            if gen.docente in horarios_docentes:
                if gen.horario in horarios_docentes[gen.docente]:
                    self.puntuacion -= 5
                else:
                    horarios_docentes[gen.docente].append(gen.horario)
            else:
                horarios_docentes[gen.docente] = [gen.horario]
            #validacion traslape de salones
            if gen.salon in horarios_salones:
                if gen.horario in horarios_salones[gen.salon]:
                    self.puntuacion -= 5
                else:
                    horarios_salones[gen.salon].append(gen.horario)
            else:
                horarios_salones[gen.salon] = [gen.horario]
            
            # verificacion traslpae del mismo semestre carrera
            if curso.tipo == "Obligatorio":
                key = (curso.carrera, curso.semestre)
                if key in horarios_cursos_obligatorios:
                    if gen.horario in horarios_cursos_obligatorios[key]:
                        self.puntuacion -= 5
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
                        self.puntuacion += 2

    def getHorario(self, i: int) -> str:
        return self.HORARIOS[i] if 0 <= i < len(self.HORARIOS) else "Horario inválido"
    def solucion(self,cursos,docentes,salones):
        print("puntuacion: ",self.puntuacion)
        for gen in self.Genes:
            #print("Curso: ", cursos[gen.curso].nombre, "Docente: ", docentes[gen.docente].nombre, "Salon: ", salones[gen.salon].nombre, "Horario: ", self.HORARIOS[gen.horario])
            print("(",gen.curso,",",gen.docente,",",gen.horario," )")

    def mutacion_random_resetting(self, cursos: List[Curso], docentes: List[Docente], salones: List[Salon], prob_mutacion=0.1):
        gentmp:Gen = random.sample(self.Genes,1)[0]
        tipo = random.randint(0,3)
        match tipo:
            case 1:
                docentes_posibles = [j for j, d in enumerate(docentes) if gentmp.curso in d.cursos_posibles]
                if docentes_posibles:  
                    gentmp.docente = random.choice(docentes_posibles)
                
            case 2:
                gentmp.salon = random.randint(0, len(salones) - 1)
                
            case 3:
                gentmp.horario = random.randint(0, 8)
        """
        for gen in self.Genes:
            
            tipo = random.randint(0,3)
            match tipo:
                case 1:
                    docentes_posibles = [j for j, d in enumerate(docentes) if gen.curso in d.cursos_posibles]
                    if docentes_posibles:  
                        gen.docente = random.choice(docentes_posibles)
                
                case 2:
                    gen.salon = random.randint(0, len(salones) - 1)
                
                case 3:
                     gen.horario = random.randint(0, 9)  
            
            #PRIMERA OPCION

            if random.random() < prob_mutacion:
                docentes_posibles = [j for j, d in enumerate(docentes) if gen.curso in d.cursos_posibles]
                if docentes_posibles:  
                    gen.docente = random.choice(docentes_posibles)
            
            # Mutación en salón
            if random.random() < prob_mutacion:
                gen.salon = random.randint(0, len(salones) - 1)
            
            # Mutación en horario
            if random.random() < prob_mutacion:
                gen.horario = random.randint(0, 8)  
        """
        self.calcularPuntuacion(cursos, docentes, salones)
class Gen:
    def __init__(self,curso:int,docente:int,salon:int,horario:int):
        self.curso:int = curso
        self.docente:int = docente
        self.salon:int = salon
        self.horario:int = horario
        pass