from format_data import split_by_new_line
from shape import Grid


directions = {
    "up": "U",
    "right": "R",
    "down": "D",
    "left": "L"
}


num_pad = {
    '-1,1': 1,
    '0,1': 2,
    '1,1': 3,
    '-1,0': 4,
    '0,0': 5,
    '1,0': 6,
    '-1,-1': 7,
    '0,-1': 8,
    '1,-1': 9
}


boundries = ['0,2', '1,2', '2,1', '2,0', '2,-1', '1,-2', '0,-2', '-1,-2', '-2,-1', '-2,0', '-2,1', '-1,2']


def bathroom_code(coords):
	return ''.join([str(num_pad[i]) for i in coords])


def p1(puzzle_input):
	puzzle_input = split_by_new_line(puzzle_input)
	G = Grid(directions, boundries=boundries)
	for instructions in puzzle_input:
		for i in instructions:
			G.move(i)
		G.add_history()
	return bathroom_code(G.history)


def p2(puzzle_input):
	res = 0
	puzzle_input = split_by_new_line(puzzle_input)
	return res