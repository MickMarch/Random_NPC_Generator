import random
from tkinter import filedialog, messagebox, ttk
from tkinter import *
from NPC_data import *
from datetime import datetime
import json
import os

os.chdir(os.path.dirname(__file__))


TERMINAL_SPACING = 30
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
WINDOW_X_SHIFT = 350
WINDOW_Y_SHIFT = 80
WINDOW_SIZE = (
    str(WINDOW_WIDTH)
    + "x"
    + str(WINDOW_HEIGHT)
    + "+"
    + str(WINDOW_X_SHIFT)
    + "+"
    + str(WINDOW_Y_SHIFT)
)


class RandomNPC:
    def __init__(self):
        self.firstName = random.choice(firstNameList)
        self.lastName = random.choice(lastNameList)
        self.fullName = self.firstName + " " + self.lastName
        self.age = random.choice(ageList)
        self.hair = random.choice(hairList)
        self.build = random.choice(buildList)
        self.pronoun = random.choice(pronounList)
        self.description = random.choice(descriptionList)
        self.wants_needs = random.choice(wantsNeedsList)
        self.secrets_obstacles = random.choice(secretsObstaclesList)
        self.carrying = random.choice(carryingList)

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def callStat(self, stat: str):
        if stat == "FULLNAME":
            return self.fullName

        elif stat == "AGE":
            return self.age

        elif stat == "HAIR":
            return self.hair

        elif stat == "BUILD":
            return self.build

        elif stat == "PRONOUN":
            return self.pronoun

        elif stat == "DESCRIPTION":
            return self.description

        elif stat == "WANTSNEEDS":
            return self.wants_needs

        elif stat == "SECRETS":
            return self.secrets_obstacles

        elif stat == "CARRYING":
            return self.carrying

    def rerollStats(self, stat: str):
        if stat == "FULLNAME":
            self.firstName = random.choice(firstNameList)
            self.lastName = random.choice(lastNameList)
            self.fullName = self.firstName + " " + self.lastName

        elif stat == "AGE":
            self.age = random.choice(ageList)

        elif stat == "HAIR":
            self.hair = random.choice(hairList)

        elif stat == "BUILD":
            self.build = random.choice(buildList)

        elif stat == "PRONOUN":
            self.pronoun = random.choice(pronounList)

        elif stat == "DESCRIPTION":
            self.description = random.choice(descriptionList)

        elif stat == "WANTSNEEDS":
            self.wants_needs = random.choice(wantsNeedsList)

        elif stat == "SECRETS":
            self.secrets_obstacles = random.choice(secretsObstaclesList)

        elif stat == "CARRYING":
            self.carrying = random.choice(carryingList)

    def createDict(self):
        return {
            "FULLNAME": self.fullName,
            "AGE": self.age,
            "HAIR": self.hair,
            "BUILD": self.build,
            "PRONOUN": self.pronoun,
            "DESCRIPTION": self.description,
            "WANTSNEEDS": self.wants_needs,
            "SECRETS": self.secrets_obstacles,
            "CARRYING": self.carrying,
        }

    # Terminal printing

    def printStat(self, stat1, stat_title: str, stat2=""):
        print("----" + stat_title.center(TERMINAL_SPACING) + "----")
        print(stat1)
        if stat2 != "":
            print(stat2)
        print()

    def printNPC(self):
        self.clear()
        print()
        print("----" + "---NPC INFORMATION---".center(TERMINAL_SPACING) + "----")
        print()
        self.printStat(self.fullName, "Name")
        self.printStat(self.pronoun, "Gender")
        self.printStat(self.age, "Age")
        self.printStat(self.hair, "Hair")
        self.printStat(self.build, "Build")
        self.printStat(self.description, "Little Description")
        self.printStat(self.wants_needs, "Wants / Needs")
        self.printStat(self.secrets_obstacles, "Secret / Obstacle")
        self.printStat(self.carrying, "Items Carried")


