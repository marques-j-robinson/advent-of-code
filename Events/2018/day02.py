from utils import split_by_new_line


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = split_by_new_line(puzzle_input)

	def solve(self):
		two_count = 0
		three_count = 0
		for boxId in self.data:
			letters = {}
			for l in boxId:
				if l not in letters:
					letters[l] = 1
				else:
					letters[l] += 1
			has_two = False
			has_three = False
			for l in letters:
				if letters[l] == 2:
					has_two = True
				elif letters[l] == 3:
					has_three = True
			if has_two is True:
				two_count += 1
			if has_three is True:
				three_count += 1
		self.p1 = two_count * three_count