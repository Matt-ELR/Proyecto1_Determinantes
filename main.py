import tkinter as tk
from tkinter import ttk

from interfaces.menu import MenuFrame
from interfaces.triangulo import TrianguloFrame
from interfaces.recta import RectaFrame
from interfaces.tetraedro import TetraedroFrame
from interfaces.plano import PlanoFrame


class CalculadoraGeometrica(tk.Tk):

    def __init__(self):
        super().__init__()

        # Window config
        self.title("Calculadora Geométrica con Determinantes")
        self.geometry("600x450")
        self.configure(bg="#2b2b2b")   # background of the window

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
            TrianguloFrame,
            RectaFrame,
            TetraedroFrame,
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