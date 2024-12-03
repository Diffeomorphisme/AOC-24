import re
import copy


def read_file():
	with open("day3/input.txt", "r") as file:
		return file.read()


def first_part():
	file_contents = read_file()
	total = 0
	for line in file_contents.splitlines():
		multiplications = re.findall(r"mul\([0-9]+\,[0-9]+\)", line)
		for multiplication in multiplications:
			numbers = re.findall(r"[0-9]+", multiplication)
			total += int(numbers[0]) * int(numbers[1])

	return total


def second_part():
	file_contents = read_file()
	total = 0
	for line in file_contents.splitlines():
		text = line
		dont = re.split(r"don't\(\)", text)
		do = ""
		for i, nope in enumerate(dont):
			print(nope)
			print("".join(re.split(r"do\(\)", nope)))
			do += "".join(re.split(r"do\(\)", nope))
		print(do)
		multiplications = re.findall(r"mul\([0-9]+\,[0-9]+\)", do)
		print(multiplications)
		for multiplication in multiplications:
			numbers = re.findall(r"[0-9]+", multiplication)
			total += int(numbers[0]) * int(numbers[1])

	return total
