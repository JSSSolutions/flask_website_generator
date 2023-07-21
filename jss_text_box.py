#
# jss_text_box.py
#
# Written by John Sowell
#
# Written 5/20/2020 - 6/10/2020 (49 lines)
#
# Defines the text box class to be added to the subclassed window class
#
# 6/21/2020 Added a parameter to the constructor function, giving the user
#           the ability to select a password-type text box. (59 lines total)
#
# 6/23/2020 Added a new function to change text in the box (91 lines total)
#
# 6/24/2020 Added a new parameter to the constructor function for the span
#           (94 lines)
#
# 6/27/2020 Added the ability to disable the text box (116 lines total)
#
# 7/3/2020  Replaced constants with jss_cons (115 lines total)
#
from tkinter import *
from tkinter.font import Font

from jss_cons import *

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class jss_text_box:

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def __init__(self, parent, sx, sy, w=20, h=1, pw=False, t='', sp=1, fp=None, b='#ffffff', f='#000000', ff='', fs=0):
        self.enabled = True
        self.function = fp
        if ff == '':
            ff = parent.font_face
        if fs == 0:
            fs = parent.font_size
        self.font = Font(family=ff, size=fs)
        self.password_box = pw
        self.mode = parent.mode
        self.width = w
        self.height = h
        self.background = b
        self.foreground = f
        self.canvas = parent.canvas
        self.function = fp
        self.start_x = sx
        self.start_y = sy
        if pw == False:
            self.widget = Text(parent.canvas, width=w, height=h, bg=b, fg=f, font=self.font)
        else:
            self.widget = Entry(parent.canvas, width=w, bg=b, fg=f, font=self.font, show="*")
        self.widget.insert(END, t)
        if parent.mode == CANVAS_MODE:
            self.widget.pack()
        self.widget.bind('<Key>', self.key_pressed)
        if parent.mode == CANVAS_MODE:
            parent.canvas.create_window(sx, sy, anchor='nw', window=self.widget)
        else:
            self.widget.grid(row=sy, column=sx, columnspan=sp)

    # *************************************************************************

    def change_text(self, t):
        if self.mode == CANVAS_MODE:
            self.widget.pack_forget()
        else:
            self.widget.grid_forget()
        if self.password_box == False:
            self.widget = Text(self.canvas, width=self.width, height=self.height, bg=self.background, fg=self.foreground, font=self.font)
        else:
            self.widget = Entry(self.canvas, width=self.width, bg=self.background, fg=self.foreground, font=self.font, show="*")
        self.widget.insert(END, t)
        if self.mode == CANVAS_MODE:
            self.widget.pack()
        if self.function != None:
            self.widget.bind('<Key>', self.function)
        if self.mode == CANVAS_MODE:
            self.canvas.create_window(self.start_x, self.start_y, anchor='nw', window=self.widget)
        else:
            self.widget.grid(row=self.start_y, column=self.start_x, padx=3, pady=3)

    # *************************************************************************

    def delete_text(self):
        self.widget.delete("1.0", "end-1c")

    # *************************************************************************

    def disable(self):
        self.widget.configure(status="disabled")
        self.enabled = False

    # *************************************************************************

    def enable(self):
        self.widget.configure(status="normal")
        self.enabled = True

    ###########################################################################

    def get_text(self):
        if self.password_box == False:
            return self.widget.get("1.0", "end-1c")
        else:
            return self.widget.get()

    # *************************************************************************

    def key_pressed(self, event_info):
        if self.enabled == False or self.function == None:
            return
        self.function(event_info)