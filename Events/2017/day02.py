from utils import split_by_new_line, split_by_tab 


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = [[int(j) for j in split_by_tab(i)] for i in split_by_new_line(puzzle_input)]

	def solve(self):
		difs = []
		for row in self.data:
			difs.append(max(row) - min(row))
		self.p1 += sum(difs)