class NPCGeneratorWindow:
    def __init__(self, master: Tk):
        def createTextbox(root, NPC: RandomNPC, stat, width, height):
            textbox = Text(root, width=width, height=height)
            textbox.insert(1.0, NPC.callStat(stat))
            textbox.config(wrap="word", state="disabled")
            return textbox

        def createLabel(root, stat: str):
            if stat == "FULLNAME":
                return ttk.Label(root, text="Name: ")

            elif stat == "AGE":
                return ttk.Label(root, text="Age: ")

            elif stat == "HAIR":
                return ttk.Label(root, text="Hair: ")

            elif stat == "BUILD":
                return ttk.Label(root, text="Build: ")

            elif stat == "PRONOUN":
                return ttk.Label(root, text="Pronoun: ")

            elif stat == "DESCRIPTION":
                return ttk.Label(root, text="Description: ")

            elif stat == "WANTSNEEDS":
                return ttk.Label(root, text="Wants/Needs: ")

            elif stat == "SECRETS":
                return ttk.Label(root, text="Secrets/Obstacles: ")

            elif stat == "CARRYING":
                return ttk.Label(root, text="Carrying: ")

        def rerollStat(NPC: RandomNPC, stat: str, textbox: Text):
            NPC.rerollStats(stat)
            textbox.config(state="normal")
            textbox.replace(1.0, "end", NPC.callStat(stat))
            textbox.config(state="disabled")

        def rerollAll(NPC: RandomNPC, textbox_dict: dict):
            for stat in textbox_dict:
                rerollStat(NPC, stat, textbox_dict[stat])

        def createItemLine(root, NPC, stat: str, row_index):
            textbox = createTextbox(root, self.NPC, stat, 30, 3)
            button = ttk.Button(
                root,
                text=" Re-Roll",
                image=self.diceIcon,
                compound=LEFT,
                command=lambda: rerollStat(NPC, stat, textbox),
            )
            label = createLabel(root, stat)
            button.grid(row=row_index, column=0)
            label.grid(row=row_index, column=1)
            textbox.grid(row=row_index, column=2)
            return textbox

        def saveNPC():
            save_path = os.path.join((os.path.dirname(__file__)), "Saved_Files")
            isExist = os.path.exists(save_path)
            if not isExist:
                os.makedirs(save_path)

            file_name = f"{self.NPC.fullName}.json"
            with open(os.path.join(save_path, file_name), "w") as file:
                json.dump(self.NPC.createDict(), file)
            messagebox.showinfo(
                title="NPC Generator Save",
                message=f'"{self.NPC.fullName}" successfully saved!',
            )

        def loadNPC(textbox_dict):
            file_name = filedialog.askopenfile().name
            with open(file_name, "r") as file:
                loaded_NPC: dict = json.load(file)

            for k, v in loaded_NPC.items():
                textbox_dict[k].config(state="normal")
                textbox_dict[k].replace(1.0, "end", loaded_NPC[k])
                textbox_dict[k].config(state="disabled")

        def exportNPCToText(NPC: RandomNPC):
            savePath = os.path.join((os.path.dirname(__file__)), "Saved_Files")
            isExist = os.path.exists(savePath)
            if not isExist:
                os.makedirs(savePath)

            savePath = os.path.join(savePath, "NPC Exported Text")
            isExist = os.path.exists(savePath)
            if not isExist:
                os.makedirs(savePath)

            character_info = f"""Character Name: {NPC.fullName}
Age: {NPC.age}
Hair: {NPC.hair}
Build: {NPC.build}
Gender: {NPC.pronoun}

Description: {NPC.description}

Wants/Needs: {NPC.wants_needs}

Secrets/Obstacle: {NPC.secrets_obstacles}

Carrying: {NPC.carrying}"""

            date = datetime.now().strftime("%Y-%m-%d-%H%M%S")
            title_name = f"{NPC.firstName}-{NPC.lastName}_{date}.txt"

            with open(os.path.join(savePath, title_name), "w") as f:
                f.write(character_info)

        self.NPC = RandomNPC()
        self.NPC_frame = ttk.Frame(master)
        self.NPC_frame.pack()
        self.diceIcon = PhotoImage(file="assets/dice.gif")

        # Window dimensions and creation
        master.title("NPC Generator")
        master.geometry(WINDOW_SIZE)
        master.resizable(False, False)

        """
        Fill with content
        """
        self.full_name_text = createItemLine(self.NPC_frame, self.NPC, "FULLNAME", 1)
        self.age_text = createItemLine(self.NPC_frame, self.NPC, "AGE", 2)
        self.pronoun_text = createItemLine(self.NPC_frame, self.NPC, "PRONOUN", 3)
        self.hair_text = createItemLine(self.NPC_frame, self.NPC, "HAIR", 4)
        self.build_text = createItemLine(self.NPC_frame, self.NPC, "BUILD", 5)
        self.description_text = createItemLine(
            self.NPC_frame, self.NPC, "DESCRIPTION", 6
        )
        self.wants_needs_text = createItemLine(
            self.NPC_frame, self.NPC, "WANTSNEEDS", 7
        )
        self.secrets_text = createItemLine(self.NPC_frame, self.NPC, "SECRETS", 8)
        self.carrying_text = createItemLine(self.NPC_frame, self.NPC, "CARRYING", 9)

        self.textbox_dict = {
            "FULLNAME": self.full_name_text,
            "AGE": self.age_text,
            "PRONOUN": self.pronoun_text,
            "HAIR": self.hair_text,
            "BUILD": self.build_text,
            "DESCRIPTION": self.description_text,
            "WANTSNEEDS": self.wants_needs_text,
            "SECRETS": self.secrets_text,
            "CARRYING": self.carrying_text,
        }
        self.reroll_all_button = ttk.Button(
            self.NPC_frame,
            text="Re-Roll Everything",
            image=self.diceIcon,
            compound=LEFT,
            command=lambda: rerollAll(self.NPC, self.textbox_dict),
        )
        self.reroll_all_button.grid(row=0, column=0, columnspan=3)

        # Menu option creation
        master.option_add("*tearOff", False)
        self.menubar = Menu(master)
        master.config(menu=self.menubar)
        self.file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.file, label="File")
        self.file.add_command(label="Save", command=lambda: saveNPC())
        self.file.add_command(
            label="Load...", command=lambda: loadNPC(self.textbox_dict)
        )
        self.file.add_command(
            label="Export as .txt file", command=lambda: exportNPCToText(self.NPC)
        )


root = Tk()
npc_generator = NPCGeneratorWindow(root)

root.mainloop()
