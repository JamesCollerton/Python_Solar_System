from Tkinter import *
from Constants import *

class Window:

	def __init__(self):

		master = Tk()

		w = Canvas(master, width=CONST.CANVAS_WIDTH, height=500)
		w.configure(background='black')
		w.pack()

		w.create_line(0, 0, 200, 100)
		w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

		w.create_rectangle(50, 25, 150, 75, fill="blue")

		mainloop()