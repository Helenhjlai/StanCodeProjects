"""
File: weather_master.py
Name: Helen Lai
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# EXIT = -1
EXIT = -100


def main():
	"""
	This program will find the maximum temperature, the minimum temperature, the mean,
	and how many days of the low temperature alarm
	"""
	print('stanCode \"Weather Master 4.0!\"')
	tem = int(input('Next Temperature: (or ' + str(int(EXIT)) + ' to quit)? '))
	cold_day = 0
	sum_tem = 0
	n = 0
	if tem == EXIT:
		print('No temperatures were entered.')
	else:
		if tem < 16:
			cold_day += 1
		highest_tem = tem
		lowest_tem = tem
		sum_tem += tem
		n += 1
		mean_tem = sum_tem / n
		while True:
			tem = int(input('Next Temperature: (or ' + str(int(EXIT)) + ' to quit)? '))
			if tem == EXIT:
				break
			if tem < 16:
				cold_day += 1
			if tem > highest_tem:
				highest_tem = tem
			if tem < lowest_tem:
				lowest_tem = tem
			sum_tem += tem
			n += 1
			mean_tem = sum_tem / n

		print('Highest Temperature = ' + str(int(highest_tem)))
		print('Lowest Temperature = ' + str(int(lowest_tem)))
		print('Average = ' + str(mean_tem))
		print(str(int(cold_day)) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
