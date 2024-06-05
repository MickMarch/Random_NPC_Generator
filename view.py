import tkinter as tk
from tkinter import Text, ttk, PhotoImage

from typing import List, Union, Callable, Any, Dict

from model import Model, NpcAttribute
from menu_classes import Menu_Labels

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

    def _create_label(
        self, root: ttk.Frame, attribute_name: str, attribute: NpcAttribute
    ) -> ttk.Label:
        return ttk.Label(root, font=LABEL_FONT, text=attribute_name)

    def _create_textbox(self, root: ttk.Frame, attribute: NpcAttribute) -> tk.Text:
        textbox = Text(root, width=TEXTBOX_WIDTH, height=TEXTBOX_HEIGHT)
        textbox.insert(1.0, attribute.current_attribute)
        textbox.config(wrap="word", state="disabled")
        textbox.tag_configure("center text", justify="center", font=("Arial", 13))
        textbox.tag_add("center text", 1.0, "end")
        return textbox

    def _create_button(self, root: ttk.Frame, button_text: str) -> ttk.Button:
        return ttk.Button(
            root,
            text=button_text,
            image=self.BUTTON_IMAGE,
            compound="left",
        )

    def _create_menubar(self) -> None:
        self.menubar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label=Menu_Labels.save)
        self.file_menu.add_command(label=Menu_Labels.save_as)
        self.file_menu.add_command(label=Menu_Labels.load_npc)
        self.file_menu.add_separator()
        self.file_menu.add_command(label=Menu_Labels.exit)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menubar)

    def bind_reroll_single_attribute_button(
        self, button: ttk.Button, callback: Callable[..., Any]
    ) -> None:
        button.configure(command=callback)

    def bind_action_to_menu_option(
        self, menubar: tk.Menu, menu_label: str, callback: Callable[..., Any]
    ) -> None:
        menubar.entryconfig(menu_label, command=callback)

    def _create_attribute_row(
        self, root, attribute_name: str, attribute: NpcAttribute
    ) -> List[Union[ttk.Label, tk.Text, ttk.Button]]:
        return [
            self._create_label(root, attribute_name, attribute),
            self._create_textbox(root, attribute),
            self._create_button(root, " Re-Roll"),
        ]

    def _create_reroll_all_row(self, root) -> List[ttk.Button]:
        return self._create_button(root)

    def _create_attribute_row_dict(
        self, root, all_attributes_dict: dict[str, NpcAttribute]
    ) -> Dict[str, List[Union[ttk.Label, tk.Text, ttk.Button]]]:
        return {
            attribute_name: self._create_attribute_row(root, attribute_name, attribute)
            for attribute_name, attribute in all_attributes_dict.items()
        }

    def update_attribute(self, textbox: tk.Text, new_text: str) -> None:
        textbox.config(state="normal")
        textbox.replace(1.0, "end", new_text)
        textbox.config(state="disabled")
        textbox.tag_add("center text", 1.0, "end")

    def update_npc(self, textbox_updates: list[list[tk.Text, str]]):
        for textbox_update in textbox_updates:
            self.update_attribute(textbox_update[0], textbox_update[1])

    def create_ui(self) -> None:
        self._create_menubar()
        npc_frame = ttk.Frame(self)
        npc_frame.pack()
        self.all_attribute_rows_dict = self._create_attribute_row_dict(
            npc_frame, self.model.npc.all_attributes_dict
        )

        for row_index, row_items in enumerate(self.all_attribute_rows_dict.values()):
            row_items[0].grid(row=row_index, column=0, padx=10, sticky="e")
            row_items[1].grid(row=row_index, column=1)
            row_items[2].grid(row=row_index, column=2, padx=10, sticky="w")
