"""
File: extension4_narcissistic_checker.py
Name: Helen Lai
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program is to check whether a number is a narcissistic number or not.
    """
    print('Welcome to the narcissistic number checker!')
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
            if narcissistic(n):
                print(str(n) + ' is a narcissistic number')
            else:
                print(str(n) + ' is not a narcissistic number')
            n = int(input('n: '))
        print('Have a good one!')


def narcissistic(n1):
    """
    :param n1: int, a number to be checked whether it's a narcissistic number or not.
    :return: bool, if a number is a narcissistic number, then return True. Otherwise, return False.
    """
    a = 0
    sum_n = a
    for i in range(0, len(str(n1))):
        a = int(str(n1)[i]) ** len(str(n1))
        sum_n += a
    if sum_n % n1 == 0:
        return True
    return False


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
