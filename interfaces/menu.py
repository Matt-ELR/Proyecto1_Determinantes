# Bibliotecas
import tkinter as tk
from tkinter import ttk

# Frame
class MenuFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        titulo = ttk.Label(
            self,
            text="Aplicaciones Clásicas de los Determinantes",
            font=("Times New Roman", 18)
        )
        titulo.pack(pady=20)

        boton_triangulo = ttk.Button(
            self,
            text="Regla de Cramer",
            width=20,
            command=lambda: controller.show_frame("ReglaDeCramerFrame")
        )
        boton_triangulo.pack(pady=10)

        boton_recta = ttk.Button(
            self,
            text="Geometría 2D",
            width=20,
            command=lambda: controller.show_frame("Geometria2DFrame")
        )
        boton_recta.pack(pady=10)

        boton_plano = ttk.Button(
            self,
            text="Geometría 3D",
            width=20,
            command=lambda: controller.show_frame("Geometria3DFrame")
        )
        boton_plano.pack(pady=10)

        boton_salir = ttk.Button(
            self,
            text="Salir",
            width=20,
            command=controller.destroy
        )
        boton_salir.pack(pady=20)