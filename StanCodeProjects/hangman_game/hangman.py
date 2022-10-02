"""
File: hangman.py
Name: Helen Lai
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program will play the hangman game.
    """
    new_turn = N_TURNS
    ans = random_word()

    dash = ""
    for i in range(len(ans)):
        dash += "-"
    print("The word looks like " + dash)
    print("You have " + str(N_TURNS) + ' wrong guesses left.')
    ch = input('Your guess: ')
    ch = ch.upper()
    guess_word = dash

    while True:
        if len(ch) > 1 or not ch.isalpha():
            print('Illegal Format.')
            ch = input('Your guess: ')
            ch = ch.upper()
        else:
            # to detect whether a user's guess(ch) is in the ans' string or not
            if ans.find(ch) != -1:
                guess_word = replace(guess_word, ch, ans)  # replace the word with the user's guess(ch)
                if guess_word == ans:
                    print('You are correct!\nYou win!')
                    break
                else:
                    print('You are correct!\nThe word looks like ' + guess_word)
                    print('You have ' + str(new_turn) + ' wrong guesses left')

            else:
                new_turn -= 1  # wrong guess, then turns -1

                # if having 0 turns left, game over.
                if new_turn != 0:
                    print('There is no ' + ch + '\'s in the word.\nThe word looks like ' + guess_word)
                    print('You have ' + str(new_turn) + ' wrong guesses left')
                else:
                    print('There is no ' + ch + '\'s in the word.\nThe word looks like ' + guess_word)
                    print('You are completely hung : (')
                    break

            ch = input('Your guess: ')
            ch = ch.upper()

    print('The word was: ' + ans)


def replace(old_s, new_guess, ans):
    """
    :param old_s: str, the old string.
    :param new_guess: str, a new character a user entered.
    :param ans: str, the answer
    :return: str, newly replaced string, named "guess_word".
    """
    guess_word = ""
    for i in range(len(ans)):
        if new_guess != ans[i]:
            guess_word += old_s[i]
        else:
            guess_word += new_guess
    return guess_word


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
