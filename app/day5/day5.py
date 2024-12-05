import copy
import re


def read_file():
	with open("day5/input.txt", "r") as file:
		return file.read()


def extract_update_data(file_contents: str) -> tuple:
	update_order: dict = {}
	updates: list = []
	for line in file_contents.splitlines():
		if "|" in line:
			first_number, second_number = (
				int(number) for number in re.findall("[0-9]+", line)
			)
			if first_number not in update_order.keys():
				update_order[first_number] = [second_number]
			else:
				update_order[first_number].append(second_number)
			if second_number not in update_order.keys():
				update_order[second_number] = []

		elif "," in line:
			updates.append(
				[int(number) for number in re.findall("[0-9]+", line)]
			)
	return update_order, updates


def first_part():
	file_contents = read_file()
	total = 0
	update_order, updates = extract_update_data(file_contents)
	correct_order_updates = []

	for update in updates:
		flag = True
		for page_index, page in enumerate(update):
			for number in update[page_index + 1: len(update)]:
				if number not in update_order[page]:
					flag = False
					break
			if not flag:
				break
		if flag:
			correct_order_updates.append(update)

	for correct_order in correct_order_updates:
		total += correct_order[len(correct_order) // 2]
	return total


def second_part():
	file_contents = read_file()
	total = 0
	update_order, updates = extract_update_data(file_contents)
	incorrect_order_updates = []
	corrected_updates = []

	for update in updates:
		flag = True
		for page_index, page in enumerate(update):
			for number in update[page_index + 1: len(update)]:
				if number not in update_order[page]:
					flag = False
					break
			if not flag:
				break
		if not flag:
			incorrect_order_updates.append(update)

	for update in incorrect_order_updates:
		copy_update = copy.deepcopy(update)
		while True:
			flag = True
			for page_index, page in enumerate(copy_update):
				for number_index, number in enumerate(copy_update[page_index + 1: len(copy_update)]):
					if number not in update_order[page]:
						copy_update[page_index] = number
						copy_update[number_index + page_index + 1] = page
						flag = False
						break
				if not flag:
					break
			if flag:
				corrected_updates.append(copy_update)
				break

	for correct_order in corrected_updates:
		total += correct_order[len(correct_order) // 2]

	return total
