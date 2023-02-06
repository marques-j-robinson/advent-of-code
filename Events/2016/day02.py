from format_data import split_by_new_line
from shape import Grid


directions = {
    "up": "U",
    "right": "R",
    "down": "D",
    "left": "L"
}


basic_boundry = ['0,2', '1,2', '2,1', '2,0', '2,-1', '1,-2', '0,-2', '-1,-2', '-2,-1', '-2,0', '-2,1', '-1,2']
basic_keys = {
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


boundry = ['0,3', '1,2', '2,1', '3,0', '2,-1', '1,-2', '0,-3', '-1,-2', '-2,-1', '-3,0', '-2,1', '-1,2']
keys = {
	'0,2': 1,
	'-1,1': 2,
	'0,1': 3,
	'1,1': 4,
	'-2,0': 5,
	'-1,0': 6,
	'0,0': 7,
	'1,0': 8,
	'2,0': 9,
	'-1,-1': 'A',
	'0,-1': 'B',
	'1,-1': 'C',
	'0,-2': 'D'
}


def press_buttons(k, buttons):
	return ''.join([str(k[i]) for i in buttons])


def p1(puzzle_input):
	buttons = []
	puzzle_input = split_by_new_line(puzzle_input)
	G = Grid(directions, boundry=basic_boundry)
	for instructions in puzzle_input:
		for i in instructions:
			G.move(i)
		buttons.append(G.coord)
	return press_buttons(basic_keys, buttons)


def p2(puzzle_input):
	buttons = []
	puzzle_input = split_by_new_line(puzzle_input)
	G = Grid(directions, boundry=boundry, origin='-2,0')
	for instructions in puzzle_input:
		for i in instructions:
			G.move(i)
		buttons.append(G.coord)
	return press_buttons(keys, buttons)
