# ------------------------------------------------------------------------------

from Planet import *
from Window import *

# ------------------------------------------------------------------------------
# MAIN

# This is the main class run on startup.

def main():

	sun = Planet("Sun", 100, 0, 0)
	moon = Planet("Moon", 10, 0, 10)
	window = Window()
	

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()