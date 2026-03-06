import tkinter as tk
from tkinter import ttk
from geometria import area_triangulo


class TrianguloFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        titulo = ttk.Label(
            self,
            text="Área de un Triángulo usando Determinantes",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=15)

        descripcion = ttk.Label(
            self,
            text="Introduce los puntos del triángulo",
            font=("Arial", 11)
        )
        descripcion.pack(pady=5)

        # Marco para la matriz de determinantes
        matrix_frame = ttk.Frame(self)
        matrix_frame.pack(pady=10)

        # Barra izquierda del determinante
        ttk.Label(matrix_frame, text="|", font=("Arial", 28)).grid(row=0, column=0, rowspan=3)

        # Fila 1
        self.x1 = ttk.Entry(matrix_frame, width=6)
        self.y1 = ttk.Entry(matrix_frame, width=6)

        self.x1.grid(row=0, column=1, padx=5, pady=3)
        self.y1.grid(row=0, column=2, padx=5, pady=3)

        ttk.Label(matrix_frame, text="1").grid(row=0, column=3)

        # Fila 2
        self.x2 = ttk.Entry(matrix_frame, width=6)
        self.y2 = ttk.Entry(matrix_frame, width=6)

        self.x2.grid(row=1, column=1, padx=5, pady=3)
        self.y2.grid(row=1, column=2, padx=5, pady=3)

        ttk.Label(matrix_frame, text="1").grid(row=1, column=3)

        # Fila 3
        self.x3 = ttk.Entry(matrix_frame, width=6)
        self.y3 = ttk.Entry(matrix_frame, width=6)

        self.x3.grid(row=2, column=1, padx=5, pady=3)
        self.y3.grid(row=2, column=2, padx=5, pady=3)

        ttk.Label(matrix_frame, text="1").grid(row=2, column=3)

        # Barra derecha del determinante
        ttk.Label(matrix_frame, text="|", font=("Arial", 28)).grid(row=0, column=4, rowspan=3)

        # Botones
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame,
            text="Calcular Área",
            width=15,
            command=self.calcular
        ).grid(row=0, column=0, padx=10)

        ttk.Button(
            button_frame,
            text="Volver",
            width=10,
            command=lambda: controller.show_frame("MenuFrame")
        ).grid(row=0, column=1)

        # Resultado
        self.resultado = ttk.Label(
            self,
            text="",
            font=("Arial", 12, "bold")
        )
        self.resultado.pack(pady=10)

    def calcular(self):
        try:

            p1 = (float(self.x1.get()), float(self.y1.get()))
            p2 = (float(self.x2.get()), float(self.y2.get()))
            p3 = (float(self.x3.get()), float(self.y3.get()))

            area = area_triangulo(p1, p2, p3)

            self.resultado.config(text=f"Área = {area:.4f}")

        except:
            self.resultado.config(text="Error: verifica los valores")