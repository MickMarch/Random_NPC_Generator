from model import Model
from view import NpcGenerator


class Controller:
    def __init__(self, model: Model, view: NpcGenerator):
        self.model = model
        self.view = view

    def run(self):
        self.view.mainloop()
