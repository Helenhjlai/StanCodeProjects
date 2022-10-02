"""
File: quadratic_solver.py
Name: Helen Lai
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program will count the square roots of a quadratic function (ax^2 + bx + c = 0),
	which is based on the coefficients (a, b, c) that users enter.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('enter a = '))
	b = int(input('enter b = '))
	c = int(input('enter c = '))
	discriminant = b ** 2 - 4 * a * c
	if discriminant > 0:
		x1 = (-b + math.sqrt(discriminant)) / (2 * a)
		x2 = (-b - math.sqrt(discriminant)) / (2 * a)
		print('Two roots: ' + str(x1) + ' , ' + str(x2))
	elif discriminant == 0:
		x1 = -b / 2 * a
		print('One root: ' + str(x1))
	else:
		print('No real roots')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
