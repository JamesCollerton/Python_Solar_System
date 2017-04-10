# ------------------------------------------------------------------------------

# Planet Class

# This is the planet class. Each planet has a name, mass and an x and a y 
# coordinate that are initialised to a certain value.

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# IMPORTS

from Constants import *

# ------------------------------------------------------------------------------

class Planet:

	""" 
	Function: 
		Initialisation

	Description:
		This initialises the planet with its name, mass, X coordinate, Y 
		coordinate, size and color.

	Args:
		self: Self from class.
		name: The name of the planet.
		mass: The mass of the planet.
		xCoord: The xCoordinate of the planet.
		yCoord: The yCoordinate of the planet.
		size: The radius of the planet.
		color: The color to draw the planet to screen.
		aCoefficient: The a coefficient in the equation for an ellipse.
		bCoefficient: The b coefficient in the equation for an ellipse.
	"""	
	def __init__(self, name, mass, xCoord, yCoord, size, color, aCoefficient = 1, bCoefficient = 1):

		self.__name = name
		self.__mass = mass
		self.__xCoord = (xCoord / 30.047) * ((CONST.CANVAS_WIDTH / 2) - 20)
		self.__yCoord = yCoord
		self.__size = size
		self.__color = color
		self.__aCoefficient = aCoefficient
		self.__bCoefficient = bCoefficient

	""" 
	Function: 
		drawPlanet

	Description:
		This passes the planet's size and position to a window to be drawn.

	Args:
		self: Self from class.
		window: The window to draw to.
	"""	
	def drawPlanet(self, window):

		window.drawCircle(self.__size, self.__xCoord, self.__yCoord, self.__color)

	""" 
	Function: 
		calculateNextPosition

	Description:
		This tells the planet where its next x and y positions should be

	Args:
		self: Self from class.
	"""	
	def calculateNextPosition(self):

		a = 1;

