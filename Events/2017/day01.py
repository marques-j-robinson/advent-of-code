from format_data import int_list


def p1(puzzle_input):
	res = 0
	puzzle_input = int_list(puzzle_input)
	prev = puzzle_input[len(puzzle_input) - 1]
	for x in puzzle_input:
		if prev == x:
			res += x
		prev = x
	return res


def p2(puzzle_input):
	res = 0
	puzzle_input = int_list(puzzle_input)
	half = len(puzzle_input) // 2
	for idx, x in enumerate(puzzle_input):
		if idx + half > len(puzzle_input) - 1:
			half_i = puzzle_input[idx - half]
		else:
			half_i = puzzle_input[idx + half]
		if half_i == x:
			res += x
	return res