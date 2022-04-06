import io

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
	Student: Frank Bernal
	Module: gladysUserInterface
	Description: This module acts as an interface for the user, with options to test,
				 set current position, set destination, map distance, run tests and quit.
	Status: Run tests [X]
			Start     [X]
			Run App   [X]
"""


def runTests():
	"""
		tests some module functions using gemeric input
	"""

	print("running a few tests...")

	# Check userLogin module
	print()
	print("====================================")
	print("**Testing userLogin**")
	print("====================================")
	testEmail = userLogin.login()
	print()
	print()
	print("testEmail = " + str(testEmail))

	# Check compute module
	print()
	print("====================================")
	print("**Testing gps calculations**")
	print("====================================")
	testAverage = compute.gpsAverage(4, 5)
	print("GPS average (X = 4, Y = 5)= ", str(testAverage))

	# Check satellite module
	print()
	print("====================================")
	print("**Testing file load**")
	print("====================================")
	testValue = satellite.readSat("latitude", "/Users/frankbernal/Documents/GitHub/gladysWestMapAppPy/src")
	if testValue != 0:
		print("Satellite files loaded successfully!")
	else:
		print("Failure to load satellite files.")
	
	# Done testing
	print()
	print("====================================")
	print("**Tests complete**")
	print("====================================")


def start():
	"""
		logs the user in, and runs the app.
	"""
	print("=====================================")
	print("Welcome to the Gladys West Map App")
	print("Please login to continue")
	print("=====================================")
	userName = userLogin.login()
	runApp(userName)


def runApp(userName):
	"""
		runs the app, gives the user the ability to set current position, destination,
		map distance, run tests, or quit.
	"""

	# loop until user types q
	# The following variables are initialized to zero
	userQuit = False
	currentX = 0
	currentY = 0
	destinationX = 0
	destinationY = 0
	distance = 0
	while (not userQuit):

		# menu
		"""
			The Menu allows users to input their current position and their destination position.
			Selecting Map computes the distance.
			Selecting run tests, tests the different modules
			
		"""
		print()
		print("=====================================")
		print("Welcome to the Gladys West Map App " + userName + "!")
		print("=====================================")
		print("Current position : X = " + str(currentX) +     " Y = " + str(currentY))
		print("Destination      : X = " + str(destinationX) + " Y = " + str(destinationY))
		print("Distance         : " + str(round(distance, 2)) + " miles")
		print("=====================================")
		print("Type [t] to run tests")
		print("Type [c] to set current position")
		print("Type [d] to set destination position")
		print("Type [m] to map")
		print("Type [q] to quit")
		print()

		# get first character of input
		userInput = input("Enter a command:")
		lowerInput = userInput.lower()
		firstChar = lowerInput[0:1]

		# menu choices, uses an if elif statement

		# Run tests
		if firstChar == 't':
			runTests()

		# Set current position
		elif firstChar == 'c':
			currentX = input("Please enter value for x: ")
			currentY = input("Please enter value for y: ")
			

		# Set destination position
		elif firstChar == 'd':
			destinationX = input("Please enter value for x: ")
			destinationY = input("Please enter value for y: ")

		# Map distance
		elif firstChar == 'm':
			currentAverage = compute.gpsAverage(int(currentX), int(currentY))
			destinationAverage = compute.gpsAverage(int(destinationX), int(destinationY))
			distance = compute.distance(float(currentAverage), float(destinationAverage))
		
		# Quit
		elif firstChar == 'q':
			userQuit = True

		# Error message
		else:
			print("ERROR: " + firstChar + " is not a valid command")

	print("\n")
	print("Thank you for using the Gladys West Map App!")
	print("\n")
