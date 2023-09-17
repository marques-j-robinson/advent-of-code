from utils import int_list


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = int_list(puzzle_input.split(','))
		self.data[1] = 12
		self.data[2] = 2

	def solve(self):
		EXITCODE = 99
		ADD = 1
		MULTIPLY = 2
		idx = 0
		while idx < len(self.data):
			opcode = self.data[idx]
			if opcode == EXITCODE:
				break
			res_idx = self.data[idx+3]
			first_arg = self.data[idx+1]
			second_arg = self.data[idx+2]
			if opcode == ADD:
				self.data[res_idx] = self.data[first_arg]+self.data[second_arg]
			elif opcode == MULTIPLY:
				self.data[res_idx] = self.data[first_arg]*self.data[second_arg]
			idx += 4
		self.p1 = self.data[0]
