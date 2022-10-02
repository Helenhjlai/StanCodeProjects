"""
File: extension1_factorial.py
Name: Helen Lai
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	This program will list the answer of factorial of the number that user entered.
	"""
	print("Welcome to stanCode factorial master!")
	number = int(input("Give me a number, and I will list the answer of factorial: "))

	if number == EXIT:
		print("- - - - - - See ya! - - - - - -")
	else:
		while True:
			factorial = 1
			if number == EXIT:
				break
			if number < 0:
				print('Please enter a positive integer!')
				number = int(input("Give me a number, and I will list the answer of factorial: "))
			if number == 0:
				print('Answer: ' + str(1))
				number = int(input("Give me a number, and I will list the answer of factorial: "))
			for i in range(number-1):
				factorial *= (i + 2)
			print('Answer: ' + str(int(factorial)))
			number = int(input("Give me a number, and I will list the answer of factorial: "))
		print("- - - - - - See ya! - - - - - -")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()
