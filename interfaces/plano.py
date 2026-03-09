import tkinter as tk
from tkinter import ttk, messagebox
import geometria

class PlanoFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Titulo
        ttk.Label(self, text="Ecuación del Plano (3D)", font=("Times New Roman", 16, "bold")).pack(pady=10)
        ttk.Label(self, text="Determina Ax + By + Cz + D = 0 a partir de 3 puntos.", font=("Times New Roman", 10, "italic")).pack(pady=2)

        # Selector de metodo determinante
        select_frame = ttk.Frame(self)
        select_frame.pack(pady=10)
        ttk.Label(select_frame, text="Metodo de calculo:").pack(side="left", padx=5)
        self.metodo_var = tk.StringVar(value="Eliminación Gauss")
        self.combo_metodo = ttk.Combobox(select_frame, textvariable=self.metodo_var,
                                         values=["Eliminación Gauss", "Formula de Laplace"], 
                                         width=18, state="readonly")
        self.combo_metodo.pack(side="left", padx=5)

        # Marco para la matriz de determinantes
        matrix_frame = ttk.Frame(self)
        matrix_frame.pack(pady=10)

        # Barra izquierda del determinante
        ttk.Label(matrix_frame, text="|", font=("Times New Roman", 28)).grid(row=1, column=0, rowspan=4)

        # Encabezados
        simbolos = [("x", "italic"), ("y", "italic"), ("z", "italic"), ("1", "normal")]
        for j, (txt, style) in enumerate(simbolos):
            ttk.Label(matrix_frame, text=txt, font=("Arial", 11, style)).grid(row=0, column=j+1, padx=10)

        # Matriz
        self.entries = []
        for i in range(3):
            row_entries = []
            for j in range(3):
                e = ttk.Entry(matrix_frame, width=6)
                e.grid(row=i+1, column=j+1, padx=4, pady=3)
                row_entries.append(e)

            ttk.Label(matrix_frame, text="1").grid(row=i+1, column=4, padx=5)
            self.entries.append(row_entries)

        # Barra derecha del determinante
        ttk.Label(matrix_frame, text="|", font=("Times New Roman", 28)).grid(row=0, column=5, rowspan=4)

        # Botones
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=25)

        ttk.Button(btn_frame, text="Calcular", command=self.calcular).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar_campos).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Volver (3D)", 
                   command=lambda: controller.show_frame("Geometria3DFrame")).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Menú Principal", 
                   command=lambda: controller.show_frame("MenuFrame")).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Salir", command=self.quit).pack(side="left", padx=5)

        # Resultado
        self.res_label = ttk.Label(self, text="", font=("Times New Roman", 13, "bold"))
        self.res_label.pack(pady=10)

    def calcular(self):
        try:
            puntos = [[float(e.get()) for e in row] for row in self.entries]

            if puntos[0] == puntos[1] or puntos[0] == puntos[2] or puntos[1] == puntos[2]:
                messagebox.showwarning("Puntos Inválidos", "Se requieren 3 puntos distintos para definir un plano.")
                return

            metodo_func = geometria.det_gauss if self.metodo_var.get() == "Eliminación Gauss" else geometria.det_laplace

            resultado_texto = geometria.ecuacion_plano(puntos, metodo_func)
            self.res_label.config(text=f"Plano: {resultado_texto}")

            resultado_texto = geometria.ecuacion_plano(puntos, metodo_func)
            self.res_label.config(text=f"Plano: {resultado_texto}")

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa coordenadas numéricas válidas.")
        except Exception as e:
            messagebox.showerror("Error de Cálculo", str(e))

    def limpiar_campos(self):
        for row in self.entries:
            for e in row: e.delete(0, tk.END)
        self.res_label.config(text="")