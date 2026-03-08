import tkinter as tk
from tkinter import ttk
import geometria  # Importación desde la raíz

class CoplanaridadFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        titulo = ttk.Label(
            self, 
            text="Prueba de Coplanaridad (3D)", 
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=15)

        descripcion = ttk.Label(
            self, 
            text="Si el det = 0, los 4 puntos están en el mismo plano", 
            font=("Arial", 11, "italic")
        )
        descripcion.pack(pady=5)

        # Marco del determinante 4x4
        matrix_frame = ttk.Frame(self)
        matrix_frame.pack(pady=10)

        # Encabezados
        ttk.Label(matrix_frame, text="X", font=("Arial", 10, "italic")).grid(row=0, column=1)
        ttk.Label(matrix_frame, text="Y", font=("Arial", 10, "italic")).grid(row=0, column=2)
        ttk.Label(matrix_frame, text="Z", font=("Arial", 10, "italic")).grid(row=0, column=3)

        # Barras visuales
        ttk.Label(matrix_frame, text="|", font=("Arial", 35)).grid(row=1, column=0, rowspan=4)
        
        self.points_entries = []

        for i in range(4):
            row_entries = []
            for j in range(3):
                e = ttk.Entry(matrix_frame, width=6)
                e.grid(row=i+1, column=j+1, padx=4, pady=3)
                row_entries.append(e)
            
            ttk.Label(matrix_frame, text="1").grid(row=i+1, column=4, padx=5)
            self.points_entries.append(row_entries)

        ttk.Label(matrix_frame, text="|", font=("Arial", 35)).grid(row=1, column=5, rowspan=4)

        # Botones
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame, text="Verificar Coplanaridad", width=20, command=self.verificar
        ).grid(row=0, column=0, padx=10)

        ttk.Button(
            button_frame, text="Volver", width=10, 
            command=lambda: controller.show_frame("MenuFrame")
        ).grid(row=0, column=1)

        self.resultado = ttk.Label(self, text="", font=("Arial", 12, "bold"))
        self.resultado.pack(pady=10)

    def verificar(self):
        try:
            puntos = []
            for row in self.points_entries:
                coords = tuple(float(e.get()) for e in row)
                puntos.append(coords)

            # Llamada a tu lógica de coplanaridad
            # Esta ya usa la tolerancia 1e-9 que definimos
            es_coplanar = geometria.son_coplanares(puntos[0], puntos[1], puntos[2], puntos[3])

            if es_coplanar:
                self.resultado.config(text="¡Son Coplanares! (V = 0)", foreground="green")
            else:
                self.resultado.config(text="No son Coplanares (V ≠ 0)", foreground="red")

        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos", foreground="orange")