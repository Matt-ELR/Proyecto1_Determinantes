import tkinter as tk
from tkinter import ttk
import geometria  # Importamos tu lógica de la raíz

class ColinealidadFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Título académico
        titulo = ttk.Label(
            self, 
            text="Prueba de Colinealidad", 
            font=("Times New Roman", 16, "bold")
        )
        titulo.pack(pady=15)

        descripcion = ttk.Label(
            self, 
            text="Si el det = 0, los puntos están en la misma recta", 
            font=("Times New Roman", 11, "italic")
        )
        descripcion.pack(pady=5)

        # Contenedor del determinante visual
        matrix_frame = ttk.Frame(self)
        matrix_frame.pack(pady=10)

        # Barra izquierda
        ttk.Label(matrix_frame, text="|", font=("Times New Roman", 28)).grid(row=0, column=0, rowspan=3)

        # Campos de entrada (P1, P2, P3)
        self.entries = []
        for i in range(3):
            x_ent = ttk.Entry(matrix_frame, width=6)
            y_ent = ttk.Entry(matrix_frame, width=6)
            x_ent.grid(row=i, column=1, padx=5, pady=3)
            y_ent.grid(row=i, column=2, padx=5, pady=3)
            ttk.Label(matrix_frame, text="1").grid(row=i, column=3, padx=5)
            self.entries.append((x_ent, y_ent))

        # Barra derecha
        ttk.Label(matrix_frame, text="|", font=("Times New Roman", 28)).grid(row=0, column=4, rowspan=3)

        # Botones de acción
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=15)

        ttk.Button(btn_frame, text="Verificar", width=15, command=self.verificar).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Volver", width=10, 
                   command=lambda: controller.show_frame("MenuFrame")).grid(row=0, column=1)

        # Resultado dinámico
        self.resultado = ttk.Label(self, text="", font=("Times New Roman", 12, "bold"))
        self.resultado.pack(pady=10)

    def verificar(self):
        try:
            # Recolección de datos
            p1 = (float(self.entries[0][0].get()), float(self.entries[0][1].get()))
            p2 = (float(self.entries[1][0].get()), float(self.entries[1][1].get()))
            p3 = (float(self.entries[2][0].get()), float(self.entries[2][1].get()))

            # Llamada a tu lógica de colinealidad
            es_colineal = geometria.colinealidad(p1, p2, p3)

            if es_colineal:
                self.resultado.config(text="¡Son Colineales! (Det ≈ 0)", foreground="green")
            else:
                self.resultado.config(text="No son Colineales (Det ≠ 0)", foreground="red")

        except ValueError:
            self.resultado.config(text="Error: Datos no válidos", foreground="orange")