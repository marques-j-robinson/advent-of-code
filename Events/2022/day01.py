from format_data import int_list_by_new_line


def split_by_two_new_line(puzzle_input):
	return puzzle_input.split('\n\n')


def format_puzzle_input(puzzle_input):
	puzzle_input = split_by_two_new_line(puzzle_input)
	res = []
	for i in puzzle_input:
		res.append(sum(int_list_by_new_line(i)))
	return res


def p1(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	for idx, i in enumerate(puzzle_input):
		if i > res:
			res = i
	return res


def p2(puzzle_input):
	puzzle_input = format_puzzle_input(puzzle_input)
	puzzle_input.sort(reverse=True)	
	return sum(puzzle_input[:3])