from Events.solution import Solution
from util import int_list


def compare(lengths):
    [a, b, c] = lengths
    return a+b>c and a+c>b and b+c>a


def is_third(i):
	return (i+1)%3==0


class S(Solution):

	triangles = [[], [], []]

	def compare_triangles(self):
		for i in self.triangles:
			if compare(i):
				self.p2 += 1

	def solve(self):
		self.split_by_new_line()
		self.data = [int_list(i.split()) for i in self.data]
		for idx, lengths in enumerate(self.data):
			if compare(lengths):
				self.p1 += 1
			for tri_idx, i in enumerate(self.triangles):
				i.append(lengths[tri_idx])
			if is_third(idx):
				self.compare_triangles()
				self.triangles = [[], [], []]
