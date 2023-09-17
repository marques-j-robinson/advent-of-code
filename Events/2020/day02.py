import re
from utils import split_by_new_line


regex = r"(\d*-\d*) ([a-zA-Z]): ([a-zA-Z]*)([a-zA-Z]*)"


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = split_by_new_line(puzzle_input)

	def solve(self):
		for i in self.data:
			res = re.match(regex, i)
			[min_i, max_i] = [int(i) for i in res.group(1).split("-")]
			letter = res.group(2)
			pwd = res.group(3)
			count = 0
			for l in pwd:
				if l == letter:
					count += 1
			self.p1 += count >= min_i and count <= max_i