from utils import Grid, split_by_comma, list_of_tuples


up = "^"
down = "v"
left = "<"
right = ">"
directions = [up, down, left, right]
G = Grid(directions)


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = puzzle_input

	def solve(self):
		for i in self.data:
			G.save_move(i)
		self.p1 = len(G.seen)