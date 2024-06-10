import tkinter as tk
from tkinter import Text, ttk, PhotoImage, messagebox, filedialog

from typing import List, Union, Callable, Any, Dict

from .model import Model, NpcAttribute
from ..project_classes.menu_classes import Menu_Labels

TITLE = "NPC Generator"
BUTTON_IMAGE_PATH = "res/assets/dice.gif"
TEXTBOX_WIDTH = 30
TEXTBOX_HEIGHT = 3
LABEL_FONT = ("Arial Black", 13)


class NpcGenerator(tk.Tk):
    def __init__(self, model: Model) -> None:
        super().__init__()
        self.BUTTON_IMAGE = PhotoImage(file=BUTTON_IMAGE_PATH)
        self.model = model
        self.title = TITLE
        self.create_ui()
        self.center_window()

    def center_window(self):
        self.pack_propagate(True)
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        w_width = self.winfo_width()
        w_height = self.winfo_height()
        print(w_width)
        print(screen_width)
        x = (screen_width // 2) - (w_width // 2)
        y = (screen_height // 2) - (w_height // 2)

        self.geometry(f"+{x}+{y}")

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
            compound="left",
        )

    def _create_button_dice_image(
        self, root: ttk.Frame, button_text: str
    ) -> ttk.Button:
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

    def bind_command_to_button(
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
            self._create_button_dice_image(root, " Re-Roll"),
        ]

    def _create_undo_reroll_all_redo_row(self, root) -> list[ttk.Button]:
        return [
            self._create_button(root, "Undo"),
            self._create_button_dice_image(root, " Re-Roll All"),
            self._create_button(root, "Redo"),
        ]

    def _create_save_load_row(self, root) -> list[ttk.Button]:
        return [
            self._create_button(root, "Save"),
            self._create_button(root, "Save As..."),
            self._create_button(root, "Load..."),
        ]

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

    def create_ui(self) -> None:
        self._create_menubar()
        self.npc_frame = ttk.Frame(self)
        self.npc_frame.pack()
        self.all_attribute_rows_dict = self._create_attribute_row_dict(
            self.npc_frame, self.model.npc.all_attributes_dict
        )

        for row_index, row_items in enumerate(self.all_attribute_rows_dict.values()):
            row_items[0].grid(row=row_index, column=0, padx=10, sticky="e")
            row_items[1].grid(row=row_index, column=1)
            row_items[2].grid(row=row_index, column=2, padx=10, sticky="w")

        self.utility_button_frame = ttk.Frame(self, borderwidth=5, relief=tk.GROOVE)
        self.utility_button_frame.pack()
        self.utility_button_rows = []

        self.undo_reroll_all_redo_row = self._create_undo_reroll_all_redo_row(
            self.utility_button_frame
        )
        self.save_load_row = self._create_save_load_row(self.utility_button_frame)

        self.utility_button_rows.append(self.undo_reroll_all_redo_row)
        self.utility_button_rows.append(self.save_load_row)

        for row_index, button_row in enumerate(self.utility_button_rows):
            button_row[0].grid(row=row_index, column=0, padx=10, pady=5, sticky="w")
            button_row[1].grid(row=row_index, column=1, pady=5)
            button_row[2].grid(row=row_index, column=2, padx=10, pady=5, sticky="e")

    def update_npc(self):
        for attribute_name, attribute_row in self.all_attribute_rows_dict.items():
            self.update_attribute(
                attribute_row[1],
                self.model.get_attribute(
                    self.model.npc.all_attributes_dict[attribute_name]
                ),
            )

    def show_yes_no_dialog(self, title: str, message: str) -> bool:
        answer = messagebox.askyesno(title, message)
        return answer

    def show_ask_save_as_file_dialog(
        self, initialdir: str, initialfile: str, file_ext: str
    ):
        file_path = filedialog.asksaveasfilename(
            initialdir=initialdir,
            initialfile=initialfile + file_ext,
            title="Save As...",
        )
        return file_path

    def show_ask_open_file_dialog(self, initialdir: str):
        file_path = filedialog.askopenfilename(initialdir=initialdir)
        return file_path
