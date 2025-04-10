import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from algoritmo.datos import *
from algoritmo.main import AlgoritmoGenetico

class InterfazAcademica:
    def __init__(self, root):
        self.AsignacionDocentes = []
        

        self.salones = [
    Salon("Aula Magna", 100),
    Salon("Laboratorio 1", 30),
    Salon("Aula 305", 40),
    Salon("Sala de Conferencias", 80),
    Salon("Laboratorio 2", 25),
    Salon("Aula 101", 50),
    Salon("Aula 202", 45),
    Salon("Laboratorio de Física", 35),
    Salon("Aula 401", 60),
    Salon("Sala de Proyecciones", 70)
]
        self.cursos = [
    Curso("Matemáticas Básicas", "MAT101", "Ingeniería", "1", "A", True),
    Curso("Programación I", "PROG101", "Sistemas", "2", "B", True),
    Curso("Física Avanzada", "FIS201", "Ingeniería", "3", "A", False),
    Curso("Inteligencia Artificial", "IA301", "Sistemas", "6", "C", False),
    Curso("Cálculo Diferencial", "MAT102", "Ingeniería", "2", "B", True),
    Curso("Bases de Datos", "BD201", "Sistemas", "4", "A", True),
    Curso("Química General", "QUI101", "Ciencias", "1", "A", True),
    Curso("Algoritmos Avanzados", "ALG301", "Sistemas", "5", "B", False),
    Curso("Estadística", "EST201", "Ingeniería", "3", "C", True),
    Curso("Biología Molecular", "BIO301", "Ciencias", "5", "A", False),
    Curso("Redes de Computadoras", "RED301", "Sistemas", "6", "B", True),
    Curso("Mecánica Clásica", "FIS101", "Ingeniería", "2", "A", True),
    Curso("Programación II", "PROG201", "Sistemas", "3", "C", True),
    Curso("Geometría Analítica", "MAT201", "Ingeniería", "3", "B", True),
    Curso("Ecología", "ECO201", "Ciencias", "4", "A", False)
]
        self.docentes = [
    Docente("Ana Pérez", "DOC001", "08:00", "14:00", [0, 4, 8, 13]),        # Matemáticas, Cálculo, Estadística, Geometría
    Docente("Juan Gómez", "DOC002", "10:00", "16:00", [1, 7, 10, 12]),      # Programación I, Algoritmos, Redes, Programación II
    Docente("María López", "DOC003", "14:00", "20:00", [1, 3, 7, 10]),      # Programación I, IA, Algoritmos, Redes
    Docente("Carlos Ruiz", "DOC004", "09:00", "15:00", [0, 2, 4, 11]),      # Matemáticas, Física Avanzada, Cálculo, Mecánica
    Docente("Elena Martínez", "DOC005", "07:00", "13:00", [6, 9, 14]),      # Química, Biología, Ecología
    Docente("Pedro Sánchez", "DOC006", "11:00", "17:00", [3, 7, 10, 12]),   # IA, Algoritmos, Redes, Programación II
    Docente("Laura Fernández", "DOC007", "08:00", "14:00", [2, 8, 11, 13]), # Física Avanzada, Estadística, Mecánica, Geometría
    Docente("Miguel Torres", "DOC008", "13:00", "19:00", [5, 6, 9, 14])     # Bases de Datos, Química, Biología, Ecología
]
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

        self.mostrar_docentes()
    def crearHorario(self):
        print("NUMERO DE SALONES: " + str(len(self.salones)))
        algoritmo = AlgoritmoGenetico(self.cursos, self.docentes, self.salones)
        algoritmo.Iniciar()


    def limpiar_panel(self):
        for widget in self.frame_tabla.winfo_children():
            widget.destroy()
        if self.boton_nuevo:
            self.boton_nuevo.destroy()

    def crear_tabla(self, columnas,datos):
        self.tabla_actual = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")
        for col in columnas:
            self.tabla_actual.heading(col, text=col)
            self.tabla_actual.column(col, width=100, anchor="center")
        for objeto in datos:
            valores = [getattr(objeto, col) for col in columnas]
            self.tabla_actual.insert("", "end", values=valores)
        self.tabla_actual.pack(fill="both", expand=True)

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

    def mostrar_cursos(self):
        self.limpiar_panel()
        columnas = ("nombre", "codigo", "carrera", "semestre", "seccion", "tipo")
        self.crear_tabla(columnas,self.cursos)
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Curso",self.cursos))
        self.boton_nuevo.pack(side="right", padx=5)

    def mostrar_docentes(self):
        self.limpiar_panel()
        columnas = ("nombre", "codigo", "horaEntrada", "horaSalida")
        self.crear_tabla(columnas,self.docentes)
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Docente",self.docentes))
        self.boton_nuevo.pack(side="right", padx=5)

    def mostrar_asignacion(self):
        self.limpiar_panel()
        columnas = ("docente", "cursos")
        self.crear_tabla(columnas,self.AsignacionDocentes)
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Asignar Docente",self.AsignacionDocentes))
        self.boton_nuevo.pack(side="right", padx=5)

    def mostrar_salones(self):
        self.limpiar_panel()
        columnas = ("nombre", "id")
        self.crear_tabla(columnas,self.salones)
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Salon",self.salones))
        self.boton_nuevo.pack(side="right", padx=5)

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