"""
File: similarity.py (extension)
Name: Helen Lai
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program will compare short dna sequence with sub sequence of a long dna sequence
    and to find a best match.
    """
    s1 = input('Please give a DNA sequence to search: ')
    s2 = input('What DNA sequence would you like to match? ')
    s1 = s1.upper()
    s2 = s2.upper()
    s = 0
    match = 0
    best_match = ""

    for i in range(len(s1) - len(s2) + 1):  # len(s1)-len(s2)+1 is the times s2 is compared in s1
        ch = s1[i: i + len(s2)]
        n = 0
        for j in range(len(s2)):  # to count how many dna is matching
            if s2[j] == ch[j]:
                n += 1
        # find out the maximum similarity ratio
        if n / len(s2) > s:
            s = n / len(s2)
            match = i  # to find out from which indexed dna has the maximum similarity ratio
    best_match += s1[match: match + len(s2)]

    print('The best match is ' + best_match)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
