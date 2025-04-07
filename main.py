import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from algoritmo.datos import *
from algoritmo.main import AlgoritmoGenetico

class InterfazAcademica:
    def __init__(self, root):
        self.AsignacionDocentes = []
        

        self.salones = [
            Salon("Aula Magna", 1),
            Salon("Laboratorio 1", 2),
            Salon("Aula 305", 3),
            Salon("Sala de Conferencias", 4)
        ]
        self.cursos = [
    Curso("Matemáticas Básicas", "MAT101", "Ingeniería", "10", "A", True),
    Curso("Programación I", "PROG101", "Sistemas", "8", "B", True),
    Curso("Física Avanzada", "FIS201", "Ingeniería", "7", "A", False),
    Curso("Inteligencia Artificial", "IA301", "Sistemas", "6", "C", False)
]
        self.docentes = [
    Docente("Ana Pérez", "DOC001", "08:00", "14:00"),
    Docente("Juan Gómez", "DOC002", "10:00", "16:00"),
    Docente("María López", "DOC003", "14:00", "20:00"),
    Docente("Carlos Ruiz", "DOC004", "09:00", "15:00")
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
        algoritmo = AlgoritmoGenetico(self.cursos, self.docentes, self.salones, self.AsignacionDocentes)
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