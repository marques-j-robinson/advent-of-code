def leading_zero(n):
    return str(n).zfill(2)


def init_format(puzzle_input):
	return puzzle_input.decode('utf-8').rstrip('\n')


def parse_coord(coord):
    return [int(i) for i in coord.split(',')]


def list_of_tuples(puzzle_input):
	return [(d[0], int(d[1:len(d)])) for d in puzzle_input.split(', ')]