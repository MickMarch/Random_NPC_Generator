from npc_data_classes import NpcData, NpcAttribute
from tkinter import filedialog
import json
import os

SAVE_FOLDER_NAME = "Saved NPCs"


class Model:
    def __init__(self):
        self.npc = NpcData()
        self.save_folder_path = os.path.join(os.path.curdir, SAVE_FOLDER_NAME)
        self._ensure_directory_exists(self.save_folder_path)

    def _directory_exists(self, directory: str) -> bool:
        return os.path.exists(directory)

    def _ensure_directory_exists(self, directory: str) -> None:
        if not self._directory_exists(directory):
            os.makedirs(directory)

    def get_attribute(self, attribute: NpcAttribute) -> str:
        return attribute.current_attribute

    def set_new_attribute(self, attribute: NpcAttribute, new_attribute_text: str):
        attribute.current_attribute = new_attribute_text

    def set_rand_new_attribute(self, attribute: NpcAttribute) -> None:
        attribute.randomize_attribute()

    def set_all_rand_new_attributes(self) -> None:
        for attribute in self.npc.all_attributes_dict.values():
            attribute.randomize_attribute()

    def get_all_attributes(self) -> dict[str, str]:
        return {
            attribute_name: attribute.current_attribute
            for attribute_name, attribute in self.npc.all_attributes_dict.items()
        }

    def _all_attributes_to_json(self):
        return json.dumps(self.get_all_attributes(), indent=4)

    def _export_json(self, file_name: str):
        file_path = os.path.join(self.save_folder_path, file_name + ".json")
        if not self._directory_exists(file_path):
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(self.get_all_attributes(), file, indent=4)
        else:
            self._export_json(file_name + "_new")

    def save_npc_to_json(self):
        npc_name = self.get_attribute(self.npc.all_attributes_dict["Full Name"])
        self._export_json(npc_name)
        print("Saved NPC")

    def save_as_npc_to_json(self):
        npc_name = self.get_attribute(self.npc.all_attributes_dict["Full Name"])
        file_path = filedialog.asksaveasfilename(
            initialdir=self.save_folder_path,
            initialfile=npc_name + ".json",
            title="Save As...",
        )
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(self.get_all_attributes(), file, indent=4)
        print("Saved As NPC")

    def load_npc_from_json(self):
        print("Loaded NPC")
