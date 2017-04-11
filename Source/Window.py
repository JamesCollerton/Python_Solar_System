# ------------------------------------------------------------------------------

# Window

# This class holds the window information and all drawing methods.

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# IMPORTS

from Tkinter import *
from Constants import *

# ------------------------------------------------------------------------------

class Window:

	""" 
	Function: 
		Initialisation

	Description:
		Initialises the window with tkinter and creates the canvas and the canvas
		center.

	Args:
		self: From class
	"""	
	def __init__(self):

		master = Tk()

		self.createCanvas(master)
		self.createCentre()

	""" 
	Function: 
		createCanvas

	Description:
		This creates the canvas to be drawn to.

	Args:
		master: The tk master to put the canvas to.
	"""	
	def createCanvas(self, master):

		self.__canvas = Canvas(master, width = CONST.CANVAS_WIDTH, height = CONST.CANVAS_HEIGHT)
		self.__canvas.configure(background = 'black')
		self.__canvas.pack()
	
	""" 
	Function: 
		createCentre

	Description:
		This sets two variables to be the x and y geometric centre of the 
		canvas.

	Args:
		self: From class
	"""	
	def createCentre(self):

		self.__xCentre = CONST.CANVAS_WIDTH / 2
		self.__yCentre = CONST.CANVAS_HEIGHT / 2
	
	
	""" 
	Function: 
		drawCircle

	Description:
		This draws a circle to the window.

	Args:
		self: 	From class
		size: 	The radius of the circle
		xCoord: The x coordinate to draw the centre
		yCoord: The y coordinate to draw the centre
		color: 	The color of the circle
	"""	
	def drawCircle(self, size, xCoord, yCoord, color):
		
		canvasXCoord = self.__xCentre + xCoord
		canvasYCoord = self.__yCentre + yCoord

		self.__canvas.create_oval(canvasXCoord - size / 2, 
								  canvasYCoord - size / 2, 
								  canvasXCoord + size / 2, 
								  canvasYCoord + size / 2, 
								  fill = color)

	
	""" 
	Function: 
		mainLoop

	Description:
		The main loop that runs to render the window.

	Args:
		self: From class.
	"""	
	def mainLoop(self):

		mainloop();

	def after(self, delay, function):

		self.__canvas.after(delay, function)

	def clear(self):

		self.__canvas.delete("all")