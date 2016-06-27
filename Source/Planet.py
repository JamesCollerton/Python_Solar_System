# This is the planet class. 

class Planet:

	def __init__(self, name, mass):

		self.__name = name
		self.__mass = mass

	def printPlanetInfo(self):

		print self.__name
		print self.__mass