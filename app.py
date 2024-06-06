from scripts.mvc.model import Model
from scripts.mvc.view import NpcGenerator
from scripts.mvc.controller import Controller


model = Model()
view = NpcGenerator(model)
controller = Controller(model, view)

controller.run()
