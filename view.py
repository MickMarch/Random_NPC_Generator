import tkinter as tk

from model import Model


class View(tk.Tk):
    def __init__(self, model: Model):
        super().__init__()
        self.model = model
