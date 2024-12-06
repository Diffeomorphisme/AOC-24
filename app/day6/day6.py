import re


def read_file():
	with open("day6/input.txt", "r") as file:
		return file.read()


def first_part():
	file_contents = read_file()
	obstacles: list[tuple] = []
	character_symbols = ["^", ">", "v", "<"]
	up = False
	down = False
	left = False
	right = False
	character: tuple = ()
	number_columns = len(file_contents.splitlines()[0])
	number_lines = len(file_contents.splitlines())
	distinct_positions: list[tuple] = []
	total = 0

	for line_index, line in enumerate(file_contents.splitlines()):
		for symbol_index, symbol in enumerate(line):
			if symbol == "#":
				obstacles.append((line_index, symbol_index))
			elif symbol in character_symbols:
				character = (line_index, symbol_index)
				up = symbol == "^"
				down = symbol == "v"
				right = symbol == ">"
				left = symbol == "<"

	while True:
		next_position = character
		if up:
			next_position = (character[0] - 1, character[1])
			if next_position in obstacles:
				up = False
				right = True
				continue
		if down:
			next_position = (character[0] + 1, character[1])
			if next_position in obstacles:
				down = False
				left = True
				continue
		if right:
			next_position = (character[0], character[1] + 1)
			if next_position in obstacles:
				right = False
				down = True
				continue
		if left:
			next_position = (character[0], character[1] - 1)
			if next_position in obstacles:
				left = False
				up = True
				continue
		character = next_position
		if (
				character[0] < 0 or
				character[0] > number_lines - 1 or
				character[1] < 0
				or character[1] > number_columns - 1
		):
			break

		if character not in distinct_positions:
			distinct_positions.append(character)
			total += 1

	return total


def second_part():
	file_contents = read_file()
	obstacles: list[tuple] = []
	character_symbols = ["^", ">", "v", "<"]
	up = False
	down = False
	left = False
	right = False
	character: tuple = ()
	number_columns = len(file_contents.splitlines()[0])
	number_lines = len(file_contents.splitlines())
	position_records: dict = {}
	total = 0

	for line_index, line in enumerate(file_contents.splitlines()):
		for symbol_index, symbol in enumerate(line):
			if symbol == "#":
				obstacles.append((line_index, symbol_index))
			elif symbol in character_symbols:
				character = (line_index, symbol_index)
				up = symbol == "^"
				down = symbol == "v"
				right = symbol == ">"
				left = symbol == "<"
	if up:
		position_records[character] = ["^"]
	elif down:
		position_records[character] = ["v"]
	elif left:
		position_records[character] = ["<"]
	elif right:
		position_records[character] = [">"]
	while True:
		next_position = character
		print(position_records)
		if up:
			next_position = (character[0] - 1, character[1])
			if next_position in obstacles:
				up = False
				right = True
				if not position_records.get(character, []):
					position_records[character] = [">"]
				else:
					position_records[character].append(">")
				continue

			for i in range(next_position[1], number_columns):
				if (next_position[0], i) in obstacles:
					break
				if ">" in position_records.get((next_position[0], i), []):
					total += 1
					print(">")
					print(next_position)
					break
			if not position_records.get(next_position, []):
				position_records[next_position] = ["^"]
			else:
				position_records[next_position].append("^")

		if down:
			next_position = (character[0] + 1, character[1])
			if next_position in obstacles:
				down = False
				left = True
				if not position_records.get(character, []):
					position_records[character] = ["<"]
				else:
					position_records[character].append("<")
				continue

			for i in range(next_position[1], 0, -1):
				if (next_position[0], i) in obstacles:
					break
				if "<" in position_records.get((next_position[0], i), []):
					total += 1
					print("<")
					print(next_position)
					break
			if not position_records.get(next_position, []):
				position_records[next_position] = ["v"]
			else:
				position_records[next_position].append("v")

		if right:
			next_position = (character[0], character[1] + 1)
			if next_position in obstacles:
				right = False
				down = True
				if not position_records.get(character, []):
					position_records[character] = ["v"]
				else:
					position_records[character].append("v")
				continue

			for i in range(next_position[0], number_lines):
				if (i, next_position[1]) in obstacles:
					break
				if "v" in position_records.get((i, next_position[1]), []):
					total += 1
					print("v")
					print(next_position)
					break
			if not position_records.get(next_position, []):
				position_records[next_position] = [">"]
			else:
				position_records[next_position].append(">")

		if left:
			next_position = (character[0], character[1] - 1)
			if next_position in obstacles:
				left = False
				up = True
				if not position_records.get(character, []):
					position_records[character] = ["^"]
				else:
					position_records[character].append("^")
				continue

			for i in range(next_position[0], 0, -1):
				if (i, next_position[1]) in obstacles:
					break
				if "^" in position_records.get((i, next_position[1]), []):
					total += 1
					print("^")
					print(next_position)
					break
			if not position_records.get(next_position, []):
				position_records[next_position] = ["<"]
			else:
				position_records[next_position].append("<")
		character = next_position

		if (
				character[0] < 0 or
				character[0] > number_lines - 1 or
				character[1] < 0
				or character[1] > number_columns - 1
		):
			break

	return total
