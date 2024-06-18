import random
import json


class AttributeKeys:
    name = "Full Name"
    race = "Race"
    pronoun = "Pronoun"
    build = "Build"
    age = "Age"
    hair = "Hairstyle"
    details = "Details"
    wants = "Wants/Needs"
    secret = "Secret"
    inventory = "Inventory"


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
        with open("res/data/npc_data.json", "r") as file:
            self.npc_json_dict = json.load(file)

        self.all_attributes_dict = {
            AttributeKeys.name: NpcCombinedAttribute(
                self.npc_json_dict["first_names"], self.npc_json_dict["last_names"]
            ),
            AttributeKeys.race: NpcSingleAttribute(self.npc_json_dict["races"]),
            AttributeKeys.pronoun: NpcSingleAttribute(self.npc_json_dict["pronouns"]),
            AttributeKeys.build: NpcSingleAttribute(self.npc_json_dict["builds"]),
            AttributeKeys.age: NpcSingleAttribute(self.npc_json_dict["ages"]),
            AttributeKeys.hair: NpcSingleAttribute(self.npc_json_dict["hairstyles"]),
            AttributeKeys.details: NpcSingleAttribute(self.npc_json_dict["details"]),
            AttributeKeys.wants: NpcSingleAttribute(self.npc_json_dict["wants_needs"]),
            AttributeKeys.secret: NpcSingleAttribute(self.npc_json_dict["secrets"]),
            AttributeKeys.inventory: NpcSingleAttribute(
                self.npc_json_dict["inventory"]
            ),
        }
