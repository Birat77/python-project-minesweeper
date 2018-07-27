import tkinter as tk
import sys

import classes as cls
import gui
import initialutils

# Set parameters if given
initialutils.set_parameters(sys.argv[1:])

# Initialze data
GRID = cls.Grid()
GRID.add_bombs()

# Create GUI
window = gui.create_main_window()
flag, mine = gui.create_images()
BOARD = gui.create_board(window, GRID, flag, mine)
top_frame = gui.create_top_frame(window, GRID, BOARD)

tk.mainloop()
