def init_format(puzzle_input):
	return puzzle_input.decode('utf-8').rstrip('\n')


def list_of_tuples(puzzle_input):
	return [(d[0], int(d[1:len(d)])) for d in puzzle_input.split(', ')]


def split_by_new_line(puzzle_input):
    return puzzle_input.split('\n')


def int_list(a):
    return [int(i) for i in a]


def int_list_by_new_line(puzzle_input):
    return int_list(split_by_new_line(puzzle_input))


def parse_coord(coord):
    return [int(i) for i in coord.split(',')]


def leading_zero(n):
    return str(n).zfill(2)