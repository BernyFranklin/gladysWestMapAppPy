import io
import getpass

"""
	Student: Frank Bernal
	Module: gladysUserLogin
	Description: This module prompts the user for their email address and password
	Status: COMPLETE
"""


def login():
	"""
		The login() function prompts the user for an email address, 
		it starts a loop and only proceeds when the "@" and "." are present,
		this code is very basic and only checks if the characters are present, 
		not if they're in the right order. 
	"""

# Set flags to false to prime the loop
	atEmail = False
	dotEmail = False
	
# Loop will cycle until atEmail and dotEmail are true
	while (atEmail == False or dotEmail == False):
		# Prompt for user to enter email address
		emailAddress = input("Please enter your email adress: ")
		# Bool variables to check if the chars "@" and "." are present
		atEmail = ("@" in emailAddress)
		dotEmail = ("." in emailAddress)
		# Test prints "@/. present? True or False"
		#print("@ present? " + str(atEmail))
		#print(". present? " + str(dotEmail))

		# If either flag is set to false, alert user and try again
		if (atEmail == False or dotEmail == False):
			print("Invalid email addresss, please try again")

	# Loop has been exited and user proceeds to input password
	password = getpass.getpass("Please enter your password: ")

	#return emailAddress to UserInterface
	return emailAddress
