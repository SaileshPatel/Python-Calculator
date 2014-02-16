# Credit goes to Sergio Tapia from 'http://www.dreamincode.net/forums/topic/198544-creating-a-console-based-calculator-in-python/'.

# Created function which converts strings.
def convertString(str):
	try:
		# Conversion in to integer.
		returnValue = int(str)
	except ValueError:
		# If conversion in to an integer fails, then it will convert in to a float.
		returnValue = float(str)
	return returnValue

# Created function to perform addition.
# The function takes two variables; 'a' and 'b'.
def addition(a, b):
	# This returns the total of 'a' and 'b' added together.
	return convertString(a) + convertString(b)

# Created function to perform subtraction.
# The function takes two variables; 'a' and 'b'
def subtraction(a, b):
	# This returns the sum of 'a' subtracted by 'b'.
	return convertString(a) - convertString(b)

# Created functon to perform multiplication.
# The function takes two variables.
def multiplication(a, b):
	# This returns the sum of 'a' multiplied by 'b'.
	return convertString(a) * convertString(b)

# Created a function for perform division.
# The function takes two variables.
def division(a, b):
	# This returns the sum of 'a' divided by 'b'.
	return convertString(a) / convertString(b)

# Created variable with the value of 'True'.
keepProgramRunning = True

# Printed string.
print "Welcome to the Calculator!"

# Created loop, to keep program running.
while keepProgramRunning:
	# Printed string.
	print "Please choose what you'd like to do:"

	# Printed multiple strings.
	print "1: Addition"
	print "2: Subtraction"
	print "3: Multiplication"
	print "4: Division"
	print "5: Quit"

	# Created variable, which takes user inputed string. 
	choice = raw_input()

	# If the user entered '1', then the program performs this.
	if choice == "1":
		# Collected user inputted string.
		a = raw_input("Please enter the number which you wish to add to: ")
		# Collected user inputted string.
		b = raw_input("Please enter the number you wish to add by: ")
		# Printed string.
		print "Here's your answer!"
		# Print the result of the function 'addition' with the parameters 'a' and 'b' 
		print addition(a, b)
		# After this operator has been completed, the program goes back to the beginning.

	# If the user entered '2', then the program performs this.
	elif choice == "2":
		# Collected user inputted string
		a = raw_input("Please enter the number you wish to subtract from: ")
		# Collected user inputted string
		b = raw_input("Please enter the number you wish to subrract by: ")
		# Printed string
		print "Here's your answer!"
		# Print the result of the function 'subtractions' with the parameters 'a' and 'b'
		print subtraction(a, b)

	# If the user entered '3', then the program performs this.
	elif choice == "3":
		# Collected user inputted string
		a = raw_input("Please enter the number you wish to multiply: ")
		# Collected user inputted string
		b = raw_input("Please enter the number yuo wish to multiply by: ")
		# Printed string
		print "Here's your answer!"
		# Print the result of the function 'multiplication' with the parameters 'a' and 'b'
		print multiplication(a, b)

	# If the user entered '4', the program perfoms this.
	elif choice == "4":
		# Collected user inputted string
		a = raw_input("Please enter the number you wish to divide: ")
		# Collected user inputted string
		b = raw_input("Please enter the amount you wish to divide by: ")
		# Printed string
		print "Here's your answer!"
		# Print the result of the function 'division' with the parameters 'a' and 'b'
		print division(a, b)

	# If the user entered '5' this happens.
	elif choice == "5":
		# Printed string
		print "Bye!"
		# Assigns the value 'False' to the variable 'keepProgramRunning' which closes the program.
		# This is because this program only runs if 'keepProgramRunning' has the value of 'True'
		keepProgramRunning = False

	# If the user enters other value, this happens.
	else:
		# Print string
		print "Please choose a valid option."
		print "\n"
		# After this, the program goes back to the beginning.
