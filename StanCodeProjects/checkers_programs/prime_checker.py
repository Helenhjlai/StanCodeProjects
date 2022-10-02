"""
File: prime_checker.py
Name: Helen Lai
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	This program will check whether a number n is prime number or not.
	"""
	print('Welcome to the Prime Checker!')
	while True:
		n = int(input('n: '))
		if n == EXIT:
			break
		if is_prime(n):
			print(str(n) + ' is a prime number.')
		else:
			print(str(n) + ' is not a prime number.')
	print('Have a good one!')


def is_prime(n1):
	"""
	:param n1: int, a number to be check whether it is a prime number or not.
	:return: bool, if a number is a prime number, then return True. Otherwise, return False.
	"""
	for i in range(2, n1):
		if n1 % i == 0:
			return False
	return True


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
