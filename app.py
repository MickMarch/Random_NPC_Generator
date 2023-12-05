from model import Model
from view import NpcGenerator
from controller import Controller

model = Model()
view = NpcGenerator(model)
controller = Controller(model, view)

controller.run()
