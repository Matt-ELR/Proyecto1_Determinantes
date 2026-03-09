import tkinter as tk
from tkinter import ttk, messagebox
import geometria

class CoplanaridadFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Titulo
        ttk.Label(self, text="Prueba de Coplanaridad (3D)", font=("Times New Roman", 16, "bold")).pack(pady=15)
        ttk.Label(self, text="Si el det = 0, los 4 puntos están en el mismo plano.", 
                  font=("Times New Roman", 10, "italic")).pack(pady=5)

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

        # Encabezados
        for j, txt in enumerate(["X", "Y", "Z", "1"]):
            ttk.Label(matrix_frame, text=txt, font=("Times New Roman", 10, "bold")).grid(row=0, column=j+1, pady=5)

        # Barra izquierda del determinante
        ttk.Label(matrix_frame, text="|", font=("Times New Roman", 28)).grid(row=1, column=0, rowspan=4)

        # Matriz
        self.entries = []
        for i in range(4):
            row_entries = []
            for j in range(3):
                e = ttk.Entry(matrix_frame, width=6)
                e.grid(row=i+1, column=j+1, padx=4, pady=3)
                row_entries.append(e)

            ttk.Label(matrix_frame, text="1").grid(row=i+1, column=4, padx=5)
            self.entries.append(row_entries)

        # Barra derecha del determinante
        ttk.Label(matrix_frame, text="|", font=("Times New Roman", 28)).grid(row=1, column=5, rowspan=4)

        # Botones
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=25)

        ttk.Button(btn_frame, text="Verificar", command=self.verificar).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar_campos).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Volver (3D)", 
                   command=lambda: controller.show_frame("Geometria3DFrame")).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Menú Principal", 
                   command=lambda: controller.show_frame("MenuFrame")).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Salir", command=self.quit).pack(side="left", padx=5)

        # Resultado
        self.res_label = ttk.Label(self, text="", font=("Times New Roman", 13, "bold"))
        self.res_label.pack(pady=10)

    def verificar(self):
        try:
            puntos = [[float(e.get()) for e in row] for row in self.entries]

            metodo_func = geometria.det_gauss if self.metodo_var.get() == "Eliminación Gauss" else geometria.det_laplace

            es_coplanar = geometria.son_coplanares(puntos, metodo_func)

            if es_coplanar:
                self.res_label.config(text="¡Son Coplanares! (Pertenecen al mismo plano)")
            else:
                self.res_label.config(text="No son Coplanares")

        except ValueError:
            messagebox.showerror("Error", "Ingresa coordenadas válidas en todos los campos.")

    def limpiar_campos(self):
        for row in self.entries:
            for e in row: e.delete(0, tk.END)
        self.res_label.config(text="")