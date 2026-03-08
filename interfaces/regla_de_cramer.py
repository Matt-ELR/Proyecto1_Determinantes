import tkinter as tk
from tkinter import ttk, messagebox
import geometria # Donde tienes det_gauss y regla_de_cramer

class ReglaDeCramerFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # --- CABECERA ---
        titulo = ttk.Label(self, text="Regla de Cramer", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        # --- SELECTOR DE TAMAÑO ---
        select_frame = ttk.Frame(self)
        select_frame.pack(pady=5)
        
        ttk.Label(select_frame, text="Tamaño del sistema (n):").pack(side="left", padx=5)
        self.n_var = tk.StringVar(value="3") # Valor por defecto
        self.combo_n = ttk.Combobox(select_frame, textvariable=self.n_var, values=["2", "3", "4", "5", "6"], width=5, state="readonly")
        self.combo_n.pack(side="left", padx=5)
        self.combo_n.bind("<<ComboboxSelected>>", self.generar_matriz)

        # --- CONTENEDOR DE LA MATRIZ (Dinámico) ---
        # Usamos un Canvas si piensas llegar a n=10 para que tenga scroll, 
        # pero para n=6 un Frame normal basta.
        self.matrix_container = ttk.Frame(self)
        self.matrix_container.pack(pady=20, padx=20)

        # Listas para guardar las referencias a los Entry
        self.matrix_entries = [] # Matriz A
        self.vector_entries = [] # Vector b (términos independientes)

        # --- BOTONES ---
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Resolver Sistema", command=self.resolver).pack(side="left", padx=10)
        ttk.Button(btn_frame, text="Volver", command=lambda: controller.show_frame("MenuFrame")).pack(side="left")

        # --- RESULTADOS ---
        self.res_label = ttk.Label(self, text="", font=("Arial", 11, "bold"), foreground="#0056b3")
        self.res_label.pack(pady=10)

        # Generar la matriz inicial (3x3)
        self.generar_matriz()

    def generar_matriz(self, event=None):
        # Limpiar lo que haya antes
        for widget in self.matrix_container.winfo_children():
            widget.destroy()
        
        n = int(self.n_var.get())
        self.matrix_entries = []
        self.vector_entries = []

        # Dibujar encabezados (x1, x2... | b)
        for j in range(n):
            ttk.Label(self.matrix_container, text=f"x{j+1}", font=("Arial", 9, "italic")).grid(row=0, column=j+1)
        ttk.Label(self.matrix_container, text="|  b", font=("Arial", 9, "bold")).grid(row=0, column=n+1)

        # Crear filas
        for i in range(n):
            row_widgets = []
            ttk.Label(self.matrix_container, text="|").grid(row=i+1, column=0) # Barra visual
            
            for j in range(n):
                e = ttk.Entry(self.matrix_container, width=5)
                e.grid(row=i+1, column=j+1, padx=2, pady=2)
                row_widgets.append(e)
            
            self.matrix_entries.append(row_widgets)
            
            # Entrada para el vector b
            ttk.Label(self.matrix_container, text="|").grid(row=i+1, column=n) # Separador
            be = ttk.Entry(self.matrix_container, width=5, foreground="brown")
            be.grid(row=i+1, column=n+1, padx=5, pady=2)
            self.vector_entries.append(be)
            
            ttk.Label(self.matrix_container, text="|").grid(row=i+1, column=n+2) # Barra visual

    def resolver(self):
        try:
            n = int(self.n_var.get())
            A = []
            b = []

            # Extraer datos de A
            for i in range(n):
                fila = [float(self.matrix_entries[i][j].get()) for j in range(n)]
                A.append(fila)
                b.append(float(self.vector_entries[i].get()))

            # Llamar a tu lógica (debe estar en geometria.py)
            soluciones = geometria.regla_de_cramer(A, b)
            
            # Formatear salida
            res_text = "Soluciones: " + ", ".join([f"x{i+1}={val:.2f}" for i, val in enumerate(soluciones)])
            self.res_label.config(text=res_text, foreground="#0056b3")

        except ValueError as e:
            if "no tiene solución única" in str(e):
                messagebox.showwarning("Cramer", "El sistema no tiene solución única (Det = 0)")
            else:
                messagebox.showerror("Error", "Asegúrate de llenar todos los campos con números.")