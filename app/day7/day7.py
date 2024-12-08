import re


def read_file():
	with open("day7/input.txt", "r") as file:
		return file.read()


def calculate_all_results(numbers: list[int]) -> list[int]:
	if len(numbers) == 1:
		return [numbers[0]]
	else:
		all_results = calculate_all_results(numbers[:-1])
		calculated_results = []
		for result in all_results:
			calculated_results.append(numbers[-1] + result)
			calculated_results.append(numbers[-1] * result)
		return calculated_results


def calculate_all_results_2(numbers: list[int]) -> list[int]:
	if len(numbers) == 1:
		return [numbers[-1]]
	else:
		all_results = calculate_all_results_2(numbers[:-1])
		calculated_results = []
		for result in all_results:
			calculated_results.append(numbers[-1] + result)
			calculated_results.append(numbers[-1] * result)
			calculated_results.append(int(str(result) + str(numbers[-1])))
		return calculated_results


def first_part():
	file_contents = read_file()
	total = 0
	for line in file_contents.splitlines():
		equation_total = int(line.split(":")[0])
		numbers = [
			int(number) for number in re.findall(r"[0-9]+", line.split(":")[1])
		]
		if equation_total in calculate_all_results(numbers):
			total += equation_total

	return total


def second_part():
	file_contents = read_file()
	total = 0
	for line in file_contents.splitlines():
		equation_total = int(line.split(":")[0])
		numbers = [
			int(number) for number in re.findall(r"[0-9]+", line.split(":")[1])
		]
		if equation_total in calculate_all_results_2(numbers):
			total += equation_total

	return total
