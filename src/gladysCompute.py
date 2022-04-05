import io

import gladysSatellite as satellite
import math

"""
	Student: Gabriel Solomon
	Module: gladysCompute
	Description: This module does …
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
		Look up in JSONs (x,y, lat) (x,y, long) (x,y, alt) (x,y, time)
	"""
	latitude  = satellite.gpsValue(x, y, "latitude")
	longitude = satellite.gpsValue(x, y, "longitude")
	altitude  = satellite.gpsValue(x, y, "altitude")
	time      = satellite.gpsValue(x, y, "time")
	#value = satellite.gpsValue(5, 6, "altitude")
	average = (latitude + longitude + altitude + time)/4 
	#average = value / 2

	return average



def distance(current, destination):
	"""
		document your function definition here. what does it do?
	"""

	"""
		delete the remaining code *in this function* and replace it with
		your own code. add more code to do what the assignment asks of you.
	"""
	distance = math.sqrt((current**2) + (destination**2))
	

	return distance

