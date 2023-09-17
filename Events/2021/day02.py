from utils import split_by_new_line


FORWARD = "forward"
DOWN = "down"
UP = "up"


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = [i.split(" ") for i in split_by_new_line(puzzle_input)]

	def solve(self):
		horizontal_position = 0
		depth = 0
		for i in self.data:
			direction = i[0]
			steps = int(i[1])
			if direction == FORWARD:
				horizontal_position += steps
			elif direction == DOWN:
				depth += steps
			elif direction == UP:
				depth -= steps
		self.p1 += horizontal_position * depth
