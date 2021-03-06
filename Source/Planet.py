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
	SPEED_MULTIPLIER:
		This is used to speed up the rotations of the planets so they're 
		a bit better to watch

	DISTANCE_MULTIPLIER:
		Same as the above, but is used to alter the x and y positions.
	"""
	SPEED_MULTIPLIER = 10;
	DISTANCE_MULTIPLIER = 9;

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
		speed: 			The number of days it takes to circle the sun.
		phi: 			The variable that works as time.
	"""	
	def __init__(self, window, name, mass, xCoord, yCoord, size, color, aCoefficient, epsilon, speed):

		self.__window = window
		self.__name = name
		self.__mass = mass
		self.__xCoord = xCoord
		self.__yCoord = yCoord
		self.__size = size
		self.__color = color
		self.__aCoefficient = aCoefficient
		self.__epsilon = epsilon
		self.__speed = 0 if speed == 0 else (1 / speed) * self.SPEED_MULTIPLIER
		self.__phi = 0 

	"""
	Function: 
		animate

	Description:
		This is used to draw the planet and calculate its next
		position. It is called every step of the animation to
		draw that step and prepare for the next one.
	"""
	def animate(self):
   		self.drawPlanet()
		self.calculateNextPosition()

	""" 
	Function: 
		drawPlanet

	Description:
		This passes the planet's size and position to a window to be drawn.

	Args:
		self: 	Self from class.
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

	See:
		http://www.pa.msu.edu/~stump/champ/mech3f01.pdf
	"""	
	def calculateNextPosition(self):

		self.__xCoord = self.__aCoefficient * (math.cos(self.__phi) - self.__epsilon) * self.DISTANCE_MULTIPLIER
		self.__yCoord = self.__aCoefficient * math.sqrt(1 - self.__epsilon * self.__epsilon) * math.sin(self.__phi) * self.DISTANCE_MULTIPLIER
		self.__phi = 0 if self.__speed == 0 else (self.__phi + self.__speed) % (2 * math.pi)
