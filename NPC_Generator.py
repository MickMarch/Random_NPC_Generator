import random
import pickle
from tkinter import filedialog, ttk
from tkinter import *
from data import *
from datetime import datetime
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
        self.wantsNeeds = random.choice(wantsNeedsList)
        self.secretsObstacles = random.choice(secretsObstaclesList)
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
            return self.wantsNeeds

        elif stat == "SECRETS":
            return self.secretsObstacles

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
            self.wantsNeeds = random.choice(wantsNeedsList)

        elif stat == "SECRETS":
            self.secretsObstacles = random.choice(secretsObstaclesList)

        elif stat == "CARRYING":
            self.carrying = random.choice(carryingList)

        elif stat == "ALL":
            self.firstName = random.choice(firstNameList)
            self.lastName = random.choice(lastNameList)
            self.fullName = self.firstName + " " + self.lastName
            self.age = random.choice(ageList)
            self.hair = random.choice(hairList)
            self.build = random.choice(buildList)
            self.pronoun = random.choice(pronounList)
            self.description = random.choice(descriptionList)
            self.wantsNeeds = random.choice(wantsNeedsList)
            self.secretsObstacles = random.choice(secretsObstaclesList)
            self.carrying = random.choice(carryingList)

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
        self.printStat(self.wantsNeeds, "Wants / Needs")
        self.printStat(self.secretsObstacles, "Secret / Obstacle")
        self.printStat(self.carrying, "Items Carried")


def createFrames(root, w, h, rel: str = None):
    return ttk.Frame(root, width=w, height=h, relief=rel)


def createEntry(NPC: RandomNPC, frame, e_width, stat):
    entry = ttk.Entry(frame, width=e_width)
    entry.insert(0, NPC.callStat(stat))
    entry.state(["readonly"])
    return entry


def rerollButton(parent, icon, pressFunction, text=" Re-Roll"):
    return ttk.Button(
        parent, text=text, image=icon, compound=LEFT, command=pressFunction
    )


def createLabel(parent, stat):
    if stat == "FULLNAME":
        return ttk.Label(parent, text="Name: ")

    elif stat == "AGE":
        return ttk.Label(parent, text="Age: ")

    elif stat == "HAIR":
        return ttk.Label(parent, text="Hair: ")

    elif stat == "BUILD":
        return ttk.Label(parent, text="Build: ")

    elif stat == "PRONOUN":
        return ttk.Label(parent, text="Pronoun: ")

    elif stat == "DESCRIPTION":
        return ttk.Label(parent, text="Description: ")

    elif stat == "WANTSNEEDS":
        return ttk.Label(parent, text="Wants/Needs: ")

    elif stat == "SECRETS":
        return ttk.Label(parent, text="Secrets/Obstacles: ")

    elif stat == "CARRYING":
        return ttk.Label(parent, text="Carrying: ")


def rerollStat(NPC: RandomNPC, stat: str, entry: ttk.Entry):
    NPC.rerollStats(stat)
    entry.state(["!readonly"])
    entry.delete(0, END)
    entry.insert(0, NPC.callStat(stat))
    entry.state(["!readonly"])


def rerollAll(NPC: RandomNPC, entryDict: dict):
    for stat in entryDict:
        NPC.rerollStats(stat)
        entryDict[stat].state(["!readonly"])
        entryDict[stat].delete(0, END)
        entryDict[stat].insert(0, NPC.callStat(stat))
        entryDict[stat].state(["!readonly"])


def buildFrameGroup(
    r,
    labelFrame,
    diceFrame,
    infoFrame,
    NPC: RandomNPC,
    stat: str,
    e_width,
):
    entry = createEntry(NPC, infoFrame, e_width, stat)
    dice = rerollButton(diceFrame, diceIcon, lambda: rerollStat(NPC, stat, entry))
    label = createLabel(labelFrame, stat)
    dice.pack(fill="both", expand=True)
    label.pack(fill="both", expand=True)
    return entry


# small save to .txt
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

Wants/Needs: {NPC.wantsNeeds}

Secrets/Obstacle: {NPC.secretsObstacles}

