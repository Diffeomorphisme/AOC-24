import re


def read_file():
	with open("day8/input.txt", "r") as file:
		return file.read()


def first_part():
	file_contents = read_file()
	total = 0
	map_length = len(file_contents.splitlines())
	map_width = len(file_contents.splitlines()[0])
	antennas: dict = {}
	antinodes = []

	for line_index, line in enumerate(file_contents.splitlines()):
		for column_index, position in enumerate(line):
			if position.isdigit() or position.isalpha():
				if position in antennas.keys():
					antennas[position].append((line_index, column_index))
				else:
					antennas[position] = [(line_index, column_index)]

	for antenna_type in antennas.keys():
		for antenna_index, antenna in enumerate(antennas[antenna_type][:-1]):
			for second_antenna_index, second_antenna in enumerate(antennas[antenna_type][antenna_index + 1:]):
				difference = (
					antenna[0] - second_antenna[0],
					antenna[1] - second_antenna[1]
				)
				first_antinode = (
					antenna[0] + difference[0],
					antenna[1] + difference[1]
				)
				second_antinode = (
					second_antenna[0] - difference[0],
					second_antenna[1] - difference[1]
				)
				if not (
						first_antinode[0] < 0 or
						first_antinode[0] >= map_length or
					first_antinode[1] < 0 or
					first_antinode[1] >= map_width
				):
					if first_antinode not in antinodes:
						antinodes.append(first_antinode)
						total += 1
				if not (
						second_antinode[0] < 0 or
						second_antinode[0] >= map_length or
					second_antinode[1] < 0 or
					second_antinode[1] >= map_width
				):
					if second_antinode not in antinodes:
						antinodes.append(second_antinode)
						total += 1

	return total


def second_part():
	file_contents = read_file()
	total = 0
	map_length = len(file_contents.splitlines())
	map_width = len(file_contents.splitlines()[0])
	antennas: dict = {}
	antinodes = []

	for line_index, line in enumerate(file_contents.splitlines()):
		for column_index, position in enumerate(line):
			if position.isdigit() or position.isalpha():
				if position in antennas.keys():
					antennas[position].append((line_index, column_index))
				else:
					antennas[position] = [(line_index, column_index)]

	for antenna_type in antennas.keys():
		for antenna_index, antenna in enumerate(antennas[antenna_type][:-1]):
			for second_antenna_index, second_antenna in enumerate(
					antennas[antenna_type][antenna_index + 1:]):
				difference = (
					antenna[0] - second_antenna[0],
					antenna[1] - second_antenna[1]
				)
				i = 0
				while True:
					first_antinode = (
						antenna[0] + i * difference[0],
						antenna[1] + i * difference[1]
					)
					second_antinode = (
						second_antenna[0] - i * difference[0],
						second_antenna[1] - i * difference[1]
					)
					first_antinode_in_map = False
					second_antinode_in_map = False
					if not (
							first_antinode[0] < 0 or
							first_antinode[0] >= map_length or
							first_antinode[1] < 0 or
							first_antinode[1] >= map_width
					):
						first_antinode_in_map = True
						if first_antinode not in antinodes:
							antinodes.append(first_antinode)
							total += 1
					if not (
							second_antinode[0] < 0 or
							second_antinode[0] >= map_length or
							second_antinode[1] < 0 or
							second_antinode[1] >= map_width
					):
						second_antinode_in_map = True
						if second_antinode not in antinodes:
							antinodes.append(second_antinode)
							total += 1

					if (not first_antinode_in_map) and (not second_antinode_in_map):
						break
					i += 1
	return total
