#
# jss_button.py
#
# Written by John Sowell
#
# Written 5/19/2020 - 6/10/2020 (45 lines total)
#
# Defines the button class to be added to the subclassed window class
#
# 6/21/2020 Added some padding for the grid mode (47 lines total)
#
# 6/22/2020 Added a parameter to the constructor function, allowing the user
#           to specify the character width of the button, and not always have
#           the width equal to the length of the text. (52 lines total)
#
# 6/24/2020 Added span for buttons in grids. Also added mechanism for enabling
#           and disabling the button. (75 lines)
#
# 7/3/2020  Took out constants, put in jss_cons instead. (74 lines)
#
from tkinter import *
from tkinter.font import Font

from jss_cons import *

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class jss_button:

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def __init__(self, parent, sx, sy, w=10, t='', sp=1, p=None, fp=None, b='#cccccc', f='#000000', ff='', fs=0):
        self.enabled = True
        self.function = fp
        if len(t) > w:
            w = len(t)
        if p != None:
            if fp == None:
                self.widget = Button(parent.canvas, image=p)
            else:
                self.widget = Button(parent.canvas, image=p, command=fp)
        else:
            if ff == '':
                ff = parent.font_face
            if fs == 0:
                fs = parent.font_size
            self.font = Font(family=ff, size=fs)
            self.widget = Button(parent.canvas, width=w, text=t, bg=b, fg=f, font=self.font, command=self.clicked)

        if parent.mode == CANVAS_MODE:
            self.widget.pack()
            parent.canvas.create_window(sx, sy, anchor='nw', window=self.widget)
        else:
            self.widget.grid(row=sy, column=sx, padx=3, pady=3, columnspan=sp)

    # *************************************************************************

    def clicked(self):
        if self.enabled == False:
            return
        if self.function != None:
            self.function()

    # *************************************************************************

    def disable(self):
        self.widget.configure(state="disabled")
        self.enabled = False

    # *************************************************************************

    def enable(self):
        self.widget.configure(state="normal")
        self.enabled = True