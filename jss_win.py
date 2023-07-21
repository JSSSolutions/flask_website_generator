#
# jss_win.py
#
# Written by John Sowell
#
# Written 5/18/2020 - 6/10/2020 (42 lines)
#
# Defines the window class to be subclassed
#
# 6/22/2020 Added member variables representing the starting coordinates for
#           the window. (47 lines total)
#
# 7/2/2020  Took out constants, included jss_cons (46 lines)
#
from tkinter import *

from jss_cons import *

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# this needs to be subclassed so that the widgets classes can be added
class jss_win:

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def __init__(self, master, t, w, h, m,  b, f, r, c, sx, sy, ff, fs):
        master.title(t)
        master.geometry("+%d+%d" % (sx, sy))
        self.canvas = Canvas(width=w, height=h, bg=b)

        self.mode = m
        if self.mode == CANVAS_MODE:
            self.canvas.pack(expand=NO, fill=BOTH)
        else:
            self.canvas.grid(rows=r, columns=c)

        self.start_x = sx
        self.start_y = sy
        self.width = w
        self.height = h
        self.rows = r
        self.columns = c
        self.background = b
        self.foreground = f
        self.font_face = ff
        self.font_size = fs