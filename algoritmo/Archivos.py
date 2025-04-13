import csv
import random
from typing import List
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from algoritmo.cromosoma import Cromosoma
from algoritmo.datos import *

def crerPdf(nombre_archivo, cromosoma:Cromosoma, cursos:List[Curso], docentes, salones):

    doc = SimpleDocTemplate(nombre_archivo, pagesize=landscape(letter), rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    elementos = []
    colores = {}
    for gen in cromosoma.Genes:
        if cursos[gen.curso].carrera is not colores:
            codigo = (random.randrange(250),random.randrange(250),random.randrange(250))
            colores[cursos[gen.curso].carrera] = codigo
            
    styles = getSampleStyleSheet()
    elementos.append(Paragraph("Horario de Clases INGENIERIA-CUNOC", styles['Heading1']))
    
    num_horarios = 10  
    num_salones = len(salones)
    datos = [[None] * (num_salones + 1) for _ in range(num_horarios + 1)] 
    
    # filas,columnas para los datos
    
    datos[0][0] = "Horario"  
    for i in range(num_horarios):
        datos[i + 1][0] = cromosoma.getHorario(i)
    

    for j, salon in enumerate(salones):
        datos[0][j + 1] = salon.nombre
    
    #columna,fila para los colores
    estilo = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Fondo gris para encabezados de salones
        ('BACKGROUND', (0, 0), (0, -1), colors.grey),  # Fondo gris para columna de horarios
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Texto blanco en encabezados
        ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),  # Texto blanco en horarios
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinear todo al centro
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Alinear verticalmente al centro
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Negrita para salones
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),  # Negrita para horarios
        ('FONTSIZE', (0, 0), (-1, -1), 3),  # Tamaño de fuente general
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Bordes negros
        #('BACKGROUND', (5, 6), (5, 6), colors.red),  # Fondo blanco para celdas de datos
        ('SPAN', (0, 0), (0, 0)),  # Evitar que "Horario" se combine
    ]
    
    for gen in cromosoma.Genes:
        curso = cursos[gen.curso]
        docente_nombre = docentes[gen.docente].nombre
        indiceHorario = gen.horario  
        indiceSalon = gen.salon
        carrera = curso.carrera     
        color = colores[carrera]
        datos[indiceHorario + 1][indiceSalon + 1] = f"{curso.nombre}\n({docente_nombre}) {curso.semestre}"
        tmp = ("BACKGROUND",(indiceSalon+1,indiceHorario+1),(indiceSalon+1,indiceHorario+1),colors.Color(color[0]/255,color[1]/255,color[2]/255))
        estilo.append(tmp)
    estilo2 = TableStyle(estilo)
    tabla = Table(datos)
    tabla.setStyle(estilo2)
    
    

    tabla._argW = [(10/num_salones) * 70] * (num_salones+1)      #ancho  
    tabla._argH = [40] * (num_horarios+1)   #alto
    
    elementos.append(tabla)
    doc.build(elementos)

def crearPDFEstadisticas(estadisticas:Estadisticas):
    print("generando estadisticas")
    doc = SimpleDocTemplate("Estadisticas.pdf", pagesize=landscape(letter), rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    elementos  = []
    styles = getSampleStyleSheet()
    elementos.append(Paragraph("Estadisticas", styles['Heading1']))
    datos = [[None] * (2) for _ in range(8) ] 
    datos[0][0] = "Nombre"
    datos[0][1] = "Valor"
    datos[1][0] = "Conflictos Salon"
    datos[1][1] = estadisticas.conflictosSalon
    datos[2][0] = "Conflictos Docente"
    datos[2][1] = estadisticas.conflictosDocente
    datos[3][0] = "Conflictos semestre"
    datos[3][1] = estadisticas.conflictosSemestre
    datos[4][0] = "Iteraciones"
    datos[4][1] = estadisticas.Iteraciones
    datos[5][0] = "Tiempo Ejecucion"
    datos[5][1] = estadisticas.TiempoEjecucion
    datos[6][0] = "Porcentaje Cursos"
    datos[6][1] = estadisticas.porcentajeCursos
    datos[7][0] = "Espacio Memoria"
    datos[7][1] = estadisticas.espacioMemoria


    tabla = Table(datos)
    tabla._argW = [100] * (2)      #ancho  
    tabla._argH = [40] * (5)   #alto
    


    elementos.append(tabla)
    doc.build(elementos)



def crearCSV(nombre_archivo, cromosoma, cursos, docentes, salones):
    with open(nombre_archivo, 'w') as file:
        file.write("Horario,Salon,Cursos,Docentes\n")
        for gen in cromosoma.Genes:
            curso_nombre = cursos[gen.curso].nombre
            docente_nombre = docentes[gen.docente].nombre
            horario = cromosoma.getHorario(gen.horario)
            salon = salones[gen.salon].nombre
            file.write(f"{horario},{salon},{curso_nombre},{docente_nombre}\n")
    print(f"CSV creado: {nombre_archivo}")

def leerCSV(archivo,listado,tipo:int,listado2):
    #tipo: 1.cursos  2. docente 3. relacionesCursoDocente 4.salones
    if tipo == 3:
        docente_dict = {docente.codigo: docente for docente in listado}
        curso_indices = {curso.codigo: idx for idx, curso in enumerate(listado2)}
    with open(archivo,newline='',encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            match tipo:
                case 1:
                    salon = Curso(row['Nombre'],row['Código'],row['Carrera'],row['Semestre'],row['Sección'],row['Tipo'])
                    listado.append(salon)
                case 2:
                    docente = Docente(row['Nombre'],row['Registro'],row['Hora Entrada'],row['Hora Salida'])
                    listado.append(docente)
                case 3:
                    registro = row['Registro de Personal']
                    codigo_curso = row['Código de Curso']
                    if registro in docente_dict and codigo_curso in curso_indices:
                        docente = docente_dict[registro]
                        indice_curso = curso_indices[codigo_curso]
                        docente.cursos_posibles.append(indice_curso)
                case 4:
                    salon = Salon(row['Nombre'],row['id'])
                    listado.append(salon)
                    pass


                
    