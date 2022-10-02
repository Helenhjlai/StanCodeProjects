"""
File: largest_digit.py
Name: Helen Lai
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the number which is going to check its largest digit
	:return: int, the largest digit of n
	"""
	n = abs(n)
	return find_largest_digit_helper(n, -float('inf'))


def find_largest_digit_helper(n, largest):
	"""
	:param n: int, the number which is going to check its largest digit
	:param largest: int, the largest digit of the comparison of each run. The started value is set a negative infinite value
	:return: int, the largest digit of n
	"""
	if n == 0:
		return largest
	else:
		module = n % 10
		division = n // 10

		if module > largest:
			largest = module
		return find_largest_digit_helper(division, largest)


if __name__ == '__main__':
	main()
