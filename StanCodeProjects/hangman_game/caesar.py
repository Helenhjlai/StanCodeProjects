"""
File: caesar.py
Name: Helen Lai
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program will decipher a caesar cipher string.
    """
    n = int(input('Secret Number: '))
    cipher = input('What\'s the ciphered string? ')

    # Create a new alphabet string
    new_alphabet = ALPHABET[len(ALPHABET) - n:len(ALPHABET) + 1] + ALPHABET[0:len(ALPHABET) - n]
    cipher = cipher.upper()  # make cipher string all upper case
    decipher = ""

    for i in range(len(cipher)):
        if cipher[i] == "":
            decipher += ""
        if new_alphabet.find(cipher[i]) == -1:  # deal with ex: !,?,「」,", etc.
            decipher += cipher[i]
        for j in range(len(ALPHABET)):
            if cipher[i] == new_alphabet[j]:
                decipher += ALPHABET[j]

    print('The deciphered string is: ' + decipher)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
