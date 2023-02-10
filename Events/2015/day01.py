from Events.solution import Solution

def step(direction):
	up = "("
	if direction == up:
		return 1
	else:
		return -1


def stepping_into_basement(floor_id):
	return floor_id == -1


class S(Solution):


	def solve(self):
		for idx, direction in enumerate(self.data):
			self.p1 += step(direction)
			if self.p2 == 0 and stepping_into_basement(self.p1):
				self.p2 = idx
