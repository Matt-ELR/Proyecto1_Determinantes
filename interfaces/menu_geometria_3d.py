# Bibliotecas
import tkinter as tk
from tkinter import ttk

# Frame
class Geometria3DFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        titulo = ttk.Label(
            self,
            text="Aplicaciones en Geometría 3D",
            font=("Times New Roman", 18)
        )
        titulo.pack(pady=20)

        boton_triangulo = ttk.Button(
            self,
            text="Volumen de un Tetraedro",
            width=20,
            command=lambda: controller.show_frame("TetraedroFrame")
        )
        boton_triangulo.pack(pady=10)

        boton_recta = ttk.Button(
            self,
            text="Prueba de Coplanaridad",
            width=20,
            command=lambda: controller.show_frame("CoplanaridadFrame")
        )
        boton_recta.pack(pady=10)

        boton_plano = ttk.Button(
            self,
            text="Ecuación de un Plano",
            width=20,
            command=lambda: controller.show_frame("PlanoFrame")
        )
        boton_plano.pack(pady=10)

        boton_menu = ttk.Button(
            self,
            text="Volver",
            width=20,
            command=lambda: controller.show_frame("MenuFrame")
        )
        boton_menu.pack(pady=10)