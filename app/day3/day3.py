import re

def read_file():
	with open("day3/input.txt", "r") as file:
		return file.read()


def first_part():
	file_contents = read_file()
	total = 0
	for line in file_contents.splitlines():
		multiplications = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
		for multiplication in multiplications:
			numbers = re.findall(r"[0-9]+", multiplication)
			total += int(numbers[0]) * int(numbers[1])

	return total


def second_part():
	file_contents = read_file()
	total = 0

	matches = re.findall(
		r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)",
		file_contents
	)
	do = True
	for match in matches:
		if match == "do()":
			do = True
		elif match == "don't()":
			do = False
		else:
			if do:
				numbers = re.findall(r"[0-9]+", match)
				total += int(numbers[0]) * int(numbers[1])

	return total
