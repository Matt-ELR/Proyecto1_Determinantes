import tkinter as tk
from tkinter import ttk, messagebox
import geometria 

class TetraedroFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        ttk.Label(self, text="Volumen de un Tetraedro (3D)", font=("Times New Roman", 16, "bold")).pack(pady=10)
        ttk.Label(self, text="Introduce los 4 puntos en el espacio.", font=("Times New Roman", 10, "italic")).pack(pady=2)
        
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

        ttk.Button(btn_frame, text="Calcular", command=self.calcular).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar_campos).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Volver (3D)", 
                   command=lambda: controller.show_frame("Geometria3DFrame")).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Menú Principal", 
                   command=lambda: controller.show_frame("MenuFrame")).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Salir", command=self.quit).pack(side="left", padx=5)

        # Resultado
        self.resultado = ttk.Label(self, text="", font=("Times New Roman", 13, "bold"))
        self.resultado.pack(pady=5)

    def calcular(self):
        try:
            puntos = [[float(e.get()) for e in row] for row in self.entries]

            metodo_func = geometria.det_gauss if self.metodo_var.get() == "Eliminación Gauss" else geometria.det_laplace

            vol_val = geometria.volumen_tetraedro(puntos, metodo_func)

            if abs(vol_val) < 1e-9:
                self.resultado.config(text="Volumen = 0 (Puntos Coplanares)")
            else:
                self.resultado.config(text=f"Volumen = {vol_val:.6g} u³")

        except ValueError:
            messagebox.showerror("Error", "Asegúrate de llenar todos los campos con números válidos.")

    def limpiar_campos(self):
        for row in self.entries:
            for e in row: e.delete(0, tk.END)
        self.resultado.config(text="")