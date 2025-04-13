import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from algoritmo import Archivos
from algoritmo.cromosoma import Gen
from algoritmo.datos import *
from algoritmo.main import AlgoritmoGenetico

class InterfazAcademica:
    def __init__(self, root):
        self.AsignacionDocentes = []
        self.cursosSeleccionados = []
        self.docentesSeleccionados = []

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
            Docente("Ana Pérez", "DOC001", "14:00", "18:00", [0, 1, 2, 3, 4, 5]),
            Docente("Juan Gómez", "DOC002", "18:00", "22:00", [3, 4, 5, 6, 7, 8]),
            Docente("María López", "DOC003", "14:00", "20:00", [5, 6, 7, 8, 9]),
            Docente("Carlos Ruiz", "DOC004", "13:00", "17:00", [10, 11, 12, 13, 14, 15]),
            Docente("Elena Martínez", "DOC005", "17:00", "22:00", [12, 13, 14, 15, 16, 17]),
            Docente("Pedro Sánchez", "DOC006", "14:00", "22:00", [15, 16, 17, 18, 19]),
            Docente("Laura Fernández", "DOC007", "14:00", "19:00", [20, 21, 22, 23, 24, 25]),
            Docente("Miguel Torres", "DOC008", "17:00", "22:00", [23, 24, 25, 26, 27, 28]),
            Docente("Sofía Ramírez", "DOC009", "13:00", "16:00", [25, 26, 27, 28, 29]),
            Docente("Andrés Vargas", "DOC010", "16:00", "22:00", [30, 31, 32, 33, 34, 35]),
            Docente("Clara Díaz", "DOC011", "13:00", "22:00", [33, 34, 35, 36, 37, 38]),
            Docente("Diego Morales", "DOC012", "14:00", "18:00", [35, 36, 37, 38, 39])
        ]
        self.horarios = [
            ("08:00-09:00", "Lunes"),
            ("09:00-10:00", "Lunes"),
            ("10:00-11:00", "Lunes"),
            ("11:00-12:00", "Lunes"),
            ("13:00-14:00", "Lunes"),
            ("14:00-15:00", "Lunes"),
            ("15:00-16:00", "Lunes"),
            ("16:00-17:00", "Lunes")
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
        self.menu_bar.add_command(label="Asignación Manual", command=self.mostrar_asignacion_manual)
        self.menu_bar.add_command(label="Seleccion ", command=self.seleccion)
        self.menu_bar.add_command(label="Generación Horario", command=self.mostrar_horarios)
        self.menu_bar.add_command(label="Algoritmo", command=self.configurarAlgoritmo)


        self.frame_superior = tk.Frame(self.root)
        self.frame_superior.pack(fill="x", padx=5, pady=5)

        self.frame_tabla = tk.Frame(self.root, bg="lightgray")
        self.frame_tabla.pack(fill="both", expand=True, padx=5, pady=5)

        self.tabla_actual = None
        self.boton_nuevo = None
        self.botonExportacion = None
        self.botonCrear = None
        self.botonAsignacion = None
        self.mostrar_docentes()
    def configurarAlgoritmo(self):
        self.limpiar_panel()
        item = ttk.Treeview(self.frame_tabla)
        columnas = ["Poblacion","Generaciones Maxima"]
        item.columm = columnas
        entradas = {}
        for col in columnas:
            tk.Label(self.frame_tabla, text=f"{col}:").pack()
            entrada = tk.Entry(self.frame_tabla)
            entrada.pack()
            entradas[col] = entrada
        


    def mostrar_asignacion_manual(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Asignación Manual de Curso a Salón")
        ventana.geometry("400x200")

        frame = tk.Frame(ventana)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(frame, text="Seleccionar Curso:", font=("Arial", 10, "bold")).pack(pady=5)
        cursos_nombres = [curso.nombre for curso in self.cursosSeleccionados]
        curso_combobox = ttk.Combobox(frame, values=cursos_nombres, state="readonly")
        curso_combobox.pack(pady=5)
        curso_combobox.set(cursos_nombres[0] if cursos_nombres else "")

        tk.Label(frame, text="Seleccionar Salón:", font=("Arial", 10, "bold")).pack(pady=5)
        salones_nombres = [salon.nombre for salon in self.salones]
        salon_combobox = ttk.Combobox(frame, values=salones_nombres, state="readonly")
        salon_combobox.pack(pady=5)
        salon_combobox.set(salones_nombres[0] if salones_nombres else "")

        def guardar_asignacion():
            curso_nombre = curso_combobox.get()
            salon_nombre = salon_combobox.get()

            if not curso_nombre or not salon_nombre:
                messagebox.showwarning("Advertencia", "Debe seleccionar un curso y un salón.")
                return
            curso_seleccionado = 0
            salon_seleccionado = 0
            for i,curso in enumerate(self.cursosSeleccionados):
                if curso.nombre == curso_nombre:
                    curso_seleccionado = i
            for i,salon in enumerate(self.salones):
                if salon.nombre == salon_nombre:
                    salon_seleccionado = i
            
            asignacion = Gen(curso_seleccionado,0,salon_seleccionado,0)
            self.AsignacionDocentes.append(asignacion)

            messagebox.showinfo("Éxito", f"Curso '{curso_nombre}' asignado al salón '{salon_nombre}' correctamente.")
            ventana.destroy()

            self.mostrar_horarios()

        tk.Button(frame, text="Guardar Asignación", bg="#008080", fg="white", font=("Arial", 10, "bold"), command=guardar_asignacion).pack(pady=10)

    def seleccion(self):
        self.limpiar_panel()
        columnas_docentes = ("nombre", "codigo", "Seleccionar")
        tabla_docentes = ttk.Treeview(self.frame_tabla, columns=columnas_docentes, show="headings")
        for col in columnas_docentes:
            tabla_docentes.heading(col, text=col)
            tabla_docentes.column(col, width=150, anchor="center")

        seleccionados_docentes = {}
        for docente in self.docentes:
            var = tk.BooleanVar(value=False)
            seleccionados_docentes[docente.codigo] = var
            tabla_docentes.insert("", "end", values=(docente.nombre, docente.codigo, ""))

        tabla_docentes.pack(fill="both", expand=True)

        seleccionar_todos_docentes_var = tk.BooleanVar(value=False)
        def toggle_seleccionar_todos_docentes():
            estado = seleccionar_todos_docentes_var.get()
            for var in seleccionados_docentes.values():
                var.set(estado)
            for i, item in enumerate(tabla_docentes.get_children()):
                docente_codigo = tabla_docentes.item(item, "values")[1]
                tabla_docentes.item(item, values=(self.docentes[i].nombre, docente_codigo, "✔" if seleccionados_docentes[docente_codigo].get() else ""))

        tk.Checkbutton(self.frame_tabla, text="Seleccionar todos los docentes", variable=seleccionar_todos_docentes_var, command=toggle_seleccionar_todos_docentes).pack(pady=5)
        def actualizar_checkbox_docentes(event):
            item = tabla_docentes.selection()
            if not item:
                return
            docente_codigo = tabla_docentes.item(item, "values")[1]
            seleccionados_docentes[docente_codigo].set(not seleccionados_docentes[docente_codigo].get())
            tabla_docentes.item(item, values=(tabla_docentes.item(item, "values")[0], docente_codigo, "✔" if seleccionados_docentes[docente_codigo].get() else ""))
            todos_seleccionados = all(var.get() for var in seleccionados_docentes.values())
            seleccionar_todos_docentes_var.set(todos_seleccionados)

        tabla_docentes.bind("<Button-1>", actualizar_checkbox_docentes)

        tk.Label(self.frame_tabla, text="Seleccionar Cursos", font=("Arial", 12, "bold")).pack()
        columnas_cursos = ("nombre", "codigo", "Seleccionar")
        tabla_cursos = ttk.Treeview(self.frame_tabla, columns=columnas_cursos, show="headings")
        for col in columnas_cursos:
            tabla_cursos.heading(col, text=col)
            tabla_cursos.column(col, width=150, anchor="center")

        seleccionados_cursos = {}
        for curso in self.cursos:
            var = tk.BooleanVar(value=False)
            seleccionados_cursos[curso.codigo] = var
            tabla_cursos.insert("", "end", values=(curso.nombre, curso.codigo, ""))

        tabla_cursos.pack(fill="both", expand=True)

        seleccionar_todos_cursos_var = tk.BooleanVar(value=False)
        def toggle_seleccionar_todos_cursos():
            estado = seleccionar_todos_cursos_var.get()
            for var in seleccionados_cursos.values():
                var.set(estado)
            for i, item in enumerate(tabla_cursos.get_children()):
                curso_codigo = tabla_cursos.item(item, "values")[1]
                tabla_cursos.item(item, values=(self.cursos[i].nombre, curso_codigo, "✔" if seleccionados_cursos[curso_codigo].get() else ""))

        tk.Checkbutton(self.frame_tabla, text="Seleccionar todos los cursos", variable=seleccionar_todos_cursos_var, command=toggle_seleccionar_todos_cursos).pack(pady=5)

        def actualizar_checkbox_cursos(event):
            item = tabla_cursos.selection()
            if not item:
                return
            curso_codigo = tabla_cursos.item(item, "values")[1]
            seleccionados_cursos[curso_codigo].set(not seleccionados_cursos[curso_codigo].get())
            tabla_cursos.item(item, values=(tabla_cursos.item(item, "values")[0], curso_codigo, "✔" if seleccionados_cursos[curso_codigo].get() else ""))
            todos_seleccionados = all(var.get() for var in seleccionados_cursos.values())
            seleccionar_todos_cursos_var.set(todos_seleccionados)

        tabla_cursos.bind("<Button-1>", actualizar_checkbox_cursos)

        def guardar_seleccion():
            self.docentesSeleccionados = [docente for docente in self.docentes if seleccionados_docentes[docente.codigo].get()]
            self.cursosSeleccionados = [curso for curso in self.cursos if seleccionados_cursos[curso.codigo].get()]

            if not self.docentesSeleccionados:
                messagebox.showwarning("Advertencia", "Debe seleccionar al menos un docente.")
                return
            if not self.cursosSeleccionados:
                messagebox.showwarning("Advertencia", "Debe seleccionar al menos un curso.")
                return

            messagebox.showinfo("Éxito", f"Se seleccionaron {len(self.docentesSeleccionados)} docentes y {len(self.cursosSeleccionados)} cursos.")

        self.botonAsignacion = tk.Button(self.frame_superior, text="Guardar selección", bg="#008080", fg="white", font=("Arial", 10, "bold"), command=guardar_seleccion)
        self.botonAsignacion.pack(side="right", padx=5)
        
    def crearHorario(self):
        if not self.cursosSeleccionados:
            self.cursosSeleccionados = self.cursos
        if not self.docentesSeleccionados:
            self.docentesSeleccionados = self.docentes
        algoritmo = AlgoritmoGenetico(self.cursos,self.docentes,self.salones,self.AsignacionDocentes)
        algoritmo.Iniciar()
        self.cursosSeleccionados = []
        self.docentesSeleccionados = []
    def limpiar_panel(self):
        for widget in self.frame_tabla.winfo_children():
            widget.destroy()
        if self.boton_nuevo:
            self.boton_nuevo.destroy()
        if self.botonExportacion:
            self.botonExportacion.destroy()
        if self.botonCrear:
            self.botonCrear.destroy()
        if self.botonAsignacion:
            self.botonAsignacion.destroy()

    def crear_tabla(self, tabla_actual, frame_tabla, columnas, datos):
        tabla_actual = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        for col in columnas:
            tabla_actual.heading(col, text=col)
            tabla_actual.column(col, width=100, anchor="center")
        
        if not self.asignacion:
            for objeto in datos:
                if isinstance(objeto, Gen):
                    valores = (objeto.horario, self.docentesSeleccionados[objeto.docente].nombre, self.cursosSeleccionados[objeto.curso].nombre, self.salones[objeto.salon].nombre)
                else:   
                    valores = [getattr(objeto, col) for col in columnas if col not in ["Horario", "Docente", "Curso", "Salón"]]
                    if len(valores) != len(columnas):
                        valores = objeto
                tabla_actual.insert("", "end", values=valores)
            tabla_actual.pack(fill="both", expand=True)
        else:
            for docente in datos:
                for curso in docente.cursos_posibles:
                    valores = [docente.nombre, self.cursos[curso].nombre]
                    tabla_actual.insert("", "end", values=valores)
                    tabla_actual.pack(fill="both", expand=True)
            self.asignacion = False
        return tabla_actual

    def crear_formulario(self, columnas, titulo, arreglo):
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

    def importarCSV(self, listado, tipo, columnas, listado2=None):
        file_path = filedialog.askopenfilename(
            initialdir="./",
            title="Seleccionar archivo",
            filetypes=[("Archivos de texto", "*.csv"), ("Todos los archivos", "*.*")]
        )
        Archivos.leerCSV(file_path, listado, tipo, listado2)
        if tipo == 3:
            self.asignacion = True
        self.limpiar_panel()
        self.crear_tabla(self.tabla_actual, self.frame_tabla, columnas, listado)

    def mostrar_cursos(self):
        self.limpiar_panel()
        columnas = ("nombre", "codigo", "carrera", "semestre", "seccion", "tipo")
        self.tabla_actual = self.crear_tabla(self.tabla_actual, self.frame_tabla, columnas, self.cursos)
        self.botonExportacion = tk.Button(self.frame_superior, text="Importar CSV", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                         command=lambda: self.importarCSV(self.cursos, 1, columnas))
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Curso", self.cursos))
        self.boton_nuevo.pack(side="right", padx=5)
        self.botonExportacion.pack(side="right", padx=5)

    def mostrar_docentes(self):
        self.limpiar_panel()
        columnas = ("nombre", "codigo", "horaEntrada", "horaSalida")
        self.tabla_actual = self.crear_tabla(self.tabla_actual, self.frame_tabla, columnas, self.docentes)
        self.botonExportacion = tk.Button(self.frame_superior, text="Importar CSV", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                         command=lambda: self.importarCSV(self.docentes, 2, columnas))
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Docente", self.docentes))
        self.boton_nuevo.pack(side="right", padx=5)
        self.botonExportacion.pack(side="right", padx=5)

    def mostrar_asignacion(self):
        self.limpiar_panel()
        columnas = ("docente", "cursos")
        self.asignacion = True
        self.tabla_actual = self.crear_tabla(self.tabla_actual, self.frame_tabla, columnas, self.docentes)
        self.botonExportacion = tk.Button(self.frame_superior, text="Importar CSV", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                         command=lambda: self.importarCSV(self.docentes, 3, columnas, listado2=self.cursos))
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Asignar Docente", self.AsignacionDocentes))
        self.boton_nuevo.pack(side="right", padx=5)
        self.botonExportacion.pack(side="right", padx=5)

    def mostrar_salones(self):
        self.limpiar_panel()
        columnas = ("nombre", "id")
        self.tabla_actual = self.crear_tabla(self.tabla_actual, self.frame_tabla, columnas, self.salones)
        self.botonExportacion = tk.Button(self.frame_superior, text="Importar CSV", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                         command=lambda: self.importarCSV(self.salones, 4, columnas))
        self.boton_nuevo = tk.Button(self.frame_superior, text="Nuevo", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crear_formulario(columnas, "Salon", self.salones))
        self.boton_nuevo.pack(side="right", padx=5)
        self.botonExportacion.pack(side="right", padx=5)

    def mostrar_horarios(self):
        self.limpiar_panel()
        columnas = ("Horario", "Docente", "Curso", "Salón")
        self.tabla_actual = self.crear_tabla(self.tabla_actual, self.frame_tabla, columnas, self.AsignacionDocentes)
        self.botonCrear = tk.Button(self.frame_superior, text="Crear", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.crearHorario())
        self.botonCrear.pack(side="right", padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazAcademica(root)
    root.mainloop()