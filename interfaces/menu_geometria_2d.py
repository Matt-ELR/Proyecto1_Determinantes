# Bibliotecas
import tkinter as tk
from tkinter import ttk

# Frame
class Geometria2DFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        titulo = ttk.Label(
            self,
            text="Aplicaciones en Geometría 2D",
            font=("Times New Roman", 18)
        )
        titulo.pack(pady=20)

        boton_triangulo = ttk.Button(
            self,
            text="Área de Triangulos",
            width=20,
            command=lambda: controller.show_frame("TrianguloFrame")
        )
        boton_triangulo.pack(pady=10)

        boton_recta = ttk.Button(
            self,
            text="Prueba de Colinealidad",
            width=20,
            command=lambda: controller.show_frame("ColinealidadFrame")
        )
        boton_recta.pack(pady=10)

        boton_plano = ttk.Button(
            self,
            text="Ecuación de la Recta",
            width=20,
            command=lambda: controller.show_frame("RectaFrame")
        )
        boton_plano.pack(pady=10)