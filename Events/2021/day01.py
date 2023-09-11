from utils import int_list_by_new_line


def group_by_three(data):
	res = []
	idx_to_excude = [0,1]
	for idx, i in enumerate(data):
		if idx in idx_to_excude:
			pass
		else:
			res.append(sum([data[idx-2], data[idx-1], i]))
	return res


def solve(data):
	res = 0
	prev = None
	for i in data:
		if prev == None:
			pass
		elif i > prev:
			res += 1
		prev = i
	return res


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = int_list_by_new_line(puzzle_input)
		self.data_group_by_three = group_by_three(self.data)

	def solve(self):
		self.p1 = solve(self.data)
		self.p2 = solve(self.data_group_by_three)
