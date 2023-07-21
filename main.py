#
# main.py
#
# Written by John Sowell
#
# Written 7/10/2023 - 7/19/2023
#
# main entry point for the flask_generator project
#
from tkinter import *

from jss_cons import *

from generator import generator

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

root = Tk()
win = generator(root, "Flask Website Generator -- John Sowell's Seventh Python GUI")
root.mainloop()