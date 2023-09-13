from utils import int_list_by_new_line


def format_puzzle_input(puzzle_input):
	puzzle_input = puzzle_input.split('\n\n')
	res = []
	for i in puzzle_input:
		res.append(sum(int_list_by_new_line(i)))
	return res


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = format_puzzle_input(puzzle_input)

	def solve(self):
		self.p1 = max(self.data)
		self.data.sort(reverse=True)	
		self.p2 = sum(self.data[:3])