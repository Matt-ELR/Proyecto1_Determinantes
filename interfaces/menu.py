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

        boton_cramer = ttk.Button(
            self,
            text="Regla de Cramer",
            width=20,
            command=lambda: controller.show_frame("ReglaDeCramerFrame")
        )
        boton_cramer.pack(pady=10)

        boton_2d = ttk.Button(
            self,
            text="Geometría 2D",
            width=20,
            command=lambda: controller.show_frame("Geometria2DFrame")
        )
        boton_2d.pack(pady=10)

        boton_3d = ttk.Button(
            self,
            text="Geometría 3D",
            width=20,
            command=lambda: controller.show_frame("Geometria3DFrame")
        )
        boton_3d.pack(pady=10)

        boton_salir = ttk.Button(
            self,
            text="Salir",
            width=20,
            command=controller.destroy
        )
        boton_salir.pack(pady=20)