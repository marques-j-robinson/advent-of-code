from utils import split_by_new_line, int_list
		

target = 2020


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = int_list(split_by_new_line(puzzle_input))

	def solve(self):
		for i in self.data:
			for j in self.data:
				if i+j == target:
					self.p1 = i*j
				for k in self.data:
					if i+j+k == target:
						self.p2 = i*j*k
