from npc_data_classes import NpcData, NpcAttribute
import json
import os


class Model:
    def __init__(self):
        self.npc = NpcData()
        self.save_file_path = os.path.join(os.path.curdir, "Saved NPCs")
        self._ensure_directory_exists(self.save_file_path)

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

    def save_npc_to_json(self):
        ...
