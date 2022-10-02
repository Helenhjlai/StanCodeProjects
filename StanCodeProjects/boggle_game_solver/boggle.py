"""
File: boggle.py
Name: Helen Lai
----------------------------------------
Boggle is a traditional word game. In this situation, we'll ask user to set up a 4X4 alphabet grid.
And this program will find all possible words in this grid.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ROW = 4


def main():
	"""
	This program will fill all words in a boggle grid.
	"""
	grid = []
	####################
	for i in range(ROW):
		row = input(f'{i+1} row of letters: ')
		while len(row) != (2 * ROW - 1) or num_blank(row) != (ROW - 1):
			print('Illegal input!')
			row = input(f'{i + 1} row of letters: ')
		row_letters = ''
		for letter in row:
			if letter != " ":
				row_letters += letter.lower()
		grid.append(row_letters)

	if len(grid) == ROW:
		start = time.time()
		find_words(grid)
	####################
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def num_blank(s):
	"""
	:param s: str, the letter of one row that user entered
	:return: int, the number of blank
	-----------------------------------------------------------
	To check whether the user entered a correct number blank or not.
	"""
	count = 0
	for i in s:
		if i == " ":
			count += 1
	return count


def read_dictionary(d):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dic = []
	with open(FILE, 'r') as f:
		for word in f:
			word = word.strip()
			if len(word) >= 4 and check_possible(word, d):
				dic.append(word)
	return dic


def check_possible(word, d):
	"""
	:param word: str, the word in dictionary.txt
	:param d: dict, it's a dictionary stores each letter in the boggle grid and its counts
	:return: bool, whether the word is possibly found in the boggle grid
	----------------------------------------------------------------------------
	This program will detect whether a word will possibly found in the boggle grid.
	The solution is to check all letters in a word whether they all includes in the boggle grid.

	EX:
	the boggle grid::
		['fycl',
		'iomg',
		'oril',
		'hjhu']

	    True situation:
	         word == 'firm'
	         all letters ('f' 'i' 'r' 'm') can be found in the boggle grid
		False situation:
			word == 'fyce'
			'e' cannot be found in the boggle grid.
			Therefore, this word will not be included in the dictionary list for searching.
	"""
	for letter in word:
		if letter not in d:
			return False
	return True


def find_words(grid):
	letters = {}  # a dictionary stores each letter in the boggle grid and its counts
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			if grid[x][y] not in letters:
				letters[grid[x][y]] = 1
			else:
				letters[grid[x][y]] += 1

	dic = read_dictionary(letters)
	results = []  # result list

	# define neighbors
	neighbor = [(-1, -1), (-1, 0), (-1, 1),
				(0, -1),           (0, 1),
				(1, -1), (1, 0), (1, 1)]

	for x in range(len(grid)):
		for y in range(len(grid[x])):
			results += find_words_helper(grid, dic, grid[x][y], [], x, y, [(x, y)], neighbor)

	for result in results:
		print(f'Found "{result}"')
	print(f'There are {len(results)} words in total.')


def find_words_helper(grid, dic, cur, found_lst, x, y, used_lst, neighbor):
	if cur in dic and cur not in found_lst:
		found_lst.append(cur)

	for dx, dy in neighbor:
		nx, ny = x + dx, y + dy
		if in_grid(nx, ny, grid) and (nx, ny) not in used_lst:
			# choose
			cur += grid[nx][ny]
			used_lst.append((nx, ny))

			# explore
			if has_prefix(cur, dic):
				find_words_helper(grid, dic, cur, found_lst, nx, ny, used_lst, neighbor)

			# un-choose
			cur = cur[:-1]
			used_lst.pop()
	return found_lst


def in_grid(x, y, grid):
	"""
	:param x: int, current x position
	:param y: int, current y position
	:param grid: list, the boggle grid
	:return: bool, whether current position is in the boggle grid
	"""
	return 0 <= x < len(grid) and 0 <= y < len(grid[x])


def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dic: lst, the dictionary list
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic:
		if word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
