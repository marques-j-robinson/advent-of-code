from Events.solution import Solution
from util import int_list


class S(Solution):

	def solve(self):
		self.data = int_list(self.data)
		prev = self.data[len(self.data)-1]
		half = len(self.data) // 2
		for idx, i in enumerate(self.data):
			if prev == i:
				self.p1 += i
			prev = i
			if idx + half > len(self.data)-1:
				half_i = self.data[idx - half]
			else:
				half_i = self.data[idx + half]
			if half_i == i:
				self.p2 += i