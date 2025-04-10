import random
from typing import List
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from algoritmo.cromosoma import Cromosoma
from algoritmo.datos import Curso

def crerPdf(nombre_archivo, cromosoma:Cromosoma, cursos:List[Curso], docentes, salones):

    doc = SimpleDocTemplate(nombre_archivo, pagesize=landscape(letter), rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    elementos = []
    colores = {}
    for gen in cromosoma.Genes:
        if cursos[gen.curso].carrera is not colores:
            codigo = (random.randrange(250),random.randrange(250),random.randrange(250))
            print("codigo: ",codigo)
            colores[cursos[gen.curso].carrera] = codigo
            
    styles = getSampleStyleSheet()
    elementos.append(Paragraph("Horario de Clases INGENIERIA-CUNOC", styles['Heading1']))
    
    num_horarios = 10  
    num_salones = len(salones)
    datos = [[None] * (num_salones + 1) for _ in range(num_horarios + 1)] 
    
    # filas,columnas para los datos
    #columna,fila para los colores
    datos[0][0] = "Horario"  
    for i in range(num_horarios):
        datos[i + 1][0] = cromosoma.getHorario(i)
    

    for j, salon in enumerate(salones):
        datos[0][j + 1] = salon.nombre
    

    estilo = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Fondo gris para encabezados de salones
        ('BACKGROUND', (0, 0), (0, -1), colors.grey),  # Fondo gris para columna de horarios
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Texto blanco en encabezados
        ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),  # Texto blanco en horarios
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinear todo al centro
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Alinear verticalmente al centro
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Negrita para salones
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),  # Negrita para horarios
        ('FONTSIZE', (0, 0), (-1, -1), 5),  # Tamaño de fuente general
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Bordes negros
        ('BACKGROUND', (5, 6), (5, 6), colors.red),  # Fondo blanco para celdas de datos
        ('SPAN', (0, 0), (0, 0)),  # Evitar que "Horario" se combine
    ]
    
    for gen in cromosoma.Genes:
        curso = cursos[gen.curso]
        docente_nombre = docentes[gen.docente].nombre
        indiceHorario = gen.horario  
        indiceSalon = gen.salon
        carrera = curso.carrera     
        color = colores[carrera]
        datos[indiceHorario + 1][indiceSalon + 1] = f"{curso.nombre}\n({docente_nombre},{curso.semestre})"
        tmp = ("BACKGROUND",(indiceSalon+1,indiceHorario+1),(indiceSalon+1,indiceHorario+1),colors.Color(color[0]/255,color[1]/255,color[2]/255))
        estilo.append(tmp)
    estilo2 = TableStyle(estilo)
    print(estilo2)
    tabla = Table(datos)
    tabla.setStyle(estilo2)
    
    tabla._argW = [40] + [80] * num_salones  # Ancho: 80 para horarios, 150 para salones
    tabla._argH = [30] * (num_horarios + 1)   # Alto fijo para todas las filas
    
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
