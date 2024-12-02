import re
import copy


def read_file():
	with open("day2/input.txt", "r") as file:
		return file.read()


def first_part():
	file_contents = read_file()
	total = 0
	for line in file_contents.splitlines():
		numbers: list[int] = [
			int(number) for number in re.findall(r"[0-9]+", line)
		]
		increasing: bool = False
		decreasing: bool = False
		unsafe: bool = False

		for index, number in enumerate(numbers):
			if index == len(numbers) - 1:
				continue
			difference = numbers[index + 1] - number
			if difference == 0 or abs(difference) > 3:
				unsafe = True
				break
			if abs(difference) > 3:
				unsafe = True
				break
			increasing = difference > 0 if difference > 0 else increasing
			decreasing = difference < 0 if difference < 0 else decreasing
			if decreasing and increasing:
				unsafe = True
				break
		if not unsafe:
			total += 1

	return total


def second_part():
	file_contents = read_file()
	total = 0

	for line in file_contents.splitlines():
		numbers: list[int] = [
			int(number) for number in re.findall(r"[0-9]+", line)
		]

		for i in range(len(numbers) + 1):
			increasing: bool = False
			decreasing: bool = False
			unsafe: bool = False
			new_numbers = copy.deepcopy(numbers)
			if i > 0:
				new_numbers.pop(len(numbers) - i)

			for index, number in enumerate(new_numbers):
				if index == len(new_numbers) - 1:
					continue
				difference = new_numbers[index + 1] - number
				if difference == 0 or abs(difference) > 3:
					unsafe = True
					break
				if abs(difference) > 3:
					unsafe = True
					break
				increasing = difference > 0 if difference > 0 else increasing
				decreasing = difference < 0 if difference < 0 else decreasing
				if decreasing and increasing:
					unsafe = True
					break
			if not unsafe:
				total += 1
				break

	return total
