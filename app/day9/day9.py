def read_file():
	with open("day9/input.txt", "r") as file:
		return file.read()


def rearrange_blocks(individual_blocks: list) -> list:
	i = 0
	while True:

		if "." not in individual_blocks:
			break
		first_free_space = individual_blocks.index(".")
		last_digit = 0
		for index, a in enumerate(individual_blocks[:][::-1]):
			if type(a) == int:
				last_digit = len(individual_blocks) - 1 - index
				break

		if first_free_space > last_digit:
			break
		individual_blocks[first_free_space] = individual_blocks[last_digit]
		individual_blocks = individual_blocks[:last_digit]
		i += 1
	return individual_blocks


def first_part():
	file_contents = read_file()
	total = 0
	individual_blocks = []
	file_index = 0
	for line in file_contents.splitlines():
		for char_index, char in enumerate(line):
			if char_index % 2 == 0 or char_index == 0:
				individual_blocks.extend(int(char) * [file_index])
				file_index += 1
			else:
				individual_blocks.extend(int(char) * ["."])
	rearranged_blocks = rearrange_blocks(individual_blocks)
	for index, block in enumerate(rearranged_blocks):
		if block == ".":
			continue
		total += index * block
	return total


def second_part():
	file_contents = read_file()
	total = 0
	for line in file_contents.splitlines():
		pass
	return total
