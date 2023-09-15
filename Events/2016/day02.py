from utils import Grid, split_by_new_line


up = "U"
down = "D"
left = "L"
right = "R"
directions = [up, down, left, right]
boundry = 1
G = Grid(directions, boundry)


keypad = {
	'-1,1': 1,
	'0,1': 2,
	'1,1': 3,
	'-1,0': 4,
	'0,0': 5,
	'1,0': 6,
	'-1,-1': 7,
	'0,-1': 8,
	'1,-1': 9,
}


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = split_by_new_line(puzzle_input)

	def solve(self):
		btns = []
		for step in self.data:
			for i in step:
				G.save_move(i)
			btns.append(G.coord)
		self.p1 = "".join([str(keypad[i]) for i in btns])
