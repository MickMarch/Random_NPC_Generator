import tkinter as tk
from tkinter import Text, ttk, LEFT, PhotoImage

from model import Model, NpcAttribute

TITLE = "NPC Generator"
BUTTON_IMAGE = PhotoImage(file="assets/dice.gif")
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
TEXTBOX_WIDTH = 30
TEXTBOX_HEIGHT = 3
LABEL_FONT = ("Arial Black", 13)


class NpcGenerator(tk.Tk):
    def __init__(self, model: Model) -> None:
        super().__init__()
        self.model = model
        self.title = TITLE
        self.dimensions = DIMENSIONS
        self.create_ui()

    def _create_label(self, root: ttk.Frame, attribute: NpcAttribute) -> ttk.Label:
        return ttk.Label(root, font=LABEL_FONT, text=attribute.attribute_name)

    def _create_textbox(self, root: ttk.Frame, attribute: NpcAttribute) -> tk.Text:
        textbox = Text(root, width=TEXTBOX_WIDTH, height=TEXTBOX_HEIGHT)
        textbox.insert(1.0, attribute.current_attribute)
        textbox.config(wrap="word", state="disabled")
        textbox.tag_configure("center text", justify="center", font=("Arial", 13))
        textbox.tag_add("center text", 1.0, "end")
        return textbox

    def _create_reroll_button(self, root: ttk.Frame) -> ttk.Button:
        return ttk.Button(
            root,
            text=" Re-Roll",
            image=BUTTON_IMAGE,
            compound=LEFT,
        )

    def _create_reroll_all_button(self, root: ttk.Frame) -> ttk.Button:
        return ttk.Button(
            root,
            text=" Re-Roll Everything",
            image=BUTTON_IMAGE,
            compound=LEFT,
        )

    def bind_reroll_button(self, button: ttk.Button, callback: function) -> None:
        button.configure(command=callback)

    def create_ui(self) -> None:
        pass

    def update_npc(self) -> None:
        pass
