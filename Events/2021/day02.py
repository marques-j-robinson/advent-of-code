from format_data import split_by_new_line
from shape import Grid


directions = {
	"up": "down",
	"down": "up",
	"right": "forward",
	"left": "NA"
}


def format_puzzle_input(puzzle_input):
	puzzle_input = split_by_new_line(puzzle_input)
	for idx, i in enumerate(puzzle_input):
		[direction, steps] = i.split(' ')
		puzzle_input[idx] = (direction, int(steps))
	return puzzle_input


def p1(puzzle_input):
	puzzle_input = format_puzzle_input(puzzle_input)
	G = Grid(directions)
	for direction, steps in puzzle_input:
		while steps > 0:
			steps -= 1
			G.move_auto(direction)	
	return G.x*G.y


def p2(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	return res