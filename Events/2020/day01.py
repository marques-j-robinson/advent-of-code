from format_data import int_list_by_new_line


def p1(puzzle_input):
	res = 0
	puzzle_input = int_list_by_new_line(puzzle_input)
	for i in puzzle_input:
		for j in puzzle_input:
			if i+j == 2020:
				res = i*j
	return res


def p2(puzzle_input):
	res = 0
	puzzle_input = int_list_by_new_line(puzzle_input)
	for i in puzzle_input:
		for j in puzzle_input:
			for k in puzzle_input:
				if i+j+k == 2020:
					res = i*j*k
	return res