import re


def read_file():
	with open("day1/input.txt", "r") as file:
		return file.read()


def first_part():
	first_list = []
	second_list = []
	file_contents = read_file()
	total = 0
	for line in file_contents.splitlines():
		numbers = re.findall(r"[0-9]+", line)
		first_list.append(int(numbers[0]))
		second_list.append((int(numbers[1])))

	first_list.sort()
	second_list.sort()

	for i, j in zip(first_list, second_list):
		total += abs(j - i)
	return total


def second_part():
	first_list = []
	second_list = []
	file_contents = read_file()
	total = 0
	for line in file_contents.splitlines():
		numbers = re.findall(r"[0-9]+", line)
		first_list.append(int(numbers[0]))
		second_list.append((int(numbers[1])))

	for number in first_list:
		total += number * second_list.count(number)
	return total
