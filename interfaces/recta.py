import tkinter as tk
from tkinter import ttk, messagebox
import geometria

class RectaFrame(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        # Titulo
        ttk.Label(self, text="Ecuación de la Recta (2D)", font=("Times New Roman", 16, "bold")).pack(pady=15)
        ttk.Label(self, text="Introduce dos puntos para generar la ecuación", font=("Times New Roman", 10, "italic")).pack(pady=5)

        # Seleccionar el Metodo Determinante
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

        # Encabezados
        ttk.Label(matrix_frame, text="x", font=("Times New Roman", 11, "italic")).grid(row=0, column=1)
        ttk.Label(matrix_frame, text="y", font=("Times New Roman", 11, "italic")).grid(row=0, column=2)
        ttk.Label(matrix_frame, text="1").grid(row=0, column=3)

        # Matriz
        self.entries = []
        for i in range(1, 3):
            ex = ttk.Entry(matrix_frame, width=6)
            ey = ttk.Entry(matrix_frame, width=6)
            ex.grid(row=i, column=1, padx=5, pady=3)
            ey.grid(row=i, column=2, padx=5, pady=3)
            ttk.Label(matrix_frame, text="1").grid(row=i, column=3, padx=5)
            self.entries.append([ex, ey])

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
        self.res_label = ttk.Label(self, text="", font=("Times New Roman", 12, "bold"))
        self.res_label.pack(pady=10)

    def calcular(self):
        try:
            p1 = [float(self.entries[0][0].get()), float(self.entries[0][1].get())]
            p2 = [float(self.entries[1][0].get()), float(self.entries[1][1].get())]

            if p1 == p2:
                messagebox.showwarning("Puntos iguales", "Introduce dos puntos distintos para definir una recta.")
                return

            metodo_func = geometria.det_gauss if self.metodo_var.get() == "Eliminación Gauss" else geometria.det_laplace

            resultado_texto = geometria.ecuacion_recta(p1, p2, metodo_func)
            self.res_label.config(text=f"Ecuación: {resultado_texto}")

        except ValueError:
            messagebox.showerror("Error", "Ingresa coordenadas numéricas válidas.")

    def limpiar_campos(self):
        for row in self.entries:
            for e in row: e.delete(0, tk.END)
        self.res_label.config(text="")