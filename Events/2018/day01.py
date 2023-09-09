from itertools import accumulate, cycle
from utils import split_by_new_line, int_list


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = int_list(split_by_new_line(puzzle_input))

	def solve(self):
		for i in self.data:
			self.p1 += i
		# Could not figure out how to solve this one fast, so looked up a solution here:
		# https://www.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/
		seen = {0}
		self.p2 = next(f for f in accumulate(cycle(self.data)) if f in seen or seen.add(f))
