from utils import split_by_new_line


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = [[int(j) for j in i.strip().split()] for i in split_by_new_line(puzzle_input)]

	def solve(self):
		for i in self.data:
			[a, b, c] = i
			valid = True
			if a+b <= c:
				valid = False
			elif b+c <= a:
				valid = False
			elif c+a <= b:
				valid = False
			if valid == True:
				self.p1 += 1