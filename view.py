import tkinter as tk
from tkinter import Text, ttk, PhotoImage

from typing import List, Union, Callable, Any

from model import Model, NpcAttribute

TITLE = "NPC Generator"
BUTTON_IMAGE_PATH = "assets/dice.gif"
WINDOW_HEIGHT = 580
WINDOW_WIDTH = 600
WINDOW_X_SHIFT = 350
WINDOW_Y_SHIFT = 80
DIMENSIONS = (
    str(WINDOW_WIDTH)
    + "x"
    + str(WINDOW_HEIGHT)
    + "+"
    + str(WINDOW_X_SHIFT)
    + "+"
    + str(WINDOW_Y_SHIFT)
)
TEXTBOX_WIDTH = 30
TEXTBOX_HEIGHT = 3
LABEL_FONT = ("Arial Black", 13)


class NpcGenerator(tk.Tk):
    def __init__(self, model: Model) -> None:
        super().__init__()
        self.BUTTON_IMAGE = PhotoImage(file=BUTTON_IMAGE_PATH)
        self.model = model
        self.title = TITLE
        self.dimensions = DIMENSIONS
        self.create_ui()

    def _create_label(self, root: ttk.Frame, attribute: NpcAttribute) -> ttk.Label:
        return ttk.Label(root, font=LABEL_FONT, text=attribute.attribute_name)

    def _create_textbox(self, root: ttk.Frame, attribute: NpcAttribute) -> tk.Text:
        textbox = Text(root, width=TEXTBOX_WIDTH, height=TEXTBOX_HEIGHT)
        textbox.insert(1.0, attribute.current_attribute)
        textbox.config(wrap="word", state="disabled")
        textbox.tag_configure("center text", justify="center", font=("Arial", 13))
        textbox.tag_add("center text", 1.0, "end")
        return textbox

    def _create_reroll_button(self, root: ttk.Frame) -> ttk.Button:
        return ttk.Button(
            root,
            text=" Re-Roll",
            image=self.BUTTON_IMAGE,
            compound="left",
        )

    def _create_reroll_all_button(self, root: ttk.Frame) -> ttk.Button:
        return ttk.Button(
            root,
            text=" Re-Roll Everything",
            image=self.BUTTON_IMAGE,
            compound="left",
        )

    def bind_reroll_button(
        self, button: ttk.Button, callback: Callable[..., Any]
    ) -> None:
        button.configure(command=callback)

    def _create_attribute_row(
        self, root, attribute: NpcAttribute
    ) -> List[Union[ttk.Label, tk.Text, ttk.Button]]:
        return [
            self._create_label(root, attribute),
            self._create_textbox(root, attribute),
            self._create_reroll_button(root),
        ]

    def _create_reroll_all_row(self, root) -> List[ttk.Button]:
        return self._create_reroll_all_button(root)

    def _create_attribute_row_list(
        self, root, all_attributes: list[NpcAttribute]
    ) -> List[List[Union[ttk.Label, tk.Text, ttk.Button]]]:
        return [
            self._create_attribute_row(root, attribute) for attribute in all_attributes
        ]

    def create_ui(self) -> None:
        npc_frame = ttk.Frame(self)
        npc_frame.pack()

        for row_index, row_items in enumerate(
            self._create_attribute_row_list(npc_frame, self.model.npc.all_attributes)
        ):
            row_items[0].grid(row=row_index, column=0, padx=10, sticky="e")
            row_items[1].grid(row=row_index, column=1)
            row_items[2].grid(row=row_index, column=2, padx=10, sticky="w")

    def update_npc(self) -> None:
        # TODO consider moving all textbox updates here
        pass
