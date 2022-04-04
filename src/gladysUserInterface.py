import io

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
	Student: Frank Bernal
	Module: gladysUserInterface
	Description: This module does …
"""


def runTests():
	"""
		tests some module functions using gemeric input
	"""

	print("running a few tests")

	average = compute.gpsAverage(4, 5)
	print("average = ", average)

	# delete the remaining code *in this function* and replace it with
	# your code. add more code to do what the assignment asks you to do.
	# add 3 more tests of different functions in different modules
	print("hello!")


def start():
	"""
		logs the user in, and runs the app, this funtion is complete.
	"""
	print("=====================================")
	print("Welcome to the Gladys West Map App")
	print("Please login to continue")
	print("=====================================")
	userName = userLogin.login()
	print()
	runApp(userName)


def runApp(userName):
	"""
		runs the app, this function is partially done, refer to other comments
	"""

	# loop until user types q
	userQuit = False
	while (not userQuit):

		# menu
		"""
			The menu display is done, however we need to link each option to 
			the appropriate module
		"""
		print("-- Welcome to the Gladys West Map App " + userName + "! --")
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

		# menu choices, use a switch-like if-elif control structure

		"""
			The test option works, current and destination positions are started, map is incomplete,
			quit works, and error is set.
		"""
		# Run tests
		if firstChar == 't':
			runTests()

		# Set current position
		elif firstChar == 'c':
			x = input("Please enter value for x: ")
			y = input("Please enter value for y: ")
			

		# Set destination position
		elif firstChar == 'd':
			x = input("Please enter value for x: ")
			y = input("Please enter value for y: ")

		# Map distance
		elif firstChar == 'm':
			runTests()
		
		# Quit
		elif firstChar == 'q':
			userQuit = True

		# Error message
		else:
			print("ERROR: " + firstChar + " is not a valid command")

	print("\n")
	print("Thank you for using the Gladys West Map App!")
	print("\n")
