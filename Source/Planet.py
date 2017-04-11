# ------------------------------------------------------------------------------

# Planet Class

# This is the planet class. Each planet has a name, mass and an x and a y 
# coordinate that are initialised to a certain value.

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# IMPORTS

from Constants import *
import math

# ------------------------------------------------------------------------------

class Planet:

	""" 
	Function: 
		Initialisation

	Description:
		This initialises the planet with its name, mass, X coordinate, Y 
		coordinate, size and color.

	Args:
		self: 			Self from class.
		window: 		The window the planet will be drawn in
		name: 			The name of the planet.
		mass: 			The mass of the planet.
		xCoord: 		The xCoordinate of the planet.
		yCoord: 		The yCoordinate of the planet.
		size: 			The radius of the planet.
		color: 			The color to draw the planet to screen.
		aCoefficient: 	The a coefficient in the equation for an ellipse.
		bCoefficient: 	The b coefficient in the equation for an ellipse.
		phi: 			The variable that works as time
	"""	
	def __init__(self, window, name, mass, xCoord, yCoord, size, color, aCoefficient = 1, epsilon = 1, phi = 0):

		self.__window = window
		self.__name = name
		self.__mass = mass
		self.__xCoord = (xCoord / 30.047) * ((CONST.CANVAS_WIDTH / 2) - 20)
		self.__yCoord = yCoord
		self.__size = size
		self.__color = color
		self.__aCoefficient = aCoefficient
		self.__epsilon = epsilon
		self.__phi = phi

	def animate(self):
		
   		self.drawPlanet()
		self.calculateNextPosition()
		self.__window.after(100, self.animate)

	""" 
	Function: 
		drawPlanet

	Description:
		This passes the planet's size and position to a window to be drawn.

	Args:
		self: 	Self from class.
		window: The window to draw to.
	"""	
	def drawPlanet(self):

		self.__window.drawCircle(self.__size, self.__xCoord, self.__yCoord, self.__color)

	""" 
	Function: 
		calculateNextPosition

	Description:
		This tells the planet where its next x and y positions should be, as well
		as incrementing the phi variable which acts as time

	Args:
		self: Self from class.
	"""	
	def calculateNextPosition(self):

		self.__xCoord = self.__aCoefficient * (math.cos(self.__phi) - self.__epsilon)
		self.__yCoord = self.__aCoefficient * math.sqrt(1 - self.__epsilon * self.__epsilon) * math.sin(self.__phi)
		self.__phi = self.__phi + 0.01
