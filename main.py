import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from algoritmo import Archivos
from algoritmo.datos import *
from algoritmo.main import AlgoritmoGenetico

class InterfazAcademica:
    def __init__(self, root):
        self.AsignacionDocentes = []
        

        self.salones = [
    Salon("Aula Magna 1", 120),
    Salon("Aula Magna 2", 100),
    Salon("Laboratorio de Informática 1", 30),
    Salon("Laboratorio de Informática 2", 25),
    Salon("Aula 301", 40),
    Salon("Sala de Conferencias 1", 80),
    Salon("Sala de Conferencias 2", 70),
    Salon("Laboratorio de Física 1", 35),
    Salon("Laboratorio de Física 2", 30),
    Salon("Aula 302", 45),
    Salon("Aula 401", 60),
    Salon("Aula 402", 50),
    Salon("Laboratorio de Biología 1", 25),
    Salon("Laboratorio de Biología 2", 20),
    Salon("Sala de Proyecciones 1", 90),
    Salon("Sala de Proyecciones 2", 85),
    Salon("Aula 501", 55),
    Salon("Aula 502", 50),
    Salon("Laboratorio de Química 1", 30),
    Salon("Laboratorio de Química 2", 25)
]
        self.cursos = [
    # Ingeniería en Sistemas (códigos SYS101 a SYS110)
    Curso("Programación I", "SYS101", "Ingeniería en Sistemas", "1", "A", True),
    Curso("Programación II", "SYS102", "Ingeniería en Sistemas", "2", "B", True),
    Curso("Bases de Datos", "SYS103", "Ingeniería en Sistemas", "3", "A", True),
    Curso("Algoritmos Avanzados", "SYS104", "Ingeniería en Sistemas", "4", "B", False),
    Curso("Inteligencia Artificial", "SYS105", "Ingeniería en Sistemas", "5", "C", False),
    Curso("Redes de Computadoras", "SYS106", "Ingeniería en Sistemas", "6", "A", True),
    Curso("Sistemas Operativos", "SYS107", "Ingeniería en Sistemas", "3", "B", True),
    Curso("Ingeniería de Software", "SYS108", "Ingeniería en Sistemas", "4", "A", True),
    Curso("Ciberseguridad", "SYS109", "Ingeniería en Sistemas", "5", "B", False),
    Curso("Proyectos de TI", "SYS110", "Ingeniería en Sistemas", "6", "C", True),

    # Ingeniería Civil (códigos CIV101 a CIV110)
    
    Curso("Cálculo Estructural", "CIV101", "Ingeniería Civil", "1", "A", True),
    Curso("Mecánica de Suelos", "CIV102", "Ingeniería Civil", "2", "B", True),
    Curso("Diseño de Puentes", "CIV103", "Ingeniería Civil", "3", "A", False),
    Curso("Hidráulica", "CIV104", "Ingeniería Civil", "4", "B", True),
    Curso("Construcción Sostenible", "CIV105", "Ingeniería Civil", "5", "A", False),
    Curso("Geotecnia", "CIV106", "Ingeniería Civil", "3", "B", True),
    Curso("Topografía", "CIV107", "Ingeniería Civil", "2", "A", True),
    Curso("Materiales de Construcción", "CIV108", "Ingeniería Civil", "1", "B", True),
    Curso("Gestión de Proyectos", "CIV109", "Ingeniería Civil", "5", "C", True),
    Curso("Diseño Sísmico", "CIV110", "Ingeniería Civil", "6", "A", False),

    # Ciencias Biológicas (códigos BIO101 a BIO110)
    Curso("Biología Celular", "BIO101", "Ciencias Biológicas", "1", "A", True),
    Curso("Genética", "BIO102", "Ciencias Biológicas", "2", "B", True),
    Curso("Ecología", "BIO103", "Ciencias Biológicas", "3", "A", False),
    Curso("Microbiología", "BIO104", "Ciencias Biológicas", "4", "B", True),
    Curso("Biotecnología", "BIO105", "Ciencias Biológicas", "5", "C", False),
    Curso("Fisiología Vegetal", "BIO106", "Ciencias Biológicas", "3", "A", True),
    Curso("Zoología", "BIO107", "Ciencias Biológicas", "2", "B", True),
    Curso("Bioquímica", "BIO108", "Ciencias Biológicas", "4", "A", True),
    Curso("Evolución", "BIO109", "Ciencias Biológicas", "5", "B", False),
    Curso("Biología Marina", "BIO110", "Ciencias Biológicas", "6", "C", True),

    # Administración de Empresas (códigos ADM101 a ADM110)
    Curso("Introducción a la Administración", "ADM101", "Administración de Empresas", "1", "A", True),
    Curso("Contabilidad Básica", "ADM102", "Administración de Empresas", "2", "B", True),
    Curso("Marketing", "ADM103", "Administración de Empresas", "3", "A", True),
    Curso("Finanzas Corporativas", "ADM104", "Administración de Empresas", "4", "B", True),
    Curso("Gestión de Recursos Humanos", "ADM105", "Administración de Empresas", "5", "C", False),
    Curso("Economía Empresarial", "ADM106", "Administración de Empresas", "3", "A", True),
    Curso("Estrategia Empresarial", "ADM107", "Administración de Empresas", "4", "B", True),
    Curso("Emprendimiento", "ADM108", "Administración de Empresas", "5", "A", False),
    Curso("Comportamiento Organizacional", "ADM109", "Administración de Empresas", "2", "B", True),
    Curso("Logística y Cadena de Suministro", "ADM110", "Administración de Empresas", "6", "C", True)
    
]
        self.docentes = [
    # Docentes de Ingeniería en Sistemas
    Docente("Ana Pérez", "DOC001", "14:00", "18:00", [0, 1, 2, 3, 4, 5]),  # Programación I, Programación II, Bases de Datos, Algoritmos Avanzados, Inteligencia Artificial, Redes de Computadoras
    Docente("Juan Gómez", "DOC002", "18:00", "22:00", [3, 4, 5, 6, 7, 8]),  # Algoritmos Avanzados, Inteligencia Artificial, Redes de Computadoras, Sistemas Operativos, Ingeniería de Software, Ciberseguridad
    Docente("María López", "DOC003", "14:00", "20:00", [5, 6, 7, 8, 9]),    # Redes de Computadoras, Sistemas Operativos, Ingeniería de Software, Ciberseguridad, Proyectos de TI

    # Docentes de Ingeniería Civil
    Docente("Carlos Ruiz", "DOC004", "13:00", "17:00", [10, 11, 12, 13, 14, 15]),  # Cálculo Estructural, Mecánica de Suelos, Diseño de Puentes, Hidráulica, Construcción Sostenible, Geotecnia
    Docente("Elena Martínez", "DOC005", "17:00", "22:00", [12, 13, 14, 15, 16, 17]),  # Diseño de Puentes, Hidráulica, Construcción Sostenible, Geotecnia, Topografía, Materiales de Construcción
    Docente("Pedro Sánchez", "DOC006", "14:00", "22:00", [15, 16, 17, 18, 19]),  # Geotecnia, Topografía, Materiales de Construcción, Gestión de Proyectos, Diseño Sísmico

    # Docentes de Ciencias Biológicas
    Docente("Laura Fernández", "DOC007", "14:00", "19:00", [20, 21, 22, 23, 24, 25]),  # Biología Celular, Genética, Ecología, Microbiología, Biotecnología, Fisiología Vegetal
    Docente("Miguel Torres", "DOC008", "17:00", "22:00", [23, 24, 25, 26, 27, 28]),  # Microbiología, Biotecnología, Fisiología Vegetal, Zoología, Bioquímica, Evolución
    Docente("Sofía Ramírez", "DOC009", "13:00", "16:00", [25, 26, 27, 28, 29]),  # Fisiología Vegetal, Zoología, Bioquímica, Evolución, Biología Marina

    # Docentes de Administración de Empresas
    Docente("Andrés Vargas", "DOC010", "16:00", "22:00", [30, 31, 32, 33, 34, 35]),  # Introducción a la Administración, Contabilidad Básica, Marketing, Finanzas Corporativas, Gestión de Recursos Humanos, Economía Empresarial
    Docente("Clara Díaz", "DOC011", "13:00", "22:00", [33, 34, 35, 36, 37, 38]),  # Finanzas Corporativas, Gestión de Recursos Humanos, Economía Empresarial, Estrategia Empresarial, Emprendimiento, Comportamiento Organizacional
    Docente("Diego Morales", "DOC012", "14:00", "18:00", [35, 36, 37, 38, 39])  # Economía Empresarial, Estrategia Empresarial, Emprendimiento, Comportamiento Organizacional, Logística y Cadena de Suministro
]

        
        self.asignacion = False
        self.root = root
        self.root.title("Sistema de Gestión Académica")
        self.root.geometry("800x400")

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.menu_bar.add_command(label="Cursos", command=self.mostrar_cursos)
        self.menu_bar.add_command(label="Docentes", command=self.mostrar_docentes)
        self.menu_bar.add_command(label="Asignación Docentes", command=self.mostrar_asignacion)
        self.menu_bar.add_command(label="Salones", command=self.mostrar_salones)
        self.menu_bar.add_command(label="Generación Horario", command=self.mostrar_horarios)

        self.frame_superior = tk.Frame(self.root)
        self.frame_superior.pack(fill="x", padx=5, pady=5)

        self.frame_tabla = tk.Frame(self.root, bg="lightgray")
        self.frame_tabla.pack(fill="both", expand=True, padx=5, pady=5)

        self.tabla_actual = None
        self.boton_nuevo = None
        self.botonExportacion = None

        self.mostrar_docentes()
    def crearHorario(self):
        algoritmo = AlgoritmoGenetico(self.cursos, self.docentes, self.salones)
        algoritmo.Iniciar()


    def limpiar_panel(self):
        for widget in self.frame_tabla.winfo_children():
            widget.destroy()
        if self.boton_nuevo:
            self.boton_nuevo.destroy()
        if self.botonExportacion:
            self.botonExportacion.destroy()

    def crear_tabla(self, columnas,datos):
        self.tabla_actual = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")
        for col in columnas:
            self.tabla_actual.heading(col, text=col)
            self.tabla_actual.column(col, width=100, anchor="center")
        if not self.asignacion:
            for objeto in datos:
                valores = [getattr(objeto, col) for col in columnas]
                self.tabla_actual.insert("", "end", values=valores)
            self.tabla_actual.pack(fill="both", expand=True)
        else:
            for docente in datos:
                for curso in docente.cursos_posibles:
                    valores = [docente.nombre,self.cursos[curso].nombre]
                    self.tabla_actual.insert("", "end", values=valores)
                    self.tabla_actual.pack(fill="both", expand=True)
            self.asignacion = False

    def crear_formulario(self, columnas, titulo,arreglo):
        ventana_nuevo = tk.Toplevel(self.root)
        ventana_nuevo.title(titulo)
        ventana_nuevo.geometry("300x400")

        entradas = {}
        for col in columnas:
            tk.Label(ventana_nuevo, text=f"{col}:").pack()
            entrada = tk.Entry(ventana_nuevo)
            entrada.pack()
            entradas[col] = entrada

        def guardar():

            valores = tuple(entradas[col].get() for col in columnas)
            valores_dict = {col: entradas[col].get() for col in columnas}
            self.tabla_actual.insert("", "end", values=valores)
            clase = globals()[titulo]  
            objeto = clase(**valores_dict)
            arreglo.append(objeto)
            ventana_nuevo.destroy()

        tk.Button(ventana_nuevo, text="Guardar", command=guardar).pack(pady=10)
    def importarCSV(self,listado,tipo,columnas,listado2=None):
        file_path = filedialog.askopenfilename(
        initialdir="./",
        title="Seleccionar archivo",
        filetypes=[("Archivos de texto", "*.csv"), ("Todos los archivos", "*.*")]
        )
        Archivos.leerCSV(file_path,listado,tipo,listado2)
        if tipo == 3:
            self.asignacion = True
        self.limpiar_panel()
        self.crear_tabla(columnas,listado)
        pass

    def mostrar_cursos(self):
        self.limpiar_panel()
        columnas = ("nombre", "codigo", "carrera", "semestre", "seccion", "tipo")
        self.crear_tabla(columnas,self.cursos)
        self.botonExportacion = tk.Button(self.frame_superior, text="Importar CSV", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.importarCSV(self.cursos,1,columnas))
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Curso",self.cursos))
        self.boton_nuevo.pack(side="right", padx=5)
        self.botonExportacion.pack(side="right",padx=5)

    def mostrar_docentes(self):
        self.limpiar_panel()
        columnas = ("nombre", "codigo", "horaEntrada", "horaSalida")
        self.crear_tabla(columnas,self.docentes)
        self.botonExportacion = tk.Button(self.frame_superior, text="Importar CSV", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.importarCSV(self.docentes,2,columnas))
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Docente",self.docentes))
        self.boton_nuevo.pack(side="right", padx=5)
        self.botonExportacion.pack(side="right",padx=5)

    def mostrar_asignacion(self):
        self.limpiar_panel()
        columnas = ("docente", "cursos")
        self.asignacion = True
        self.crear_tabla(columnas,self.docentes)
        self.botonExportacion = tk.Button(self.frame_superior, text="Importar CSV", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.importarCSV(self.docentes,3,columnas,listado2=self.cursos))
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Asignar Docente",self.AsignacionDocentes))
        self.boton_nuevo.pack(side="right", padx=5)
        self.botonExportacion.pack(side="right",padx=5)

    def mostrar_salones(self):
        self.limpiar_panel()
        columnas = ("nombre", "id")
        self.crear_tabla(columnas,self.salones)
        self.botonExportacion = tk.Button(self.frame_superior, text="Importar CSV", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.importarCSV(self.salones,4,columnas))
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Salon",self.salones))
        self.boton_nuevo.pack(side="right", padx=5)
        self.botonExportacion.pack(side="right",padx=5)

    def mostrar_horarios(self):
        self.limpiar_panel()
        columnas = ("Horario", "Docente", "Curso", "Salón")
        self.crear_tabla(columnas,self.AsignacionDocentes)
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crearHorario())
        self.boton_nuevo.pack(side="right", padx=5)

# Crear la ventana principal y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazAcademica(root)
    root.mainloop()