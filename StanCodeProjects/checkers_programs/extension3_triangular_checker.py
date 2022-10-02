"""
File: extension3_triangular_checker.py
Name: Helen Lai
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program will check whether a number is triangular number or not.
    """
    print('Welcome to the triangular number checker!')
    n = int(input('n: '))
    if n == EXIT:
        print('Have a good one!')
    else:
        while True:
            if n == EXIT:
                break
            if n < 0:
                print('Please enter a positive integer!')
                n = int(input('n: '))
            if triangular_check(n):
                print(str(n) + ' is a triangular number')
            else:
                print(str(n) + ' is not a triangular number')
            n = int(input('n: '))
        print('Have a good one!')


def triangular_check(n1):
    """
    :param n1: int, a number to be check whether it's triangular number or not.
    :return: bool, if a number is a triangular number, then return True. Otherwise, return False.
    """
    number = 1
    sum_tri = number
    while True:
        if sum_tri > n1 or sum_tri == n1:
            break
        if sum_tri < n1:
            number += 1
            sum_tri += number
    if sum_tri == n1:
        return True
    return False


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
