# ------------------------------------------------------------------------------

# SolarSystem Class

# This is the Solar System class which holds all of the planets and controls
# their interaction.

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# IMPORTS

from Planet import *
from Window import *

# ------------------------------------------------------------------------------

class SolarSystem:

	""" 
	Function: 
		Initialisation.

	Description:
		This initialises the solar system class by creating all of the arguments
		and adding them to a list.

	Args:
		self: Self from class.
	"""	 
	def __init__(self):

		self.SPEED = 1
		self.__window = Window()
		self.__planets = self.createPlanetList()
		self.animate()

		# for planet in self.__planets:
		# 	planet.animate()

		self.__window.mainLoop()

	""" 
	Function: 
		createPlanetList

	Description:
		This creates a list of all of the planets and then appends them to
		an array

	Args:
		self: Self from class.

	Returns:
		planets: A list of the planets.
	"""	
	def createPlanetList(self):

		sun = Planet(self.__window, "Sun", 330000, 0, 0, 5, "yellow", 0, 0, 0)
		mercury = Planet(self.__window, "Mercury", 0.06, 0.387, 0, 5, "grey", 0.3871, 0.2056, 87.969)
		venus = Planet(self.__window, "Venus", 0.82, 0.723, 0, 5, "orange", 0.7233, 0.0068, 224.701)
		earth = Planet(self.__window, "Earth", 1, 1, 0, 5, "blue", 1.000, 0.0167, 365.256)
		mars = Planet(self.__window, "Mars", 0.11, 1.524, 0, 5, "gold2", 1.5273, 0.0934, 686.98)
		jupiter = Planet(self.__window, "Jupiter", 317.8, 5.203, 0, 5, "thistle4", 5.2028, 0.0484, 4329.63)
		saturn = Planet(self.__window, "Saturn", 95.2, 9.582, 0, 5, "khaki2", 9.5388, 0.0542, 10751.805)
		uranus = Planet(self.__window, "Uranus", 14.6, 19.201, 0, 5, "skyblue", 19.1914, 0.0472, 30664.015)
		neptune = Planet(self.__window, "Neptune", 17.2, 30.047, 0, 5, "royalblue3", 30.0611, 0.0086, 60148.35)

		planets = []
		planets.append(sun)
		planets.append(mercury)
		planets.append(venus)
		planets.append(earth)
		planets.append(mars)
		planets.append(jupiter)
		planets.append(saturn)
		planets.append(uranus)
		planets.append(neptune)

		return planets

	def animate(self):

		self.__window.clear()

		for planet in self.__planets:
			planet.animate()		

		self.__window.after(self.SPEED, self.animate)
