def init_format(puzzle_input):
	return puzzle_input.decode('utf-8').rstrip('\n')


def list_of_tuples(puzzle_input):
	return [(d[0], int(d[1:len(d)])) for d in puzzle_input.split(', ')]


def split_by_new_line(puzzle_input):
    return puzzle_input.split('\n')


def split_by_comma(puzzle_input):
    return puzzle_input.split(',')


def int_list_by_new_line(puzzle_input):
    return int_list(split_by_new_line(puzzle_input))


def combine(a, b):
    return len(a + list(set(b) - set(a)))