# 
- MVC architecture
    - model.py will house handle the data
    - view.py will handle the display
    - controller will handle the communications between all parts
    - Add Stability AI to future workflow

Next task: `view.py` - create GUI that can grow dynamically based on information from `model.py`.
- Top row has a single button to be bound to a reroll all function
- 1 row per attribute
    - Label -> Textbox -> Button to be bound to rerolling this line's attribute
- GUI menubar has saving/loading options to be bound later

# Credits up Top
All information currently used is 99.9% from ***The Game Master's Book of Random Encounters*** by **Jeff Ashworth**

# NPC Generator

A python app used to generate a random NPC for TTRPG games. Although it was made with D&D 5e in mind, it is vague enough to be used for other games. 

Data is stored in a python file.
NPC can be saved and loaded from the app (JSON format)

You can reroll each stat individually, or all at once. There is save function.

# Before Running:

You must have Tkinter installed. In your terminal, type:
```
pip3 install tk
```

# What I Learned

- Classes and class functions
- JSON basics with Python, used for saving and loading saved NPCs
- GUI with Tkinter:
    - Main display and geometry management
    - Creating menus with save function
    - Interactive buttons
- Creating python tools to call on
- Drawing with Aseprite for the dice Icon
