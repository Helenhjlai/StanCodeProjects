"""
File: complement.py
Name: Helen Lai
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program will find the complement of a DNA strand.
    """
    c = input("Please give me a DNA strand and I'll find the complement: ")
    c = c.upper()
    build_complement(c)


def build_complement(s):
    """
    :param s: str, a DNA strand
    :return: str, the complement of the DNA strand, s.
    """
    com = ""
    for i in range(len(s)):
        c = s[i]
        if c == 'A':
            c = 'T'
        elif c == "T":
            c = "A"
        elif c == "C":
            c = "G"
        else:
            c = "C"
        com += c
    print('The complement of ' + s + ' is ' + com)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
