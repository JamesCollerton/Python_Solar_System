# ------------------------------------------------------------------------------

# Planet Class

# This is the planet class. Each planet has a name, mass and an x and a y 
# coordinate that are initialised to a certain value.

# ------------------------------------------------------------------------------

from Constants import *


class Planet:

	def __init__(self, name, mass, xCoord, yCoord, size, color):

		self.__name = name
		self.__mass = mass
		self.__xCoord = (xCoord / 30.047) * ((CONST.CANVAS_WIDTH / 2) - 20)
		self.__yCoord = yCoord
		self.__size = size
		self.__color = color

	def printPlanetInfo(self):

		print self.__name
		print self.__mass
		print self.__xCoord
		print self.__yCoord
		print self.__size

	def drawPlanet(self, window):

		window.drawCircle(self.__size, self.__xCoord, self.__yCoord, self.__color)


