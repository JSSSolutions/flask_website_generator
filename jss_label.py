#
# jss_label.py
#
# Written by John Sowell
#
# Written 5/20/2020 - 6/10/2020 (43 lines)
#
# Defines the label class to be added to the subclassed window class
#
# 6/20/2020 Added an optional parameter to the constructor function to provide
#           the ability for labels to span more than one column in grid mode.
#           Also added vertical padding of 3 (47 lines total)
#
# 6/21/2020 Added a change text function. (73 lines total)
#
# 7/2/2020  Added an optional parameter in the constructor for which way
#           the label is to be anchored (in case it needs to be centered, for
#           example. (78 lines total)
#
# 7/2/2020  Took out the constants in this file, and added the reference to
#           jss_cons in its place. (78 lines)
#
from tkinter import *
from tkinter.font import Font

from jss_cons import *

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class jss_label:

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def __init__(self, parent, sx, sy, t='', sp=1, p=None, b='', f='', ff='', fs=8, anc='nw'):
        if p != None:
            self.widget = Label(parent.canvas, image=p)
        else:
            if ff == '':
                ff = parent.font_face
            if fs == 0:
                fs = parent.font_size
            if b == '':
                b = parent.background
            if f == '':
                f = parent.foreground

            self.mode = parent.mode
            self.canvas = parent.canvas
            self.foreground = f
            self.background = b
            self.start_x = sx
            self.start_y = sy
            self.span = sp
            self.anchor = anc

            self.font = Font(family=ff, size=fs)
            self.widget = Label(parent.canvas, width=len(t), text=t, bg=b, fg=f, font=self.font)

        if parent.mode == CANVAS_MODE:
            self.widget.pack()
            parent.canvas.create_window(sx, sy, anchor=anc, window=self.widget)
        else:
            self.widget.grid(row=sy, column=sx, columnspan=sp, pady=3)

    # *************************************************************************

    def change_text(self, t, cx=-1, cy=-1):
        if self.mode == CANVAS_MODE:
            self.widget.pack_forget()
        else:
            self.widget.grid_forget()
        self.widget = Label(self.canvas, width=len(t), text=t, bg=self.background, fg=self.foreground, font=self.font)

        if self.mode == CANVAS_MODE:
            self.widget.pack()
            if cx == -1 and cy == -1:
                self.canvas.create_window(self.start_x, self.start_y, anchor=self.anchor, window=self.widget)
            else:
                self.canvas.create_window(cx, cy, anchor=self.anchor, window=self.widget)

        else:
            self.widget.grid(row=self.start_y, column=self.start_x, columnspan=self.span, pady=3)