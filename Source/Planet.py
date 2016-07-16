# ------------------------------------------------------------------------------

# Planet Class

# This is the planet class. Each planet has a name, mass and an x and a y 
# coordinate that are initialised to a certain value.

# ------------------------------------------------------------------------------

class Planet:

	def __init__(self, name, mass, xCoord, yCoord, size):

		self.__name = name
		self.__mass = mass
		self.__xCoord = xCoord
		self.__yCoord = yCoord
		self.__size = size

	def printPlanetInfo(self):

		print self.__name
		print self.__mass
		print self.__xCoord
		print self.__yCoord

	def drawPlanet(self, window):

		window.drawCircle(self.__mass, self.__xCoord, self.__yCoord)


