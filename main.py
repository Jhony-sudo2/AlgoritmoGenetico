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
        self.asignacionManuales = []
        self.cursosSeleccionados = []
        self.docentesSeleccionados = []
        self.NoPoblacion = 20
        self.Generaciones = 50
        self.salones = []
        self.cursos = []
        self.docentes = []
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

        self.menu_options = [
            ("Cursos", self.mostrar_cursos),
            ("Docentes", self.mostrar_docentes),
            ("Asignación Docentes", self.mostrar_asignacion),
            ("Salones", self.mostrar_salones),
            ("Asignación Manual", self.mostrar_asignacionesManuales),
            ("Seleccion", self.seleccion),
            ("Generación Horario", self.mostrar_horarios),
            ("Algoritmo", self.configurarAlgoritmo)
        ]

        self.active_menu_index = tk.IntVar(value=-1)  
        

        for idx, (label, command) in enumerate(self.menu_options):
            def make_command(cmd=command, index=idx):
                return lambda: self.set_active_menu(index, cmd)
            self.menu_bar.add_command(
                label=label,
                command=make_command()
            )


        self.frame_superior = tk.Frame(self.root)
        self.frame_superior.pack(fill="x", padx=5, pady=5)
        self.active_option_label = tk.Label(
            self.frame_superior,
            text="Opción activa: Ninguna",
            font=("Arial", 12, "bold"),
            fg="blue",
            bg="white"
        )
        self.active_option_label.pack(side="left", padx=5)
        self.frame_tabla = tk.Frame(self.root, bg="lightgray")
        self.frame_tabla.pack(fill="both", expand=True, padx=5, pady=5)

        self.tabla_actual = None
        self.boton_nuevo = None
        self.botonExportacion = None
        self.botonCrear = None
        self.botonAsignacion = None
        self.mostrar_docentes()
        self.set_active_menu(1) 

    def set_active_menu(self, index, command=None):
        self.active_menu_index.set(index)
        option_name = self.menu_options[index][0]
        self.active_option_label.config(text=f"{option_name}")
        if command:
            command()

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
        self.AsignacionDocentes = []
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
            self.asignacionManuales.append(asignacion)

            messagebox.showinfo("Éxito", f"Curso '{curso_nombre}' asignado al salón '{salon_nombre}' correctamente.")
            ventana.destroy()

            self.mostrar_asignacionesManuales()

        tk.Button(frame, text="Guardar Asignación", bg="#008080", fg="white", font=("Arial", 10, "bold"), command=guardar_asignacion).pack(pady=10)

    def seleccion(self):
        self.limpiar_panel()

        frame_principal = tk.Frame(self.frame_tabla)
        frame_principal.pack(fill="both", expand=True)

        tk.Label(frame_principal, text="Seleccionar Docentes", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)

        canvas_docentes = tk.Canvas(frame_principal)
        scrollbar_docentes = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas_docentes.yview)
        frame_docentes = tk.Frame(canvas_docentes)

        canvas_docentes.configure(yscrollcommand=scrollbar_docentes.set)

        scrollbar_docentes.pack(side="right", fill="y")
        canvas_docentes.pack(side="left", fill="both", expand=True)
        canvas_docentes.create_window((0, 0), window=frame_docentes, anchor="nw")

        seleccionados_docentes = {}
        checkbuttons_docentes = {}  # Checkbutton de docentes

        for docente in self.docentes:
            var = tk.BooleanVar(value=docente in self.docentesSeleccionados)
            seleccionados_docentes[docente.codigo] = var

            frame_fila = tk.Frame(frame_docentes)
            frame_fila.pack(fill="x", padx=5, pady=2)

            check = tk.Checkbutton(frame_fila, variable=var)
            check.pack(side="left")
            checkbuttons_docentes[docente.codigo] = check

            tk.Label(frame_fila, text=f"{docente.nombre} ({docente.codigo})").pack(side="left", padx=5)

        frame_docentes.update_idletasks()
        canvas_docentes.configure(scrollregion=canvas_docentes.bbox("all"))

    # Checkbutton seleccionar todos los docentes
        seleccionar_todos_docentes_var = tk.BooleanVar(value=all(var.get() for var in seleccionados_docentes.values()))
        def toggle_seleccionar_todos_docentes():
            estado = seleccionar_todos_docentes_var.get()
            for var in seleccionados_docentes.values():
                var.set(estado)

        tk.Checkbutton(frame_principal, text="Seleccionar todos los docentes", variable=seleccionar_todos_docentes_var, 
                   command=toggle_seleccionar_todos_docentes).pack(anchor="w", padx=5, pady=5)

        tk.Label(frame_principal, text="Seleccionar Cursos", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)

        canvas_cursos = tk.Canvas(frame_principal)
        scrollbar_cursos = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas_cursos.yview)
        frame_cursos = tk.Frame(canvas_cursos)

        canvas_cursos.configure(yscrollcommand=scrollbar_cursos.set)

        scrollbar_cursos.pack(side="right", fill="y")
        canvas_cursos.pack(side="left", fill="both", expand=True)
        canvas_cursos.create_window((0, 0), window=frame_cursos, anchor="nw")

        seleccionados_cursos = {}
        checkbuttons_cursos = {}  # Checkbutton de cursos

        for curso in self.cursos:
            var = tk.BooleanVar(value=curso in self.cursosSeleccionados)
            seleccionados_cursos[curso.codigo] = var

            frame_fila = tk.Frame(frame_cursos)
            frame_fila.pack(fill="x", padx=5, pady=2)

            check = tk.Checkbutton(frame_fila, variable=var)
            check.pack(side="left")
            checkbuttons_cursos[curso.codigo] = check
            tk.Label(frame_fila, text=f"{curso.nombre} ({curso.codigo})").pack(side="left", padx=5)

        frame_cursos.update_idletasks()
        canvas_cursos.configure(scrollregion=canvas_cursos.bbox("all"))

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
        if not self.docentesSeleccionados:
            continuar = False
            mensaje = f"No hay docentes ingresados"
        if not self.cursosSeleccionados:
            continuar = False
            mensaje = f"No hay cursos ingresados"
        if not self.salones:
            continuar = False
            mensaje = f"No hay salones ingresados"
        if continuar:
            for i,curso in enumerate(self.cursosSeleccionados):
                docentes_posibles = [j for j, d in enumerate(self.docentesSeleccionados) if i in d.cursos_posibles]
                if not docentes_posibles:
                    mensaje = f"No hay docentes disponibles para {curso.nombre}"
                    continuar = False
        if continuar:
            algoritmo = AlgoritmoGenetico(self.cursosSeleccionados,self.docentesSeleccionados,self.salones,self.asignacionManuales,self.NoPoblacion,self.Generaciones)
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
                if docente.cursos_posibles:
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
            if col.lower() == "tipo": 
                entrada = ttk.Combobox(ventana_nuevo, values=["obligatorio", "optativo"], state="readonly")
                entrada.pack()
                entrada.set("obligatorio")  
            else:
                # Para otras columnas, usar un Entry normal
                entrada = tk.Entry(ventana_nuevo)
                entrada.pack()
            entradas[col] = entrada

        def guardar():
            valores = tuple(entradas[col].get() for col in columnas)
            valores_dict = {col: entradas[col].get() for col in columnas}
            if titulo == "Asignacion Docente":
                indice = []
                docentetmp = None
                for i,curso in enumerate(self.cursos):
                    if curso.codigo == valores_dict.get("cursos"):
                        print("curso archivado")
                        indice.append(i)
                for docente in self.docentes:
                    if docente.codigo == valores_dict.get("docente"):
                        print("docente archivado")
                        docentetmp = docente
                if not indice and not docentetmp:
                    messagebox.showwarning("Error","el curso o docente no existe")
                    return
                else:
                    for indicetmp in indice:
                        if not indice in docentetmp.cursos_posibles:
                            docentetmp.cursos_posibles.append(indicetmp)
                        else:
                            messagebox.showerror("Error","El curso ya esta asignado al docente")
                    self.mostrar_asignacion()
                    ventana_nuevo.destroy()
                pass
            else:

                clase = globals()[titulo]
                error = False
                objeto = None
                try:
                    objeto = clase(**valores_dict)
                    if isinstance(objeto,Curso):
                        curso_indices = {curso.codigo: curso for curso in self.cursos}
                        if objeto.codigo in curso_indices and objeto.seccion == curso_indices.get(objeto.codigo).seccion:
                            error = True
                            mensaje = "Ya hay un curso con el codigo: " + str(objeto.codigo)
                        elif objeto.codigo in curso_indices and objeto.seccion != curso_indices.get(objeto.codigo).seccion:
                            nuevaSeccion =  curso_indices.get(objeto.codigo)
                            objeto.nombre = nuevaSeccion.nombre
                            objeto.semestre =nuevaSeccion.semestre
                            objeto.carrera = nuevaSeccion.carrera
                            objeto.tipo =  nuevaSeccion.tipo

                    if isinstance(objeto,Docente):
                        docente_indices = {docente.codigo:idx for idx, docente in enumerate(self.docentes)}
                        if objeto.codigo in docente_indices:
                            error = True
                            mensaje = "Ya hay un docente con el codigo: " + str(objeto.codigo)
                except Exception as e:
                    error = True
                    mensaje = "Error en formato de datos"
                    if titulo == "Curso":
                        mensaje = "Semestre tiene que ser un numero entero"
                    else:
                        mensaje = "Error en formato de hora (H:m) 24 horas" 
                    messagebox.showwarning("Error",mensaje)
                if error:
                    messagebox.showwarning("Erro",mensaje)
                else:
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
        if file_path:
            Archivos.leerCSV(file_path, listado, tipo,self.docentes,self.cursos)
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

    def mostrar_asignacionesManuales(self):
        self.limpiar_panel()
        columnas = ("Horario", "Docente", "Curso", "Salón")
        self.tabla_actual = self.crear_tabla(self.tabla_actual, self.frame_tabla, columnas, self.asignacionManuales)
        self.botonCrear = tk.Button(self.frame_superior, text="Crear", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.mostrar_asignacion_manual())
        self.botonCrear.pack(side="right", padx=5)
        self.boton_nuevo = tk.Button(self.frame_superior, text="Eliminar Configuraciones", bg="#008080", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: self.eliminarAsignacionesManuales())
        self.boton_nuevo.pack(side='right',padx=5)
    def eliminarAsignacionesManuales(self):
        self.asignacionManuales = []
        self.mostrar_asignacionesManuales()

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