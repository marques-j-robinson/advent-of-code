from main import CacheLayer, int_list


class S(CacheLayer):

	def solve(self):
		self.puzzle_input = int_list(self.puzzle_input)
		prev = self.puzzle_input[len(self.puzzle_input)-1]
		half = len(self.puzzle_input) // 2
		for idx, i in enumerate(self.puzzle_input):
			if prev == i:
				self.p1 += i
			prev = i
			if idx + half > len(self.puzzle_input)-1:
				half_i = self.puzzle_input[idx - half]
			else:
				half_i = self.puzzle_input[idx + half]
			if half_i == i:
				self.p2 += i
