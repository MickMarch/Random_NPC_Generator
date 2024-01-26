import random
import json


class NpcAttribute:
    def __init__(self):
        self.attribute_list: list[str] = ...
        self.current_attribute: str = ...

    def randomize_attribute(self) -> None:
        pass


class NpcSingleAttribute(NpcAttribute):
    def __init__(self, attribute_list: list[str]) -> None:
        self.attribute_list = attribute_list
        self.randomize_attribute()

    def randomize_attribute(self) -> None:
        self.current_attribute = random.choice(self.attribute_list)


class NpcCombinedAttribute(NpcAttribute):
    def __init__(
        self,
        attribute_list_1: list[str],
        attribute_list_2: list[str],
    ) -> None:
        self.attribute_list_1 = attribute_list_1
        self.attribute_list_2 = attribute_list_2
        self.randomize_attribute()

    def randomize_attribute(self) -> None:
        self.current_attribute = (
            random.choice(self.attribute_list_1)
            + " "
            + random.choice(self.attribute_list_2)
        )


class NpcData:
    def __init__(self) -> None:
        with open("data/npc_data.json", "r") as file:
            self.npc_json_dict = json.load(file)

        self.all_attributes_dict = {
            "Full Name": NpcCombinedAttribute(
                self.npc_json_dict["first_names"], self.npc_json_dict["last_names"]
            ),
            "Race": NpcSingleAttribute(self.npc_json_dict["races"]),
            "Pronoun": NpcSingleAttribute(self.npc_json_dict["pronouns"]),
            "Build": NpcSingleAttribute(self.npc_json_dict["builds"]),
            "Age": NpcSingleAttribute(self.npc_json_dict["ages"]),
            "Hairstyle": NpcSingleAttribute(self.npc_json_dict["hairstyles"]),
            "Details": NpcSingleAttribute(self.npc_json_dict["details"]),
            "Wants/Needs": NpcSingleAttribute(self.npc_json_dict["wants_needs"]),
            "Secret": NpcSingleAttribute(self.npc_json_dict["secrets"]),
            "Inventory": NpcSingleAttribute(self.npc_json_dict["inventory"]),
        }
