from Events.solution import Solution
from util import int_list


class S(Solution):

	def format_puzzle_input(self):
		self.split_by_new_line()
		self.data = [int_list(i.strip().split("\t")) for i in self.data]

	def solve(self):
		self.format_puzzle_input()
		for row in self.data:
			self.p1 += max(row) - min(row)
			for idx, i in enumerate(row):
				for j in row[idx+1:]:
					m = max([i, j])
					n = min([i, j])
					if m%n==0:
						self.p2 += m//n