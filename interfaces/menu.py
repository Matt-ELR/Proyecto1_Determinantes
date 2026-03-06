import tkinter as tk
from tkinter import ttk


class MenuFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        titulo = ttk.Label(
            self,
            text="Calculadora Geométrica",
            font=("Arial", 18)
        )
        titulo.pack(pady=20)

        boton_triangulo = ttk.Button(
            self,
            text="Triángulo",
            width=20,
            command=lambda: controller.show_frame("TrianguloFrame")
        )
        boton_triangulo.pack(pady=10)

        boton_recta = ttk.Button(
            self,
            text="Recta",
            width=20,
            command=lambda: controller.show_frame("RectaFrame")
        )
        boton_recta.pack(pady=10)

        boton_plano = ttk.Button(
            self,
            text="Plano",
            width=20,
            command=lambda: controller.show_frame("PlanoFrame")
        )
        boton_plano.pack(pady=10)

        boton_tetraedro = ttk.Button(
            self,
            text="Tetraedro",
            width=20,
            command=lambda: controller.show_frame("TetraedroFrame")
        )
        boton_tetraedro.pack(pady=10)

        boton_salir = ttk.Button(
            self,
            text="Salir",
            width=20,
            command=controller.destroy
        )
        boton_salir.pack(pady=20)