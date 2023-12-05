from npc_data_classes import NpcData, NpcAttribute


class Model:
    def __init__(self):
        self.npc = NpcData()

    def get_attribute(self, attribute: NpcAttribute) -> str:
        return attribute.current_attribute

    def set_new_attribute(self, attribute: NpcAttribute, new_attribute_text: str):
        attribute.current_attribute = new_attribute_text

    def set_rand_new_attribute(self, attribute: NpcAttribute) -> None:
        attribute.randomize_attribute()

    def set_all_rand_new_attributes(self) -> None:
        for attribute in self.npc.all_attributes:
            attribute.randomize_attribute()

    def get_all_attributes(self) -> dict[str, str]:
        return {
            attribute.attribute_name: attribute.current_attribute
            for attribute in self.npc.all_attributes
        }
