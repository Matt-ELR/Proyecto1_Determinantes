import tkinter as tk
from tkinter import ttk
import geometria # Importación desde la raíz

class PlanoFrame(ttk.Frame): # Usamos ttk.Frame para el estilo global
    def __init__(self, parent, controller):
        super().__init__(parent)

        titulo = ttk.Label(
            self, 
            text="Ecuación del Plano (3D)", 
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=15)

        descripcion = ttk.Label(
            self, 
            text="Introduce 3 puntos para obtener Ax + By + Cz + D = 0", 
            font=("Arial", 11)
        )
        descripcion.pack(pady=5)

        # Marco del determinante visual
        matrix_frame = ttk.Frame(self)
        matrix_frame.pack(pady=10)

        # Barra izquierda
        ttk.Label(matrix_frame, text="|", font=("Arial", 35)).grid(row=0, column=0, rowspan=4)

        # FILA 1: Variables simbólicas (x, y, z, 1)
        ttk.Label(matrix_frame, text="x", font=("Arial", 12, "italic")).grid(row=0, column=1, padx=10)
        ttk.Label(matrix_frame, text="y", font=("Arial", 12, "italic")).grid(row=0, column=2, padx=10)
        ttk.Label(matrix_frame, text="z", font=("Arial", 12, "italic")).grid(row=0, column=3, padx=10)
        ttk.Label(matrix_frame, text="1", font=("Arial", 12)).grid(row=0, column=4, padx=10)

        # Creación de filas para puntos P1, P2 y P3
        self.points_entries = []
        for i in range(3):
            row_entries = []
            for j in range(3):
                e = ttk.Entry(matrix_frame, width=6)
                e.grid(row=i+1, column=j+1, padx=4, pady=3)
                row_entries.append(e)
            
            ttk.Label(matrix_frame, text="1").grid(row=i+1, column=4, padx=5)
            self.points_entries.append(row_entries)

        # Barra derecha
        ttk.Label(matrix_frame, text="|", font=("Arial", 35)).grid(row=0, column=5, rowspan=4)

        # Botones
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame, text="Generar Plano", width=15, command=self.calcular
        ).grid(row=0, column=0, padx=10)

        ttk.Button(
            button_frame, text="Volver", width=10, 
            command=lambda: controller.show_frame("MenuFrame")
        ).grid(row=0, column=1)

        self.resultado = ttk.Label(self, text="", font=("Arial", 12, "bold"), foreground="#0056b3")
        self.resultado.pack(pady=10)

    def calcular(self):
        try:
            puntos = []
            for row in self.points_entries:
                puntos.append(tuple(float(e.get()) for e in row))

            # Tu función ya devuelve la cadena formateada "Ax + By + Cz + D = 0"
            resultado_texto = geometria.ecuacion_plano(puntos[0], puntos[1], puntos[2])
            
            self.resultado.config(text=f"Ecuación: {resultado_texto}", foreground="#0056b3")

        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos", foreground="red")
        except Exception as e:
            self.resultado.config(text=f"Error: {str(e)}", foreground="red")