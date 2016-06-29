from Tkinter import *

class Window:

	def __init__(self):

		# rootWindow = Tk()
		# windowFrame = Frame(rootWindow)

		# w = Label(rootWindow, text="Hello, world!")
		# w.pack()

		# rootWindow.mainloop()

		master = Tk()

		w = Canvas(master, width=200, height=100)
		w.pack()

		w.create_line(0, 0, 200, 100)
		w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

		w.create_rectangle(50, 25, 150, 75, fill="blue")

		mainloop()