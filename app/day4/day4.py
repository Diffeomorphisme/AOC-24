def read_file():
    with open("day4/input.txt", "r") as file:
        return file.read()


def first_part():
    possible_xmas = (
        ["X", "M", "A", "S"],
        ["S", "A", "M", "X"],
    )
    file_contents = read_file()
    lines = file_contents.splitlines()
    number_of_columns = len(lines[0])
    number_of_lines = len(lines)

    total = 0
    for line_index in range(len(lines)):
        for column_index in range(len(lines[0])):
            if line_index + 3 < number_of_lines and column_index + 3 < number_of_columns:
                test_x = [
                        lines[line_index][column_index],
                        lines[line_index + 1][column_index + 1],
                        lines[line_index + 2][column_index + 2],
                        lines[line_index + 3][column_index + 3],
                    ]
                if test_x in possible_xmas:
                    total += 1
            if line_index + 3 < number_of_lines:
                test_x = [
                    lines[line_index][column_index],
                    lines[line_index + 1][column_index],
                    lines[line_index + 2][column_index],
                    lines[line_index + 3][column_index],
                ]
                if test_x in possible_xmas:
                    total += 1
            if column_index + 3 < number_of_columns:
                test_x = [
                    lines[line_index][column_index],
                    lines[line_index][column_index + 1],
                    lines[line_index][column_index + 2],
                    lines[line_index][column_index + 3],
                ]
                if test_x in possible_xmas:
                    total += 1
            if line_index - 3 >= 0 and column_index + 3 < number_of_columns:
                test_x = [
                    lines[line_index][column_index],
                    lines[line_index - 1][column_index + 1],
                    lines[line_index - 2][column_index + 2],
                    lines[line_index - 3][column_index + 3],
                ]
                if test_x in possible_xmas:
                    total += 1
    return total


def second_part():
    possible_xmas = (
        [
            ["M", "S"],
            ["A"],
            ["M", "S"]
        ],
        [
            ["S", "S"],
            ["A"],
            ["M", "M"]
        ],
        [
            ["M", "M"],
            ["A"],
            ["S", "S"]
        ],
        [
            ["S", "M"],
            ["A"],
            ["S", "M"]
        ],
    )
    file_contents = read_file()
    lines = file_contents.splitlines()

    total = 0
    for line_index in range(1, len(lines) - 1):
        for column_index in range(1, len(lines[0]) - 1):
            test_x = [
                        [
                            lines[line_index - 1][column_index - 1],
                            lines[line_index - 1][column_index + 1]
                        ],
                        [lines[line_index][column_index]],
                        [
                            lines[line_index + 1][column_index - 1],
                            lines[line_index + 1][column_index + 1]
                        ]
                    ]
            if test_x in possible_xmas:
                total += 1
    return total
