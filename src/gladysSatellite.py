import io
import json

"""
	Student: Frank Bernal
	Module: gladysSatellite
	Description: This module reads "readSat()" 1 of 4 JSON files ("latitude", "longitude", 
				 "altitude", or "time") when called and stores it in variable "data". 
				 
				 The gpsValue() function uses the readSat() function to load the data from 
				 the JSON, Data is read into a dictionary using the X and Y values as keys, to 
				 retrieve the values and returns dataValue

	Status: readSat  [X]
		    gpsValue [X]

"""


def readSat(sat, pathToJSONDataFiles):
	"""
		reads satellite data from a json file
		Students do NOT need to change the readSat function.
	"""

	# data file path
	fileName = sat + "-satellite.json"
	filePath = pathToJSONDataFiles + "/" + fileName

	# open the file
	try:
		fileHandle = open(filePath)
	except IOError:
		print("ERROR: Unable to open the file " + filePath)
		raise IOError

	# print("filePath = ", filePath)

	# read the file
	data = json.load(fileHandle)

	return data


def gpsValue(x, y, sat):
	"""
		This function reads the satellite data required to the associated call from the compute 
		module. Reads the data into a dicitonary. Uses the Xand Y as a key to grab the value and 
		return to the module that called it.
	"""
	#initialize 
	dataValue = 0
	# Location of all JSONs
	pathToJSONDataFiles = "/Users/frankbernal/Documents/GitHub/gladysWestMapAppPy/src"

	# read the satellite data
	data = readSat(sat, pathToJSONDataFiles)

	# create an empty dictionary
	dataDictionary = {}

	# read data into dataDictionary
	# create keys to xVal and yVal to correlate to the value in the JSON
	for elem in data:
		xVal = elem["x"]
		yVal = elem["y"]
		value  = elem["value"]
		
		dataDictionary[(xVal, yVal)] = value
		
		# Find the user input as a key and return the value as dataValue
		# If X or Y is out of bounds return error
		if (x, y) in dataDictionary:
			dataValue = dataDictionary[(x, y)]
		else:
			dataValue = "ERROR: NO DATA FOUND WITH THOSE VALUES"
		
	return dataValue

# Test prints for all JSONs
#print(gpsValue(99, 46, "latitude"))
#print(gpsValue(99, 46, "longitude"))
#print(gpsValue(99, 46, "altitude"))
#print(gpsValue(99, 46, "time"))
