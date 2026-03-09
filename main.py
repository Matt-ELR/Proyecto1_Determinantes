# Bibliotecas
import tkinter as tk
from tkinter import ttk

# Frames
# Menús
from interfaces.menu import MenuFrame
from interfaces.menu_geometria_2d import Geometria2DFrame
from interfaces.menu_geometria_3d import Geometria3DFrame
# a) Regla de Cramer
from interfaces.regla_de_cramer import ReglaDeCramerFrame
# b) Geometria 2D
from interfaces.triangulo import TrianguloFrame
from interfaces.colinealidad import ColinealidadFrame
from interfaces.recta import RectaFrame
# c) Geometria 3D
from interfaces.tetraedro import TetraedroFrame
from interfaces.coplanaridad import CoplanaridadFrame
from interfaces.plano import PlanoFrame


class CalculadoraGeometrica(tk.Tk):

    def __init__(self):
        super().__init__()

        # Window config
        self.title("Aplicaciones Clásicas de los Determinantes")
        self.geometry("600x600")
        self.eval('tk::PlaceWindow . center')
        self.configure(bg="#E4E4E4")

        style = ttk.Style(self)
        style.theme_use("clam")

        # Light interface colors
        style.configure("TFrame", background="#f2f2f2")

        style.configure(
            "TLabel",
            background="#f2f2f2",
            foreground="#222222",
            font=("Segoe UI", 11)
        )

        style.configure(
            "TButton",
            font=("Segoe UI", 10),
            padding=6
        )

        style.configure(
            "TEntry",
            padding=5
        )

        # Container
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True, padx=20, pady=20)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for FrameClass in (
            MenuFrame,
            ReglaDeCramerFrame,
            Geometria2DFrame,
            TrianguloFrame,
            ColinealidadFrame,
            RectaFrame,
            Geometria3DFrame,
            TetraedroFrame,
            CoplanaridadFrame,
            PlanoFrame
        ):

            frame = FrameClass(container, self)

            self.frames[FrameClass.__name__] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuFrame")


    def show_frame(self, frame_name):

        frame = self.frames[frame_name]
        frame.tkraise()


if __name__ == "__main__":

    app = CalculadoraGeometrica()
    app.mainloop()