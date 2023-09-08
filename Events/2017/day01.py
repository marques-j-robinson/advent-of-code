from itertools import cycle


from utils import int_list


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = int_list(puzzle_input)

	def solve(self):
		last_idx = len(self.data)-1
		prev = self.data[last_idx]
		half_idx = len(self.data) // 2
		for idx, i in enumerate(self.data):
			if prev == i:
				self.p1 += i
			prev = i
			if idx + half_idx > last_idx:
				half = self.data[idx - half_idx]
			else:
				half = self.data[idx + half_idx]
			if half == i:
				self.p2 += i
