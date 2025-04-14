import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from algoritmo import Archivos
from algoritmo import main
from algoritmo.cromosoma import Cromosoma, Gen
from algoritmo.datos import *
from algoritmo.main import AlgoritmoGenetico

class InterfazAcademica:
    def __init__(self, root):
        self.AsignacionDocentes = []
        self.cursosSeleccionados = []
        self.docentesSeleccionados = []
        self.NoPoblacion = 20
        self.Generaciones = 50
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
            Curso("Programación I", "SYS101", "Ingeniería en Sistemas", "1", "A", "obligatorio"),
            Curso("Programación II", "SYS102", "Ingeniería en Sistemas", "2", "B", "obligatorio"),
            Curso("Bases de Datos", "SYS103", "Ingeniería en Sistemas", "3", "A", "obligatorio"),
            Curso("Algoritmos Avanzados", "SYS104", "Ingeniería en Sistemas", "4", "B", "optativo"),
            Curso("Inteligencia Artificial", "SYS105", "Ingeniería en Sistemas", "5", "C", "optativo"),
            Curso("Redes de Computadoras", "SYS106", "Ingeniería en Sistemas", "6", "A", "obligatorio"),
            Curso("Sistemas Operativos", "SYS107", "Ingeniería en Sistemas", "3", "B", "obligatorio"),
            Curso("Ingeniería de Software", "SYS108", "Ingeniería en Sistemas", "4", "A", "obligatorio"),
            Curso("Ciberseguridad", "SYS109", "Ingeniería en Sistemas", "5", "B", "optativo"),
            Curso("Proyectos de TI", "SYS110", "Ingeniería en Sistemas", "6", "C", "obligatorio"),
            Curso("Cálculo Estructural", "CIV101", "Ingeniería Civil", "1", "A", "obligatorio"),
            Curso("Mecánica de Suelos", "CIV102", "Ingeniería Civil", "2", "B", "obligatorio"),
            Curso("Diseño de Puentes", "CIV103", "Ingeniería Civil", "3", "A", "optativo"),
            Curso("Hidráulica", "CIV104", "Ingeniería Civil", "4", "B", "obligatorio"),
            Curso("Construcción Sostenible", "CIV105", "Ingeniería Civil", "5", "A", "optativo"),
            Curso("Geotecnia", "CIV106", "Ingeniería Civil", "3", "B", "obligatorio"),
            Curso("Topografía", "CIV107", "Ingeniería Civil", "2", "A", "obligatorio"),
            Curso("Materiales de Construcción", "CIV108", "Ingeniería Civil", "1", "B", "obligatorio"),
            Curso("Gestión de Proyectos", "CIV109", "Ingeniería Civil", "5", "C", "obligatorio"),
            Curso("Diseño Sísmico", "CIV110", "Ingeniería Civil", "6", "A", "optativo"),
            Curso("Biología Celular", "BIO101", "Ciencias Biológicas", "1", "A", "obligatorio"),
            Curso("Genética", "BIO102", "Ciencias Biológicas", "2", "B", "obligatorio"),
            Curso("Ecología", "BIO103", "Ciencias Biológicas", "3", "A", "optativo"),
            Curso("Microbiología", "BIO104", "Ciencias Biológicas", "4", "B", "obligatorio"),
            Curso("Biotecnología", "BIO105", "Ciencias Biológicas", "5", "C", "optativo"),
            Curso("Fisiología Vegetal", "BIO106", "Ciencias Biológicas", "3", "A", "obligatorio"),
            Curso("Zoología", "BIO107", "Ciencias Biológicas", "2", "B", "obligatorio"),
            Curso("Bioquímica", "BIO108", "Ciencias Biológicas", "4", "A", "obligatorio"),
            Curso("Evolución", "BIO109", "Ciencias Biológicas", "5", "B", "optativo"),
            Curso("Biología Marina", "BIO110", "Ciencias Biológicas", "6", "C", "obligatorio"),
            Curso("Introducción a la Administración", "ADM101", "Administración de Empresas", "1", "A", "obligatorio"),
            Curso("Contabilidad Básica", "ADM102", "Administración de Empresas", "2", "B", "obligatorio"),
            Curso("Marketing", "ADM103", "Administración de Empresas", "3", "A", "obligatorio"),
            Curso("Finanzas Corporativas", "ADM104", "Administración de Empresas", "4", "B", "obligatorio"),
            Curso("Gestión de Recursos Humanos", "ADM105", "Administración de Empresas", "5", "C", "optativo"),
            Curso("Economía Empresarial", "ADM106", "Administración de Empresas", "3", "A", "obligatorio"),
            Curso("Estrategia Empresarial", "ADM107", "Administración de Empresas", "4", "B", "obligatorio"),
            Curso("Emprendimiento", "ADM108", "Administración de Empresas", "5", "A", "optativo"),
            Curso("Comportamiento Organizacional", "ADM109", "Administración de Empresas", "2", "B", "obligatorio"),
            Curso("Logística y Cadena de Suministro", "ADM110", "Administración de Empresas", "6", "C", "obligatorio")
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
        for i,col in enumerate(columnas):
            tk.Label(self.frame_tabla, text=f"{col}:").pack()
            entrada = tk.Entry(self.frame_tabla)
            entrada.pack()
            if i == 0:
                entrada.insert(0,self.NoPoblacion)
            else:
                entrada.insert(0,self.Generaciones)
            entradas[col] = entrada
        
        def guardar():
            valores = tuple(entradas[col].get() for col in columnas)
            if valores[0].isdigit() and valores[1].isdigit():
                self.NoPoblacion = int(valores[0])
                self.Generaciones = int(valores[1])
                messagebox.showinfo("OK","Configuracion guardada exitosamente")
            else:
                messagebox.showwarning("Error", "Por favor ingrese numeros entero")

            print("poblacion: ",self.NoPoblacion, " generaciones : ", self.Generaciones)
        tk.Button(self.frame_tabla, text="Guardar", command=guardar).pack(pady=10)

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

        # Frame principal para contener las dos secciones (docentes y cursos)
        frame_principal = tk.Frame(self.frame_tabla)
        frame_principal.pack(fill="both", expand=True)

        # --- Sección de Docentes ---
        tk.Label(frame_principal, text="Seleccionar Docentes", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)

        # Canvas y Scrollbar para docentes
        canvas_docentes = tk.Canvas(frame_principal)
        scrollbar_docentes = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas_docentes.yview)
        frame_docentes = tk.Frame(canvas_docentes)

        canvas_docentes.configure(yscrollcommand=scrollbar_docentes.set)

        scrollbar_docentes.pack(side="right", fill="y")
        canvas_docentes.pack(side="left", fill="both", expand=True)
        canvas_docentes.create_window((0, 0), window=frame_docentes, anchor="nw")

        seleccionados_docentes = {}
        checkbuttons_docentes = {}  # Para almacenar los Checkbutton de docentes

        for docente in self.docentes:
            var = tk.BooleanVar(value=docente in self.docentesSeleccionados)
            seleccionados_docentes[docente.codigo] = var

            # Frame para cada fila de docente
            frame_fila = tk.Frame(frame_docentes)
            frame_fila.pack(fill="x", padx=5, pady=2)

            # Checkbutton para el docente
            check = tk.Checkbutton(frame_fila, variable=var)
            check.pack(side="left")
            checkbuttons_docentes[docente.codigo] = check

            # Etiqueta con nombre y código del docente
            tk.Label(frame_fila, text=f"{docente.nombre} ({docente.codigo})").pack(side="left", padx=5)

    # Ajustar el área de desplazamiento del Canvas
        frame_docentes.update_idletasks()
        canvas_docentes.configure(scrollregion=canvas_docentes.bbox("all"))

    # Checkbutton para seleccionar todos los docentes
        seleccionar_todos_docentes_var = tk.BooleanVar(value=all(var.get() for var in seleccionados_docentes.values()))
        def toggle_seleccionar_todos_docentes():
            estado = seleccionar_todos_docentes_var.get()
            for var in seleccionados_docentes.values():
                var.set(estado)

        tk.Checkbutton(frame_principal, text="Seleccionar todos los docentes", variable=seleccionar_todos_docentes_var, 
                   command=toggle_seleccionar_todos_docentes).pack(anchor="w", padx=5, pady=5)

    # --- Sección de Cursos ---
        tk.Label(frame_principal, text="Seleccionar Cursos", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)

    # Canvas y Scrollbar para cursos
        canvas_cursos = tk.Canvas(frame_principal)
        scrollbar_cursos = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas_cursos.yview)
        frame_cursos = tk.Frame(canvas_cursos)

        canvas_cursos.configure(yscrollcommand=scrollbar_cursos.set)

        scrollbar_cursos.pack(side="right", fill="y")
        canvas_cursos.pack(side="left", fill="both", expand=True)
        canvas_cursos.create_window((0, 0), window=frame_cursos, anchor="nw")

        seleccionados_cursos = {}
        checkbuttons_cursos = {}  # Para almacenar los Checkbutton de cursos

        for curso in self.cursos:
            var = tk.BooleanVar(value=curso in self.cursosSeleccionados)
            seleccionados_cursos[curso.codigo] = var

            # Frame para cada fila de curso
            frame_fila = tk.Frame(frame_cursos)
            frame_fila.pack(fill="x", padx=5, pady=2)

            # Checkbutton para el curso
            check = tk.Checkbutton(frame_fila, variable=var)
            check.pack(side="left")
            checkbuttons_cursos[curso.codigo] = check

            # Etiqueta con nombre y código del curso
            tk.Label(frame_fila, text=f"{curso.nombre} ({curso.codigo})").pack(side="left", padx=5)

    # Ajustar el área de desplazamiento del Canvas
        frame_cursos.update_idletasks()
        canvas_cursos.configure(scrollregion=canvas_cursos.bbox("all"))

    # Checkbutton para seleccionar todos los cursos
        seleccionar_todos_cursos_var = tk.BooleanVar(value=all(var.get() for var in seleccionados_cursos.values()))
        def toggle_seleccionar_todos_cursos():
            estado = seleccionar_todos_cursos_var.get()
            for var in seleccionados_cursos.values():
                var.set(estado)

        tk.Checkbutton(frame_principal, text="Seleccionar todos los cursos", variable=seleccionar_todos_cursos_var, 
                   command=toggle_seleccionar_todos_cursos).pack(anchor="w", padx=5, pady=5)

        def guardar_seleccion():
            self.docentesSeleccionados = []
            self.cursosSeleccionados = []
            self.AsignacionDocentes = []
            self.docentesSeleccionados = [docente for docente in self.docentes if seleccionados_docentes[docente.codigo].get()]
            self.cursosSeleccionados = [curso for curso in self.cursos if seleccionados_cursos[curso.codigo].get()]

            if not self.docentesSeleccionados:
                messagebox.showwarning("Advertencia", "Debe seleccionar al menos un docente.")
                return
            if not self.cursosSeleccionados:
                messagebox.showwarning("Advertencia", "Debe seleccionar al menos un curso.")
                return

            messagebox.showinfo("Éxito", f"Se seleccionaron {len(self.docentesSeleccionados)} docentes y {len(self.cursosSeleccionados)} cursos.")

        self.botonAsignacion = tk.Button(self.frame_superior, text="Guardar selección", bg="#008080", fg="white", font=("Arial", 10, "bold"), 
              command=guardar_seleccion)
        self.botonAsignacion.pack(side="right",padx=5)
    def crearHorario(self):
        if not self.cursosSeleccionados:
            self.cursosSeleccionados = self.cursos
        if not self.docentesSeleccionados:
            self.docentesSeleccionados = self.docentes
        continuar = True
        mensaje = ""
        for i,curso in enumerate(self.cursosSeleccionados):
            docentes_posibles = [j for j, d in enumerate(self.docentesSeleccionados) if i in d.cursos_posibles]
            if not docentes_posibles:
                mensaje = f"No hay docentes disponibles para {curso.nombre}"
                continuar = False
        if continuar:
            algoritmo = AlgoritmoGenetico(self.cursosSeleccionados,self.docentesSeleccionados,self.salones,self.AsignacionDocentes,self.NoPoblacion,self.Generaciones)
            self.AsignacionDocentes = algoritmo.Iniciar()
            self.mostrar_horarios()
        else:
            messagebox.showerror("Error",mensaje)
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
            if isinstance(datos,Cromosoma):
                for gen in datos.Genes:
                    valorestmp = (Cromosoma.HORARIOS[gen.horario], self.docentesSeleccionados[gen.docente].nombre, self.cursosSeleccionados[gen.curso].nombre, self.salones[gen.salon].nombre)
                    tabla_actual.insert("", "end", values=valorestmp)
            else:
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
            if titulo == "Asignacion Docente":
                indice = None
                docentetmp = None
                for i,curso in enumerate(self.cursos):
                    if curso.codigo == valores_dict.get("cursos"):
                        indice = i
                for docente in self.docentes:
                    if docente.codigo == valores_dict.get("docente"):
                        docentetmp = docente
                if not indice and not docentetmp:
                    messagebox.showwarning("Error","el curso o docente no existe")
                    return
                else:
                    if not indice in docentetmp.cursos_posibles:
                        docentetmp.cursos_posibles.append(indice)
                        messagebox.showinfo("OK","Curso asignado correctamente")
                        self.mostrar_asignacion()
                    else:
                        messagebox.showerror("Error","El curso ya esta asignado al docente")
                    ventana_nuevo.destroy()
                pass
            else:
                clase = globals()[titulo]
                error = False
                objeto = None
                try:
                    objeto = clase(**valores_dict)
                    
                except:
                    error = True
                    mensaje = "Error en formato de datos"
                    if titulo == "Curso":
                        mensaje = "Semestre tiene que ser un numero entero"
                    else:
                        mensaje = "Error en formato de hora (H:m) 24 horas" 
                    messagebox.showwarning("Error",mensaje)
                print("error: ",error)
                if error == False:
                    arreglo.append(objeto)
                    self.tabla_actual.insert("", "end", values=valores)
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
                                     command=lambda: self.crear_formulario(columnas, "Asignacion Docente", self.cursos))
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