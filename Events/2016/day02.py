from format_data import split_by_new_line
from shape import Grid


directions = {
    "up": "U",
    "right": "R",
    "down": "D",
    "left": "L"
}


class NumPad(Grid):

	buttons = []
	keys = {
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

	def record_button(self):
		self.buttons.append(self.coord)

	def press_buttons(self):
		return ''.join([str(self.keys[i]) for i in self.buttons])



def p1(puzzle_input):
	puzzle_input = split_by_new_line(puzzle_input)
	boundries = ['0,2', '1,2', '2,1', '2,0', '2,-1', '1,-2', '0,-2', '-1,-2', '-2,-1', '-2,0', '-2,1', '-1,2']
	num_pad = NumPad(directions, boundries=boundries)
	for instructions in puzzle_input:
		for i in instructions:
			num_pad.move(i)
		num_pad.record_button()
	return num_pad.press_buttons()


def p2(puzzle_input):
	res = 0
	puzzle_input = split_by_new_line(puzzle_input)
	return res