"""
File: anagram.py
Name: Helen Lai
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program will find all anagrams of the word that user entered.
    """
    print('Welcome to StanCode \"Anagram Generator\" (or -1 to quit)')

    ####################
    while True:
        s = input('Find anagrams for: ').strip().lower()
        if s == EXIT:
            break
        else:
            start = time.time()
            find_anagrams(s)
    ####################
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    anagram_dic = []
    with open(FILE, 'r') as f:
        for word in f:
            word = word.strip()
            if len(word) == len(s) and check_possibility_anagram(word, s):
                anagram_dic.append(word)
    return anagram_dic


def check_possibility_anagram(word, target_s):
    """
    :param word: str, a word to check whether it will possibly be a anagram of target_s or not
    :param target_s: str, a word user entered to find anagrams
    :return: bool, if the word is possibly a anagram of target_s, then return true, otherwise, return false

    example:
            word == 'otherwise'
            target_s == 'likewise'
            letter == 'l'
    so letter 'l' counts in word is 0, which is smaller than it counts in target_s. Therefore, the word otherwise is
    not an anagram of the target_s likewise.
    """
    for letter in target_s:
        if word.count(letter) < target_s.count(letter):
            return False
    return True


def find_anagrams(s):
    """
    :param s: str, a string user entered and to find anagrams
    :return: str, all anagrams of s
    """

    dic = read_dictionary(s)
    print('Searching...')
    # count each letter in s
    # letter_dic = {}
    # for letter in s:
    #     if letter not in letter_dic:
    #         letter_dic[letter] = 1
    #     else:
    #         letter_dic[letter] += 1

    # count how many anagrams were found
    # anagram = [0]
    anagram_lst = []
    find_anagrams_helper(s, '', anagram_lst, dic)
    print(f'{len(anagram_lst)} anagrams: {anagram_lst}')


def find_anagrams_helper(s, current_s, current_lst, dic):
    if len(s) == 0:
        if current_s not in current_lst:
            current_lst.append(current_s)
            print(f'Found: {current_s}')
            print('Searching...')
    else:
        for i in range(len(s)):

            # Choose
            current_s += s[i]
            remaining_s = s[:i] + s[i+1:]

            # Explore
            if has_prefix(current_s, dic):
                find_anagrams_helper(remaining_s, current_s, current_lst, dic)

            # Un-choose
            current_s = current_s[:-1]


def has_prefix(sub_s, d):
    """
    :param sub_s: str, a substring of the string waiting to find anagrams
    :param d: list, dictionary
    :return: bool, whether there are words started with the substring in the dictionary or not
    """
    for word in d:
        if word.startswith(sub_s):
            return True
            # else:
            #     # when the next letter of word which indexed the length of sub_s
            #     # is not in letter_d, then return False
            #     if word[len(sub_s)] in letter_d:
    return False


# def in_dic(cur_s, dic):
#     """
#     :param cur_s: str, the word waiting for check whether it's included in dic
#     :param dic: list, dictionary
#     :return: bool, if cur_s is in dic, then return True
#     """
#     for word in dic:
#         if cur_s == word:
#             return True


if __name__ == '__main__':
    main()
