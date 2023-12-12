from model import Model, NpcAttribute
from view import NpcGenerator

from tkinter import Text


class Controller:
    def __init__(self, model: Model, view: NpcGenerator):
        self.model = model
        self.view = view
        # TODO add loop to bind reroll_attribute() to all buttons
        # for attribute_name, attribute_row in self.view.all_attribute_rows_dict.items():
        #     textbox = attribute_row[1]
        #     button = attribute_row[2]
        #     self.view.bind_reroll_button(
        #         button,
        #         self.reroll_attribute(
        #             textbox, self.model.npc.all_attributes_dict[attribute_name]
        #         ),
        #     )

    def reroll_attribute(self, textbox: Text, npc_attribute: NpcAttribute) -> None:
        self.view.update_attribute(textbox, npc_attribute.randomize_attribute())

    def run(self) -> None:
        self.view.mainloop()
