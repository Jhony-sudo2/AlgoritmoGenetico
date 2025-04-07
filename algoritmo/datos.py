class Salon:
    def __init__(self,nombre:str,id:int):
        self.nombre:str = nombre
        self.id:int = id
        pass

class Curso:
    def __init__(self,nombre:str,codigo:str,carrera:str,semestre:str,seccion:str,tipo:bool):
        self.nombre:str = nombre
        self.codigo:str = codigo
        self.carrera:str = carrera
        self.seccion:str = seccion
        self.semestre:str = semestre
        if(tipo == True):
            self.tipo:str = "Obligatorio"
        else:
            self.tipo:str = "Optativo"
        pass

class Docente:
    def __init__(self,nombre:str,codigo:str,horaEntrada,horaSalida):
        self.nombre:str = nombre
        self.codigo:str = codigo
        self.horaEntrada = horaEntrada
        self.horaSalida = horaSalida
        pass

class asignacionDocente:
    def __init__(self,docente:Docente,cursos:Curso):
        self.docente:Docente = docente
        self.cursos:Curso = cursos
        pass
    