# ------------------------------------------------------------------------------

# Window

# This class holds the window information and all drawing methods.

# ------------------------------------------------------------------------------

from Tkinter import *
from Constants import *

class Window:

	def __init__(self):

		master = Tk()

		self.createCanvas(master)
		self.createCentre()

	def createCanvas(self, master):

		self.__canvas = Canvas(master, width = CONST.CANVAS_WIDTH, height = CONST.CANVAS_HEIGHT)
		self.__canvas.configure(background = 'black')
		self.__canvas.pack()

	def createCentre(self):

		self.__xCentre = CONST.CANVAS_WIDTH / 2
		self.__yCentre = CONST.CANVAS_HEIGHT / 2

	def drawCircle(self, size, xCoord, yCoord, color):
		
		canvasXCoord = self.__xCentre + xCoord
		canvasYCoord = self.__yCentre + yCoord

		self.__canvas.create_oval(canvasXCoord - size / 2, 
								  canvasYCoord - size / 2, 
								  canvasXCoord + size / 2, 
								  canvasYCoord + size / 2, 
								  fill = color)

	def mainLoop(self):

		mainloop();