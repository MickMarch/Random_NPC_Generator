from .model import Model, NpcAttribute
from .view import NpcGenerator
from ..project_classes.menu_classes import Menu_Labels

from tkinter import Text


class Controller:
    def __init__(self, model: Model, view: NpcGenerator):
        self.model = model
        self.view = view
        # TODO add loop to bind reroll_attribute() to all buttons
        for attribute_name, attribute_row in self.view.all_attribute_rows_dict.items():
            textbox = attribute_row[1]
            button = attribute_row[2]
            callback = lambda textbox=textbox, attribute_name=attribute_name: self.reroll_attribute(
                textbox, self.model.npc.all_attributes_dict[attribute_name]
            )
            self.view.bind_reroll_single_attribute_button(
                button,
                callback,
            )

        self.view.bind_action_to_menu_option(
            self.view.file_menu, Menu_Labels.save, self.save_npc
        )
        self.view.bind_action_to_menu_option(
            self.view.file_menu, Menu_Labels.save_as, self.save_as_npc
        )
        self.view.bind_action_to_menu_option(
            self.view.file_menu, Menu_Labels.load_npc, self.load_npc
        )
        self.view.bind_action_to_menu_option(
            self.view.file_menu, Menu_Labels.exit, self.exit
        )

    def reroll_attribute(self, textbox: Text, npc_attribute: NpcAttribute) -> None:
        npc_attribute.randomize_attribute()
        self.view.update_attribute(textbox, npc_attribute.current_attribute)

    def save_npc(self) -> None:
        self.model.save_npc_to_json()

    def save_as_npc(self) -> None:
        self.model.save_as_npc_to_json()

    def load_npc(self) -> None:
        self.model.load_npc_from_json()

    def exit(self) -> None:
        self.save_npc()
        exit()

    def run(self) -> None:
        self.view.mainloop()
