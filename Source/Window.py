# ------------------------------------------------------------------------------

# Window

# This class holds the window information and all drawing methods.

# ------------------------------------------------------------------------------

from Tkinter import *
from Constants import *

class Window:

	def __init__(self):

		master = Tk()

		self.__canvas = Canvas(master, width = CONST.CANVAS_WIDTH, height = CONST.CANVAS_HEIGHT)
		self.__canvas.configure(background='black')
		self.__canvas.pack()

		# w.create_line(0, 0, 200, 100)
		# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

		# w.create_rectangle(50, 25, 150, 75, fill="blue")

		# mainloop()

	def drawCircle(self, size, xCoord, yCoord):
		
		self.__canvas.create_oval(0, 0, 100, 100, fill = "blue")
		mainloop()