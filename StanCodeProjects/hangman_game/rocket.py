"""
File: rocket.py
Name: Helen Lai
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    This program will draw ASCII art - a rocket.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    This program will draw the head of the rocket.
    """
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(" ", end="")
        for j in range(i+1):
            print("/", end="")
        for j in range(i+1):
            print("\\", end="")
        for j in range(SIZE-i):
            print(" ", end="")
        print("")


def belt():
    """
    This program will draw the belt of the rocket.
    """
    print('+', end="")
    for i in range(SIZE):
        print('=', end="")
    for i in range(SIZE):
        print('=', end="")
    print('+', end="")
    print("")


def upper():
    """
    This program will draw the upper body of the rocket.
    """
    for i in range(SIZE):
        print('|', end="")
        for j in range(SIZE-1-i):
            print('.', end="")
        for j in range(i+1):
            print("/" + "\\", end="")
        for j in range(SIZE-1-i):
            print(".", end="")
        print('|', end="")
        print("")


def lower():
    """
    This program will draw the lower body of the rocket.
    """
    for i in range(SIZE):
        print('|', end="")
        for j in range(i):
            print('.', end="")
        for j in range(SIZE-i):
            print('\\' + '/', end="")
        for j in range(i):
            print('.', end="")
        print('|', end="")
        print("")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