Carrying: {NPC.carrying}"""

    date = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    title_name = f"{NPC.firstName}-{NPC.lastName}_{date}.txt"

    with open(os.path.join(savePath, title_name), "w") as f:
        f.write(character_info)


def pickleNPC(NPC: RandomNPC):
    savePath = os.path.join((os.path.dirname(__file__)), "Saved_Files")
    isExist = os.path.exists(savePath)
    if not isExist:
        os.makedirs(savePath)

    file_name = f"{NPC.fullName}.npc"
    with open(os.path.join(savePath, file_name), "wb") as file:
        pickle.dump(NPC, file)


def loadNPC(NPC: RandomNPC, entryDict: dict):
    file_name = filedialog.askopenfile().name
    with open(file_name, "rb") as file:
        loaded_NPC = pickle.load(file)

    NPC = loaded_NPC
    for stat in entryDict:
        entryDict[stat].state(["!readonly"])
        entryDict[stat].delete(0, END)
        entryDict[stat].insert(0, NPC.callStat(stat))
        entryDict[stat].state(["!readonly"])


"""
main body
"""

NPC = RandomNPC()


# main display
root = Tk()
root.geometry(WINDOW_SIZE)
root.resizable(False, False)
root.title("NPC Generator")

topFrame = createFrames(root, WINDOW_WIDTH, WINDOW_HEIGHT // 10)
topFrame.pack()
panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL)
panedwindow.pack(fill=BOTH, expand=True)
diceFrame = ttk.Frame(panedwindow, width=100, height=800)
labelFrame = ttk.Frame(panedwindow, width=50, height=400)
infoFrame = ttk.Frame(panedwindow, width=400, height=400)
panedwindow.add(diceFrame)
panedwindow.add(labelFrame)
panedwindow.add(infoFrame, weight=4)

# menu
root.option_add("*tearOff", False)
menubar = Menu(root)
root.config(menu=menubar)
file = Menu(menubar)
menubar.add_cascade(menu=file, label="File")
file.add_command(label="Save", command=lambda: pickleNPC(NPC))
file.add_command(label="Load...", command=lambda: loadNPC(NPC, entryDict))
file.add_command(label="Export as .txt file", command=lambda: exportNPCToText(NPC))

# assets
diceIcon = PhotoImage(file="assets/dice.gif")

"""
Build the display
"""

# FULLNAME
fullNameEntry = buildFrameGroup(
    0, labelFrame, diceFrame, infoFrame, NPC, "FULLNAME", 15
)
fullNameEntry.pack(fill="both", expand=True)

# AGE
ageEntry = buildFrameGroup(1, labelFrame, diceFrame, infoFrame, NPC, "AGE", 15)
ageEntry.pack(fill="both", expand=True)

# PRONOUN
pronounEntry = buildFrameGroup(2, labelFrame, diceFrame, infoFrame, NPC, "PRONOUN", 15)
pronounEntry.pack(fill="both", expand=True)

# HAIR
hairEntry = buildFrameGroup(3, labelFrame, diceFrame, infoFrame, NPC, "HAIR", 15)
hairEntry.pack(fill="both", expand=True)

# BUILD
buildEntry = buildFrameGroup(4, labelFrame, diceFrame, infoFrame, NPC, "BUILD", 15)
buildEntry.pack(fill="both", expand=True)

# DESCRIPTION
descriptionEntry = buildFrameGroup(
    5, labelFrame, diceFrame, infoFrame, NPC, "DESCRIPTION", 15
)
descriptionEntry.pack(fill="both", expand=True)

# WANTSNEEDS
wantsNeedsEntry = buildFrameGroup(
    6, labelFrame, diceFrame, infoFrame, NPC, "WANTSNEEDS", 15
)
wantsNeedsEntry.pack(fill="both", expand=True)

# SECRETS
secretsEntry = buildFrameGroup(7, labelFrame, diceFrame, infoFrame, NPC, "SECRETS", 15)
secretsEntry.pack(fill="both", expand=True)

# CARRYING
carryingEntry = buildFrameGroup(
    10, labelFrame, diceFrame, infoFrame, NPC, "CARRYING", 15
)
carryingEntry.pack(fill="both", expand=True)

# REROLL ALL
entryDict = {
    "FULLNAME": fullNameEntry,
    "AGE": ageEntry,
    "PRONOUN": pronounEntry,
    "HAIR": hairEntry,
    "BUILD": buildEntry,
    "DESCRIPTION": descriptionEntry,
    "WANTSNEEDS": wantsNeedsEntry,
    "SECRETS": secretsEntry,
    "CARRYING": carryingEntry,
}
allDice = rerollButton(
    topFrame,
    diceIcon,
    lambda: rerollAll(NPC, entryDict),
    text="Re-Roll Everything",
)
allDice.pack()

root.mainloop()
