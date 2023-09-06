class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = puzzle_input

	def solve(self):
		for idx, direction in enumerate(self.data):
			if direction == "(":
				self.p1 += 1
			else:
				self.p1 -= 1
			if self.p1 == -1 and self.p2 == 0:
				self.p2 = idx+1