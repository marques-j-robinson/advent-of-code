from format_data import int_list_by_new_line


def compare(puzzle_input):
	res = 0
	for idx, i in enumerate(puzzle_input):
		if idx == 0:
			pass
		else:
			prev = puzzle_input[idx-1]
			if i > prev:
				res += 1
	return res


def p1(puzzle_input):
	puzzle_input = int_list_by_new_line(puzzle_input)
	return compare(puzzle_input)


def three_measurement_window(puzzle_input):
	res = []
	for idx, i in enumerate(puzzle_input):
		if idx <= 2:
			pass
		else:
			first = puzzle_input[idx-2]
			second = puzzle_input[idx-1]
			res.append(first+second+i)
	return res


def p2(puzzle_input):
	puzzle_input = int_list_by_new_line(puzzle_input)
	return compare(three_measurement_window(puzzle_input))