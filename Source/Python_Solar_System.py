# ------------------------------------------------------------------------------

# Python Solar System

# This is a short Python program I am writing to model the solar system and
# to understand classes in Python.

# ------------------------------------------------------------------------------
# IMPORTS

from Planet import *
from Window import *

# ------------------------------------------------------------------------------
# MAIN

# This is the main class run on startup.

def main():

	sun = Planet("Sun", 100, 0, 0, 300)
	moon = Planet("Moon", 10, 0, 10, 100)
	window = Window()
	moon.drawPlanet(window)
	

# ------------------------------------------------------------------------------
# RUNNING MAIN

if __name__ == "__main__":
    main()