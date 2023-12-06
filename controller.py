from model import Model, NpcAttribute
from view import NpcGenerator

from tkinter import Text


class Controller:
    def __init__(self, model: Model, view: NpcGenerator):
        self.model = model
        self.view = view
        # TODO add loop to bind reroll_attribute() to all buttons

    def reroll_attribute(self, textbox: Text, npc_attribute: NpcAttribute) -> None:
        self.view.update_attribute(textbox, npc_attribute.randomize_attribute())

    def run(self) -> None:
        self.view.mainloop()
