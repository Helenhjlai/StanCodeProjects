"""
File: name_sq.py (extension)
Name: Helen Lai
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    This program will show the square pattern of the given name.
    """
    print('This program prints a name in a square pattern! ')
    name = input('Name: ')
    print(name)
    n = 1

    # codes below will print out the body(i.e. without first and last line) of the square pattern
    for i in name[1:len(name)-1]:
        space = ""
        square_body = ""
        n += 1
        for j in range(len(name)-2):
            space += " "
        square_body = square_body + i + space + name[len(name)-n]
        print(square_body)

    # last line is a reversed string of the given name
    print(reverse(name))


def reverse(string):
    """
    :param string: str, the given name
    :return: str, reversed string
    """
    result = ""
    for i in range(len(string)):
        result = string[i] + result
    return result


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
