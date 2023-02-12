from Events.solution import Solution
from util import Grid
		

directions = ["U", "D", "L", "R"]
G_p1 = Grid(directions)
G_p2 = Grid(directions)


keys_p1 = {
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


keys_p2 = {
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


class NumPad:

	def __init__(self, keys):
		self.buttons = []
		self.keys = keys

	def add_button(self, coord):
		self.buttons.append(self.keys[coord])

	def press_buttons(self):
		print(self.buttons)
		return ''.join([str(i) for i in self.buttons])

class S(Solution):

	def move_p1(self, direction):
		G_p1.move(direction)
		if abs(G_p1.x) == 2 or abs(G_p1.y) == 2:
			pass
		else:
			G_p1.save_coord()

	def move_p2(self, direction):
		G_p2.move(direction)
		if abs(G_p2.x) == 3 or abs(G_p2.y) == 3:
			pass
		elif (abs(G_p2.x) == 2 and abs(G_p2.y) == 1) or (abs(G_p2.y) == 2 and abs(G_p2.x) == 1):
			pass
		else:
			G_p2.save_coord()

	def process_move(self, direction):
		self.move_p1(direction)
		self.move_p2(direction)

	def solve(self):
		self.split_by_new_line()
		numpad_p1 = NumPad(keys_p1)
		numpad_p2 = NumPad(keys_p2)
		for instructions in self.data:
			for direction in instructions:
				self.process_move(direction)
			numpad_p1.add_button(G_p1.coord)
			numpad_p2.add_button(G_p2.coord)
		self.p1 = numpad_p1.press_buttons()
		self.p2 = numpad_p2.press_buttons()