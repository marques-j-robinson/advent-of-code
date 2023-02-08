from format_data import split_by_new_line


def format_puzzle_input(puzzle_input):
	puzzle_input = split_by_new_line(puzzle_input)
	for idx, i in enumerate(puzzle_input):
		[direction, steps] = i.split(' ')
		puzzle_input[idx] = (direction, int(steps))
	return puzzle_input


def p1(puzzle_input):
	puzzle_input = format_puzzle_input(puzzle_input)
	horizontal_position = 0
	depth = 0
	for direction, steps in puzzle_input:
		if direction == "up":
			depth -= steps
		elif direction == "down":
			depth += steps
		elif direction == "forward":
			horizontal_position += steps
	return horizontal_position*depth


def p2(puzzle_input):
	puzzle_input = format_puzzle_input(puzzle_input)
	aim = 0
	horizontal_position = 0
	depth = 0
	for direction, steps in puzzle_input:
		if direction == "up":
			aim -= steps	
		elif direction == "down":
			aim += steps
		elif direction == "forward":
			horizontal_position += steps
			depth += aim*steps
	return horizontal_position*depth