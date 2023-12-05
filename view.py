import tkinter as tk

from model import Model

TITLE = "NPC Generator"
WINDOW_HEIGHT = 530
WINDOW_WIDTH = 600
WINDOW_X_SHIFT = 350
WINDOW_Y_SHIFT = 80
DIMENSIONS = (
    str(WINDOW_WIDTH)
    + "x"
    + str(WINDOW_HEIGHT)
    + "+"
    + str(WINDOW_X_SHIFT)
    + "+"
    + str(WINDOW_Y_SHIFT)
)


class NpcGenerator(tk.Tk):
    def __init__(self, model: Model) -> None:
        super().__init__()
        self.model = model
        self.title = TITLE
        self.dimensions = DIMENSIONS
        self.create_ui()
        self.update_npc()

    def create_ui(self) -> None:
        pass

    def update_npc(self) -> None:
        pass
