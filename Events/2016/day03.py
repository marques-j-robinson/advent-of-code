from format_data import split_by_new_line, int_list


def format_puzzle_input(puzzle_input):
	return [int_list(l.strip().split()) for l in split_by_new_line(puzzle_input)]


def compare(lengths):
    [a, b, c] = lengths
    return a+b>c and a+c>b and b+c>a


def p1(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	for lengths in puzzle_input:
		if compare(lengths) is True:
			res += 1
	return res


def p2(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	idx = 0
	a = []
	b = []
	c = []
	while idx < len(puzzle_input):
		[a_val, b_val, c_val] = puzzle_input[idx]
		a.append(a_val)
		b.append(b_val)
		c.append(c_val)
		if (idx+1) % 3 == 0:
			if compare(a) is True:
				res += 1
			if compare(b) is True:
				res += 1
			if compare(c) is True:
				res += 1
			a = []
			b = []
			c = []
		idx += 1
	return res