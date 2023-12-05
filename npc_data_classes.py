import random
import json


class NpcAttribute:
    def __init__(self, name, attribute_list: list[str]):
        self.name = name
        self.attribute_list = attribute_list
        self.get_new_attribute()

    def get_new_attribute(self) -> None:
        self.current_attribute = random.choice(self.attribute_list)


class NpcData:
    def __init__(self, npc_data_dict: dict[str, str]):
        pass
