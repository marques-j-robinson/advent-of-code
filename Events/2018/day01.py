from format_data import split_by_new_line, int_list


def format_puzzle_input(puzzle_input):
	return int_list(split_by_new_line(puzzle_input))


def p1(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	for i in puzzle_input:
		res += i
	return res


def p2(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	freq = 0
	seen = []
	idx = 0
	while res == 0:
		correct_idx = idx % len(puzzle_input)
		i = puzzle_input[correct_idx]
		if freq in seen:
			res = freq
			break
		else:
			seen.append(freq)
			freq += i
			idx += 1
	return res