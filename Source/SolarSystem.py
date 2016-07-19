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
		self.__planets = self.createPlanetList()

		window = Window()

		for planet in self.__planets:
			planet.drawPlanet(window)

		window.mainLoop()

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

		sun = Planet("Sun", 330000, 0, 0, 5, "yellow")
		mercury = Planet("Mercury", 0.06, 0.387, 0, 5, "grey")
		venus = Planet("Venus", 0.82, 0.723, 0, 5, "orange")
		earth = Planet("Earth", 1, 1, 0, 5, "blue")
		mars = Planet("Mars", 0.11, 1.524, 0, 5, "gold2")
		jupiter = Planet("Jupiter", 317.8, 5.203, 0, 5, "thistle4")
		saturn = Planet("Saturn", 95.2, 9.582, 0, 5, "khaki2")
		uranus = Planet("Uranus", 14.6, 19.201, 0, 5, "skyblue")
		neptune = Planet("Neptune", 17.2, 30.047, 0, 5, "royalblue3")

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