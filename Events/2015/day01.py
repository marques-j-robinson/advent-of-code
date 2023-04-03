from main import CacheLayer


def step(direction):
	up = "("
	if direction == up:
		return 1
	else:
		return -1


class S(CacheLayer):

	def stepping_into_basement(self):
		return self.p1 == -1

	def solve(self):
		for idx, direction in enumerate(self.puzzle_input):
			self.p1 += step(direction)
			if self.p2 == 0 and self.stepping_into_basement():
				self.p2 = idx
