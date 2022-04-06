import io

import gladysSatellite as satellite
import math

"""
	Student: Frank Bernal
	Module: gladysCompute
	Description: This module does calculates the gpsAverage by calling for 4 
				 gpsValues (latitude, longitude, altitude, and time) based on x and y,
				 and dividing the sum of the 4, and dividing by 4, then return the average.

				 The distance() is calculated by adding the squares of the current gpsAverage
				 and the destination gpsAverage, and getting the square root of the total,
				 returns distance.

	Status: gpsAverage   [X]
			distance     [X]
			
"""


def gpsAverage(x, y):
	"""
		This function takes X and Y and gets its associated value for each satellite.
		The values are added together and divided by the number of satellites [4]
		returns Average
	"""

	"""
		Look up JSONs with (x,y, "latitude") 
						   (x,y, "longitude") 
						   (x,y, "altitude") 
						   (x,y, "time")
	"""

	latitude  = satellite.gpsValue(x, y, "latitude")
	longitude = satellite.gpsValue(x, y, "longitude")
	altitude  = satellite.gpsValue(x, y, "altitude")
	time      = satellite.gpsValue(x, y, "time")
	average = (latitude + longitude + altitude + time)/4 

	return average

def distance(current, destination):
	"""
		This function takes the current gpsAverage and destinationAverage, adds the 
		squares of each, then square roots the total. Returns distance
	"""

	distance = math.sqrt((current**2) + (destination**2))
	

	return distance

# Test values to test module functions using random values
#print("gpsAverage() = " + str(gpsAverage(56, 13)))
#print("distance() = " + str(distance(600, 435)))