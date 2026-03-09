import tkinter as tk
from tkinter import ttk, messagebox
import geometria

class TrianguloFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        # Titulo
        ttk.Label(self, text="Área de Triángulos", font=("Times New Roman", 16, "bold")).pack(pady=10)
        ttk.Label(self, text="Introduce los puntos del triángulo", font=("Times New Roman", 10, "italic")).pack(pady=2)

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
        matrix_frame.pack(pady=15)

        # Barra izquierda del determinante
        ttk.Label(matrix_frame, text="|", font=("Times New Roman", 28)).grid(row=0, column=0, rowspan=3)

        # Matriz
        self.entries = []
        for i in range(3):
            row_entries = []
            ex = ttk.Entry(matrix_frame, width=6)
            ey = ttk.Entry(matrix_frame, width=6)
            ex.grid(row=i, column=1, padx=5, pady=3)
            ey.grid(row=i, column=2, padx=5, pady=3)
            ttk.Label(matrix_frame, text="1").grid(row=i, column=3, padx=5)
            row_entries.extend([ex, ey])
            self.entries.append(row_entries)

        # Barra derecha del determinante
        ttk.Label(matrix_frame, text="|", font=("Times New Roman", 28)).grid(row=0, column=4, rowspan=3)

        # Botones
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=25)

        ttk.Button(btn_frame, text="Calcular", command=self.calcular).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar_campos).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Volver (2D)", 
                   command=lambda: controller.show_frame("Geometria2DFrame")).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Menú Principal", 
                   command=lambda: controller.show_frame("MenuFrame")).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Salir", command=self.quit).pack(side="left", padx=5)

        # Resultado
        self.res_det = ttk.Label(self, text="", font=("Times New Roman", 11))
        self.res_det.pack(pady=2)
        self.res_final = ttk.Label(self, text="", font=("Times New Roman", 13, "bold"))
        self.res_final.pack(pady=5)

    def calcular(self):
        try:
            # Metodo Determinante
            metodo_func = geometria.det_gauss if self.metodo_var.get() == "Eliminación Gauss" else geometria.det_laplace
            
            # Estracción de Datos
            matriz = [[float(row[0].get()), float(row[1].get())] for row in self.entries]

            # Cálculo
            area = geometria.area_triangulo(matriz, metodo_func)

            # Mostrar resultados detallados
            self.res_final.config(text=f"Área = {area:.6g} u²")

        except ValueError:
            messagebox.showerror("Error", "Asegúrate de que todos los puntos tengan coordenadas numéricas.")
        except Exception as e:
            messagebox.showerror("Error en Cálculo", f"Ocurrió un error inesperado: {e}")

    def limpiar_campos(self):
        for row in self.entries:
            for e in row:
                e.delete(0, tk.END)
        self.res_det.config(text="")
        self.res_final.config(text="")