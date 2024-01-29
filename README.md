# Random NPC Generator

## Overview
A simple Python program that generates a random TTRPG NPC, with attributes pulled at random from preset attribute entries. Every attribute can be re-rolled.

## Credits
All information currently used is 99.9% from ***The Game Master's Book of Random Encounters*** by **Jeff Ashworth**

## Dependencies

- `python 3.6+` - Not sure if anything below 3.6 works, I just know that above does.
- `tkinter`
  - On MacOS: `pip3 install tk`
  - On Windows: `pip install tk`

## Attributes
The current attributes generated in this program are:
- Name (First + Last generated individually before combined)
- Race
- Pronoun
- Build
- Age
- Hairstyle
- Details
- Wants/Needs
- Secret
- Inventory (based on D&D 5e, but you can use your imagination to replace with your TTRPG of choice)

## Code Architecture
- MVC architecture
    - model.py handles the data
    - view.py handles the display
    - controller handles the communications between all parts

## TODO Features
- GUI menubar has saving/loading options to be bound later

# What I Learned

- Classes and class functions
- MVC Architecture
- JSON basics with Python
- GUI with Tkinter:
    - Main display and geometry management
    - Creating menus with save function
    - Interactive buttons
- Drawing with Aseprite for the dice Icon
