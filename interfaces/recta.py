import tkinter as tk
from tkinter import ttk
from geometria import ecuacion_recta


class RectaFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        titulo = ttk.Label(
            self,
            text="Ecuación de una Recta (2 puntos)",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=15)

        descripcion = ttk.Label(
            self,
            text="Introduce dos puntos del plano",
            font=("Arial", 11)
        )
        descripcion.pack(pady=5)

        matrix_frame = ttk.Frame(self)
        matrix_frame.pack(pady=10)

        ttk.Label(matrix_frame, text="|", font=("Arial", 26)).grid(row=0, column=0, rowspan=2)

        self.x1 = ttk.Entry(matrix_frame, width=6)
        self.y1 = ttk.Entry(matrix_frame, width=6)

        self.x1.grid(row=0, column=1, padx=5)
        self.y1.grid(row=0, column=2, padx=5)
        ttk.Label(matrix_frame, text="1").grid(row=0, column=3)

        self.x2 = ttk.Entry(matrix_frame, width=6)
        self.y2 = ttk.Entry(matrix_frame, width=6)

        self.x2.grid(row=1, column=1, padx=5)
        self.y2.grid(row=1, column=2, padx=5)
        ttk.Label(matrix_frame, text="1").grid(row=1, column=3)

        ttk.Label(matrix_frame, text="|", font=("Arial", 26)).grid(row=0, column=4, rowspan=2)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame,
            text="Calcular Recta",
            width=15,
            command=self.calcular
        ).grid(row=0, column=0, padx=10)

        ttk.Button(
            button_frame,
            text="Volver",
            width=10,
            command=lambda: controller.show_frame("MenuFrame")
        ).grid(row=0, column=1)

        self.resultado = ttk.Label(self, text="", font=("Arial", 12, "bold"))
        self.resultado.pack(pady=10)

    def calcular(self):

        try:

            p1 = (float(self.x1.get()), float(self.y1.get()))
            p2 = (float(self.x2.get()), float(self.y2.get()))

            A, B, C = ecuacion_recta(p1, p2)

            self.resultado.config(
                text=f"Ecuación: {A:.2f}x + {B:.2f}y + {C:.2f} = 0"
            )

        except:

            self.resultado.config(text="Error: verifica los valores")