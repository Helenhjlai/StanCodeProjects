"""
File: extension2_number_checker.py
Name: Helen Lai
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program will check whether the number is perfect, abundant, or deficient.
    """
    print('Welcome to number checker!')
    n = int(input('n: '))
    if n == EXIT:
        print('Have a good one!')
    else:
        while True:
            divisor = 1
            if n == EXIT:
                break
            for i in range(2, n):
                if n % i == 0:
                    divisor += i

            if divisor == n:
                print(str(n) + ' is a perfect number')
            elif divisor > n:
                print(str(n) + '  is a abundant number')
            else:
                print(str(n) + ' is a deficient number')
            n = int(input('n: '))
        print('Have a good one!')


# def find_divisor(n1):
#     """
#     :param n1: int, a number that to be found out its all divisors.
#     :return: list, return a list contains all divisors of n1
#     """
#     divisor = [1]
#     for i in range(2, n1 + 1):
#         if n1 % i == 0:
#             divisor.append(i)
#     return divisor


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
