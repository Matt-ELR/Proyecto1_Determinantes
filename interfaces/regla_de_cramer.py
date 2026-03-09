# Bibliotecas
import tkinter as tk
from tkinter import ttk, messagebox
import geometria

#Frame
class ReglaDeCramerFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Titulo
        ttk.Label(self, text="Regla de Cramer", font=("Times New Roman", 16, "bold")).pack(pady=10)

        # Selector de metodo determinante
        select_frame = ttk.Frame(self)
        select_frame.pack(pady=10)
        ttk.Label(select_frame, text="Metodo de calculo:").pack(side="left", padx=5)
        self.metodo_var = tk.StringVar(value="Eliminación Gauss")
        self.combo_metodo = ttk.Combobox(select_frame, textvariable=self.metodo_var,
                                         values=["Eliminación Gauss", "Formula de Laplace"], 
                                         width=18, state="readonly")
        self.combo_metodo.pack(side="left", padx=5)

        # Selector de tamaño del sistema
        ttk.Label(select_frame, text="Tamaño del sistema (n):").pack(side="left", padx=5)
        self.n_var = tk.StringVar(value="3")
        self.combo_n = ttk.Combobox(select_frame, textvariable=self.n_var, 
                                    values=["2", "3", "4", "5"], 
                                    width=3, state="readonly")
        self.combo_n.pack(side="left", padx=5)
        self.combo_n.bind("<<ComboboxSelected>>", self.generar_matriz)

        # Matriz dinamica
        self.matrix_container = ttk.Frame(self)
        self.matrix_container.pack(pady=15, padx=20)
        self.matrix_entries = []
        self.vector_entries = []

        # Contenedor de botones
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Resolver", command=self.resolver).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar_campos).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Menú Principal", 
                   command=lambda: controller.show_frame("MenuFrame")).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Salir", command=self.quit).pack(side="left", padx=5)

        # Resultados
        self.res_label = ttk.Label(self, text="", font=("Times New Roman", 11, "bold"))
        self.res_label.pack(pady=10)

        self.generar_matriz()

    def generar_matriz(self, event=None):
        for widget in self.matrix_container.winfo_children():
            widget.destroy()
        
        n = int(self.n_var.get())
        self.matrix_entries, self.vector_entries = [], []

        #Dibujar Interfaz de Matriz
        for i in range(n):
            row_widgets = []
            ttk.Label(self.matrix_container, text="|").grid(row=i, column=0)
            for j in range(n):
                e = ttk.Entry(self.matrix_container, width=5)
                e.grid(row=i, column=j+1, padx=2, pady=2)
                row_widgets.append(e)
            self.matrix_entries.append(row_widgets)
            
            # Vector b (Separado visualmente)
            ttk.Label(self.matrix_container, text="|").grid(row=i, column=n+1)
            be = ttk.Entry(self.matrix_container, width=5, foreground="brown")
            be.grid(row=i, column=n+2, padx=5, pady=2)
            self.vector_entries.append(be)
            ttk.Label(self.matrix_container, text="|").grid(row=i, column=n+3)

    def resolver(self):
        try:
            # Metodo Determinante
            metodo_func = geometria.det_gauss if self.metodo_var.get() == "Eliminación Gauss" else geometria.det_laplace
            
            # Estracción de Datos
            A = [[float(e.get()) for e in fila] for fila in self.matrix_entries]
            b = [float(e.get()) for e in self.vector_entries]

            # Resultado
            soluciones = geometria.regla_de_cramer(A, b, metodo_func)
            res_text = "Soluciones: " + ", ".join([f"x{i+1}={val:.6g}" for i, val in enumerate(soluciones)])
            self.res_label.config(text=res_text, foreground="#0056b3")

        except ValueError:
            messagebox.showerror("Error", "Llene todos los campos con valores numéricos.")
        except Exception as e:
            messagebox.showwarning("Cramer", str(e))

    def limpiar_campos(self):
        for fila in self.matrix_entries:
            for e in fila: e.delete(0, tk.END)
        for e in self.vector_entries: e.delete(0, tk.END)
        self.res_label.config(text="")