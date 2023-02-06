from format_data import split_by_new_line, int_list


def format_puzzle_input(puzzle_input):
	return [int_list(l.strip().split("\t")) for l in split_by_new_line(puzzle_input)]


def p1(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	for i in puzzle_input:
		res += max(i) - min(i)
	return res


def p2(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	for row in puzzle_input:
		for idx, i in enumerate(row):
			for j in row[idx+1:]:
				m = max([i, j])
				n = min([i, j])
				if m%n==0:
					res += m//n
	return res