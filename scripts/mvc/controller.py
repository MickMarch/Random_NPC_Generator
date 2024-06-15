from .model import Model, NpcAttribute
from .view import NpcGenerator
from ..project_classes.menu_classes import Menu_Labels

from tkinter import Text


class Controller:
    def __init__(self, model: Model, view: NpcGenerator):
        self.has_saved = False
        self.model = model
        self.view = view
        self.view.protocol("WM_DELETE_WINDOW", self.exit)
        for attribute_name, attribute_row in self.view.all_attribute_rows_dict.items():
            textbox = attribute_row[1]
            button = attribute_row[2]
            callback = lambda textbox=textbox, attribute_name=attribute_name: self.reroll_attribute(
                textbox, self.model.npc.all_attributes_dict[attribute_name]
            )
            self.view.bind_command_to_button(
                button,
                callback,
            )

        self.view.bind_command_to_button(
            self.view.undo_reroll_all_redo_row[1], self.reroll_all_attributes
        )

        self.view.bind_action_to_menu_option(
            self.view.file_menu, Menu_Labels.save, self.save_npc
        )
        self.view.bind_command_to_button(
            self.view.utility_button_rows[1][0], self.save_npc
        )
        self.view.bind_action_to_menu_option(
            self.view.file_menu, Menu_Labels.save_as, self.save_as_npc
        )
        self.view.bind_command_to_button(
            self.view.utility_button_rows[1][1], self.save_as_npc
        )
        self.view.bind_action_to_menu_option(
            self.view.file_menu, Menu_Labels.load_npc, self.load_npc
        )
        self.view.bind_command_to_button(
            self.view.utility_button_rows[1][2], self.load_npc
        )
        self.view.bind_action_to_menu_option(
            self.view.file_menu, Menu_Labels.exit, self.exit
        )

        self.view.bind_command_to_button(self.view.utility_button_rows[0][0], self.undo)

        self.view.bind_command_to_button(self.view.utility_button_rows[0][2], self.redo)

    def undo(self):
        self.model.previous_history_record()
        self.view.update_npc()

    def redo(self):
        self.model.next_history_record()
        self.view.update_npc()

    def reroll_attribute(self, textbox: Text, npc_attribute: NpcAttribute) -> None:
        npc_attribute.randomize_attribute()
        self.view.update_attribute(textbox, npc_attribute.current_attribute)
        self.has_saved = False
        self.model.create_history_record()

    def reroll_all_attributes(self) -> None:
        self.model.set_all_rand_new_attributes()
        self.view.update_npc()
        self.model.create_history_record()

    def save_npc(self) -> None:
        if not self.has_saved:
            self.model.save_npc_to_json()
            self.has_saved = True
        else:
            print("File is already saved.")

    def save_as_npc(self) -> None:
        file_path = self.view.show_ask_save_as_file_dialog(
            self.model.save_folder_path,
            self.model.get_attribute(self.model.npc.all_attributes_dict["Full Name"]),
            file_ext=".json",
        )
        self.model.save_as_npc_to_json(file_path)

    def load_npc(self) -> None:
        if not self.has_saved and self.view.show_yes_no_dialog(
            "Save Before Loading?",
            "Would you like to save this NPC before loading another?",
        ):
            self.save_npc()

        file_path = self.view.show_ask_open_file_dialog(self.model.save_folder_path)
        self.model.load_npc_from_json(file_path)
        self.view.update_npc()
        self.has_saved = True
        self.model.create_history_record()

    def exit(self) -> None:
        if not self.has_saved and self.view.show_yes_no_dialog(
            "Save Before Exiting?",
            "Would you like to save this NPC before closing the application?",
        ):
            self.save_npc()
        exit()

    def run(self) -> None:
        self.view.update_idletasks()
        self.view.update()
        self.view.mainloop()
