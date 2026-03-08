import tkinter as tk
from tkinter import ttk
import geometria # Importación desde la raíz del proyecto

class RectaFrame(ttk.Frame): # Heredamos de ttk para mantener el estilo
    def __init__(self, parent, controller):
        super().__init__(parent)

        titulo = ttk.Label(
            self, 
            text="Ecuación de la Recta (2D)", 
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=15)

        descripcion = ttk.Label(
            self, 
            text="Introduce dos puntos para generar la ecuación", 
            font=("Arial", 11)
        )
        descripcion.pack(pady=5)

        # Marco visual del determinante (3x3 simbólico)
        matrix_frame = ttk.Frame(self)
        matrix_frame.pack(pady=10)

        # Barra izquierda del determinante
        ttk.Label(matrix_frame, text="|", font=("Arial", 30)).grid(row=0, column=0, rowspan=3)

        # FILA 1: Representación simbólica (x, y, 1)
        ttk.Label(matrix_frame, text="x", font=("Arial", 12, "italic")).grid(row=0, column=1, padx=10)
        ttk.Label(matrix_frame, text="y", font=("Arial", 12, "italic")).grid(row=0, column=2, padx=10)
        ttk.Label(matrix_frame, text="1", font=("Arial", 12)).grid(row=0, column=3, padx=10)

        # FILA 2: Punto 1
        self.x1 = ttk.Entry(matrix_frame, width=6)
        self.y1 = ttk.Entry(matrix_frame, width=6)
        self.x1.grid(row=1, column=1, padx=5, pady=5)
        self.y1.grid(row=1, column=2, padx=5, pady=5)
        ttk.Label(matrix_frame, text="1").grid(row=1, column=3)

        # FILA 3: Punto 2
        self.x2 = ttk.Entry(matrix_frame, width=6)
        self.y2 = ttk.Entry(matrix_frame, width=6)
        self.x2.grid(row=2, column=1, padx=5, pady=5)
        self.y2.grid(row=2, column=2, padx=5, pady=5)
        ttk.Label(matrix_frame, text="1").grid(row=2, column=3)

        # Barra derecha del determinante
        ttk.Label(matrix_frame, text="|", font=("Arial", 30)).grid(row=0, column=4, rowspan=3)

        # Botones
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame, text="Calcular Recta", width=15, command=self.calcular
        ).grid(row=0, column=0, padx=10)

        ttk.Button(
            button_frame, text="Volver", width=10, 
            command=lambda: controller.show_frame("MenuFrame")
        ).grid(row=0, column=1)

        # Resultado
        self.resultado = ttk.Label(self, text="", font=("Arial", 12, "bold"), foreground="#0056b3")
        self.resultado.pack(pady=10)

    def calcular(self):
        try:
            p1 = (float(self.x1.get()), float(self.y1.get()))
            p2 = (float(self.x2.get()), float(self.y2.get()))

            if p1 == p2:
                self.resultado.config(text="Error: Los puntos deben ser diferentes", foreground="red")
                return

            # Tu función ecuacion_recta ya devuelve el f-string formateado
            resultado_texto = geometria.ecuacion_recta(p1, p2)
            self.resultado.config(text=f"Ecuación: {resultado_texto}", foreground="#0056b3")

        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos", foreground="red")