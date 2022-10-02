"""
File: hailstone.py
Name: Helen Lai
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program computes Hailstone Sequences.
    If a number is odd, then make 3 multiple this number and plus 1
    If a number is even, then take half on it
    repeat steps mentioned above until the number reaches 1
    """
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number: '))
    count = 0
    if n == 1:
        print('It took 0 step to reach 1.')
    else:
        while n != 1:
            if n % 2 == 0:
                new_n = n / 2
                print(str(int(n)) + ' is even, so I take half: ' + str(int(new_n)))
            else:
                new_n = 3 * n + 1
                print(str(int(n)) + ' is odd, so I make 3n+1: ' + str(int(new_n)))
            n = new_n
            count += 1  # count steps
        print('It took ' + str(int(count)) + ' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
