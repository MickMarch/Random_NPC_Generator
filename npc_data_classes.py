import random
import json


class NpcAttribute:
    def __init__(self):
        self.attribute_name: str = ...
        self.attribute_list: list[str] = ...
        self.current_attribute: str = ...

    def get_new_attribute(self) -> None:
        pass


class NpcSingleAttribute(NpcAttribute):
    def __init__(self, attribute_name: str, attribute_list: list[str]) -> None:
        self.attribute_name = attribute_name
        self.attribute_list = attribute_list
        self.get_new_attribute()

    def get_new_attribute(self) -> None:
        self.current_attribute = random.choice(self.attribute_list)


class NpcCombinedAttribute(NpcAttribute):
    def __init__(
        self,
        attribute_name: str,
        attribute_list_1: list[str],
        attribute_list_2: list[str],
    ) -> None:
        self.attribute_name = attribute_name
        self.attribute_list_1 = attribute_list_1
        self.attribute_list_2 = attribute_list_2
        self.get_new_attribute()

    def get_new_attribute(self) -> None:
        self.current_attribute = (
            random.choice(self.attribute_list_1)
            + " "
            + random.choice(self.attribute_list_2)
        )


class NpcData:
    def __init__(self) -> None:
        with open("data/npc_data.json", "r") as file:
            self.npc_data_dict = json.load(file)
        self.names = NpcCombinedAttribute(
            "Full Name",
            self.npc_data_dict["first_names"],
            self.npc_data_dict["last_names"],
        )
        self.races = NpcSingleAttribute("Race", self.npc_data_dict["races"])
        self.pronouns = NpcSingleAttribute("Pronoun", self.npc_data_dict["pronouns"])
        self.ages = NpcSingleAttribute("Age", self.npc_data_dict["ages"])
        self.hairstyles = NpcSingleAttribute(
            "Hairstyle", self.npc_data_dict["hairstyles"]
        )
        self.details = NpcSingleAttribute("Details", self.npc_data_dict["details"])
        self.wants_needs = NpcSingleAttribute(
            "Wants/Needs", self.npc_data_dict["wants_needs"]
        )
        self.secrets = NpcSingleAttribute("Secrets", self.npc_data_dict["secrets"])
        self.inventory = NpcSingleAttribute(
            "Inventory", self.npc_data_dict["inventory"]
        )

        self.all_attributes = [
            self.names,
            self.races,
            self.pronouns,
            self.ages,
            self.hairstyles,
            self.details,
            self.wants_needs,
            self.secrets,
            self.inventory,
        ]
