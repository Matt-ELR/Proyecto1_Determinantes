import tkinter as tk
from tkinter import ttk
from geometria import ecuacion_plano


class PlanoFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        titulo = ttk.Label(
            self,
            text="Ecuación de un Plano (3 puntos)",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=15)

        matrix_frame = ttk.Frame(self)
        matrix_frame.pack(pady=10)

        ttk.Label(matrix_frame, text="|", font=("Arial", 26)).grid(row=0, column=0, rowspan=3)

        entries = []
        for i in range(3):

            row_entries = []

            for j in range(3):

                e = ttk.Entry(matrix_frame, width=6)
                e.grid(row=i, column=j+1, padx=4, pady=3)
                row_entries.append(e)

            ttk.Label(matrix_frame, text="1").grid(row=i, column=4)
            entries.append(row_entries)

        ttk.Label(matrix_frame, text="|", font=("Arial", 26)).grid(row=0, column=5, rowspan=3)

        self.x1, self.y1, self.z1 = entries[0]
        self.x2, self.y2, self.z2 = entries[1]
        self.x3, self.y3, self.z3 = entries[2]

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame,
            text="Calcular Plano",
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

            p1 = (float(self.x1.get()), float(self.y1.get()), float(self.z1.get()))
            p2 = (float(self.x2.get()), float(self.y2.get()), float(self.z2.get()))
            p3 = (float(self.x3.get()), float(self.y3.get()), float(self.z3.get()))

            A, B, C, D = ecuacion_plano(p1, p2, p3)

            self.resultado.config(
                text=f"Plano: {A:.2f}x + {B:.2f}y + {C:.2f}z + {D:.2f} = 0"
            )

        except:

            self.resultado.config(text="Error: verifica los valores")