from datetime import datetime
from typing import List


class Salon:
    def __init__(self,nombre:str,id:int):
        self.nombre:str = nombre
        self.id:int = id
        pass

class Curso:
    def __init__(self,nombre:str,codigo:str,carrera:str,semestre:str,seccion:str,tipo:str):
        self.nombre:str = nombre
        self.codigo:str = codigo
        self.carrera:str = carrera
        self.seccion:str = seccion
        self.semestre:str = int(semestre)
        if(tipo.casefold() == "obligatorio"):
            self.tipo = "Obligatorio"
        elif(tipo.casefold() == "optativo"):
            self.tipo = "Optativo"
        else:
            raise ValueError(f"Error en tipo de curso")
        pass

class Docente:
    def __init__(self,nombre:str,codigo:str,horaEntrada,horaSalida,cursos_posibles=None):
        self.nombre:str = nombre
        self.codigo:str = codigo
        self.horaEntrada = datetime.strptime(horaEntrada,"%H:%M").time()
        self.horaSalida = datetime.strptime(horaSalida,"%H:%M").time()
        if cursos_posibles == None:
            self.cursos_posibles = []
        else:
            self.cursos_posibles = cursos_posibles
        pass    

class Estadisticas:
    def __init__(self):
        self.conflictosSalon = 0
        self.conflictosDocente = 0
        self.conflictosSemestre = 0
        self.Iteraciones = 0
        self.TiempoEjecucion = 0
        self.porcentajeCursos = 0
        self.espacioMemoria = 0
        pass